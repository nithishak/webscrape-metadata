# Project name

Performing webscraping using BeautifulSoup to extract descriptive metadata

##  Environment 

- OS: Ubuntu
- Python 2.X


## Objective: 
To extract metadata information for each sample, using specific keywords for a particular GSE Series from GEO Omnibus

## Project Description
- Gene Expression Omnibus (GEO) is a public genomics data repository that contains several GEO series. 
- Each GEO Series contains information about an experiment, as well as exhibits individual links for each of the experimental links. <br>
  We can take GSE25462 (https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE25462) for instance. This series consists of 50 experimental samples. <br>
  Let us take a look at the bottonm of the GEO Series page where hyperlinks to samples can be found: <br>
  ![1](https://user-images.githubusercontent.com/35882413/36517165-44c47806-174f-11e8-88f2-670ac0f98ff9.png)

- Each experimental sample link contains metadata information regarding the sample. We would like to extract such information. For this project, we will extract information found    under the section Characteristics. The fields in this section will be referred to as keywords in several .py files. For this project, we wish to extract information for the fields 'tissue', 'gender', 'age (years)' and 'hemoglobin a1c' <br>
  An experimental sample weblink (https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM624925) would look like this: <br>
  ![2](https://user-images.githubusercontent.com/35882413/36517166-44d9f000-174f-11e8-8bca-a81e25c0e0f2.png)

- The metadata can also be found on the GSE Series page under the Series Matrix File but this often requires the user to go through a huge file and choose relevant columns. 
- To avoid such hassle, this project shows an alternate method in the form of webscraping, where the user can choose keywords for the types of metadata he wishes to know for
  each sample, and obtain it for all samples as a dataframe output. Each row in the dataframe corresponds to a sample. Please note that as this project was carried out to extract phenodata for differential gene analysis, the sample names are contained as the column names of assayData and as such, are not found in this data frame.<br> 
  The output would look like this: <br>
  ![3](https://user-images.githubusercontent.com/35882413/36517167-44eedc2c-174f-11e8-98f8-f0303539f674.png)


## Libraries needed: 
1. urllib (part of standard Python 2.X libraries, no need to pip install) 
2. re (part of standard Python 2.X libraries, no need to pip install) 
2. pandas <br>
To install, type: <br>
```` sudo pip install pandas ````
3. BeautifulSoup <br>
To install, type: <br>
```` sudo apt-get install python-bs4 ````


## Files available: 
1. config.py - contains input fields as a python dictionary
2. functions.py - contains several helper functions
3. main.py - contains main code which uses the helper functions


## Details: 
- The first step of this project would be to define the keywords for which we wish to get the values for.
- This would be followed by reading in the URL for the GSE Series as this page contains the hyperlinks to each sample that is involved in this experiment.
- Based on a unique HTML pattern, extract the links for the samples from the series page that has been read in. To do this, we can highlight a sample hyperlink, right click on it, and choose the option inspect. The pattern chosen here is '<a href="/geo/query/acc.cgi\?acc=GSM' as GSM represent sample information.
- From these links, we can use BeautifulSoup to extract part of the sample link. An example of what we would get would be /geo/query/acc.cgi?acc=GSM624925'.
- By pre defining a prefix, we can add to the truncated sample link to form a complete, functional link like 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM624925'.
- Each functional sample link can then be read in, and values for relevant keywords extracted into a dataframe. At this point, we have a list of dataframes that contain metadata, one dataframe per sample.
- Last but not least, the list of dataframes can be concatenated into one dataframe based on similar column headings and written to a .csv file.


## How to run? :
- Run the main.py file but remember to change relevant parameters in config.py.
