inputConfig = {
  'inputUrl' : 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE25462', #input should be url of GEO Series
  'pattern' : '<a href="/geo/query/acc.cgi\?acc=GSM.+', #input the pattern (in regex notation) which uniquely defines the sample weblinks only (GSM stands for GEO samples)
  'prefix' :'https://www.ncbi.nlm.nih.gov/', #input should be what needs to be added to truncated sample links obtained from BeautifulSoup. This should be standard across any GEO sample.
  'outputFile' : {
    'name' : 'GSE25462_metaData.csv', # input should be name for csv file that contains final output of relevant information
    'sep' : ',' #specify seperator for writing to csv file
  },

  # these refer to keywords for which we want the values.
  # In particular, for this project, please ensure keywords are fields from the Characteristics section from each sample link.
  # Please also provide values for keys in regex terms (escape metacharacters where applicable)
  # For our example, we use GSE27213. An example of a sample link is https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM624925
  'fieldsOfInterest': [
    { 'name' : 'tissue' },
    { 'name' : 'gender' },
    { 'name' : 'age \(years\)' },
    { 'name' : 'hemoglobin a1c' },
  ]
}

#DO NOT ALTER. This list specifies mandatory key fields of inputConfig that must be populated by user. The key 'fieldsOfInterest' should be an array with key values specified as 'name'.
mandatoryFields = ['inputUrl', 'pattern', 'prefix', 'outputFile.name', 'outputFile.sep', 'fieldsOfInterest.#array.name']