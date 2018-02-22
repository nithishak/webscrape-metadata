
from functions import *
################
# inputs
################
inputUrl = inputConfig['inputUrl']
pattern = inputConfig['pattern']
prefix = inputConfig['prefix']


#################
# main code flow
#################


try:
  if (not checkForInputs(mandatoryFields, inputConfig)) : #making sure that all required input fields are present. In the event that they are not, an exception is raised.
    raise Exception('Fields of interest not present!')

  fieldNames = getColumnValuesFromList(inputConfig["fieldsOfInterest"] , 'name') #gets a list of keywords for which we want the values
  data = readFromUrl(inputUrl) #reads in the GSE Series url in HTML
  initialLinks = filterByPattern(pattern,data) #a list of sentences starting with pattern defined (we can expect one sentence per sample)
  completeLinks = getIndividualLinks(initialLinks) #list of truncated urls, one for each sample
  arrayOfDataFrames = processIndividualLinks(prefix, completeLinks,fieldNames) #adds the prefix to the truncated sample links to form proper URLs, and extracts values for keywords from each sample into a dataframe(df)
  final_df = pd.concat(arrayOfDataFrames) #joins list of dfs into one by merging values under similar column headings
  final_df = final_df[fieldNames] #the df will sequence columns according to alphabetical order, to get a column sequence which follows the order in fieldNames, carry out this command
  final_df.to_csv( inputConfig["outputFile"]["name"], sep = inputConfig["outputFile"]["sep"] , index= False) #write final output to a csv file
  print final_df.head()

except Exception,e:
  print 'Exception caught, exiting program: ' , e # this message is shown when the code above encounters any errors and cannot finish executing
  sys.exit()
