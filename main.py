
from webscrape import *
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
  if (not checkForInputs(mandatoryFields, inputConfig)) :
    raise Exception('Fields of interest not present!')
  fieldNames = getColumnValuesFromList(inputConfig["fieldsOfInterest"] , 'name')
  data = readFromUrl(inputUrl)
  finalData = filterByPattern(pattern,data) #a list of sentences starting with pattern defined
  del finalData[0]
  del finalData[0]

  individualLinksArray = getIndividualLinks(finalData) #list of complete url for each sample
  arrayOfDataFrames = processIndividualLinks(prefix,individualLinksArray,fieldNames)
  print arrayOfDataFrames

  final_df = pd.concat(arrayOfDataFrames) #joins list of dfs into one by merging values under similar column headings
  print final_df.head()


  final_df = final_df[fieldNames]
  final_df.to_csv( inputConfig["outputFile"]["name"], sep = inputConfig["outputFile"]["sep"] , index= False)
#getColumnValuesFromList(inputConfig["fieldsOfInterest"], 'name' )
except Exception,e:
  print 'Exception caught, exiting program: ' , e
  sys.exit()
