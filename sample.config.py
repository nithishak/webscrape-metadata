inputConfig = {
  'inputUrl' : 'INPUT_URL',
  'pattern' : '<a href="/geo/query.+"?>',
  'prefix' :'URI of the data source',
  'outputFile' : {
    'name' : 'GSE92776_metaData.csv',
    'sep' : ','
  },

  
  'fieldsOfInterest': [
    { 'name' : 'field1' },
    { 'name' : 'field2' },
  ]
}

mandatoryFields = ['field1', 'field2']