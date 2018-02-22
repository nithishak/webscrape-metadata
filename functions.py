from config import *
import sys
import re
import urllib
import pandas as pd
from bs4 import BeautifulSoup 

############################
# Helper function
############################

# schema validator- to check if structure of required inputs is correct
# checkInputsList refers to the list, mandatoryFields in config.py that specifies mandatory fields that must be specified by the user
# inputDict refers to the the dictionary of inputs, inputConfig from config.py
def checkForInputs (checkInputsList, inputDict):
  for i in checkInputsList:
    if i in inputDict:
      continue
    else:
      splitWords = i.split('.') #eg. if i = 'fieldsOfInterest.#array.name', splitWords = ['fieldsOfInterest', '#array', 'name']
      loopVariable = inputDict
      processArray = False
      

      for word in splitWords:
        if (word == '#array' or processArray == True):
          if (word == '#array'):
            processArray = True
            continue
          else:
            processArray = False;
            for innerWord in loopVariable:
              if word not in innerWord:
                return False

        else:
          if word not in loopVariable:
            return False
          else:
            loopVariable = loopVariable[word]
  return True

#helper function - 1 
# inputList is the value for the key 'fieldsOfInterest' in the dictionary inputConfig. It consists of a list of dictionaries which has the format {'columnName' : 'keyword'}
# columnName for this project is 'name' as all keys in the dictionaries of inputList are named 'name'
# produces an list of keywords 
def getColumnValuesFromList(inputList, columnName):
  fieldNames =[]
  for i in inputList:    
    output = i
    for (i,k) in output.items():
      if i == columnName:
        fieldNames.append(k) 
  return fieldNames #eg. fieldNames = ['tissue', 'gender', 'age \\(years\\)', 'hemoglobin a1c']

#helper function - 2
# fetches and reads tURL which is a link in HTML
def readFromUrl(tUrl):
  return str(urllib.urlopen(tUrl).read())

#helper function - 3
# tPattern is the pattern that you want in the sentences returned
# tData is the webpage that has been fetched and read in
# output is a list of all sentences that contain the pattern eg. pattern defined here is '<a href="/geo/query/acc.cgi?acc=GSM'
def filterByPattern(tPattern,tData):
  return re.findall(tPattern, tData) 

#helper function - 4
# tfilteredData is a list of sentences that contain the predefined pattern. An example of a sentence is '<a href="/geo/query/acc.cgi?acc=GSM624925" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM624925</a></td>'
# output is a list of truncated sample links 
def getIndividualLinks(tfilteredData):
  links = []
  for i in tfilteredData: 
    soup = BeautifulSoup(i, "lxml") #parses data from content and makes a BeautifulSoup object (HTML code) on which methods like find_all can be used. eg: '<html><body><a href="/geo/query/acc.cgi?acc=GSM624925" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM624925</a></body></html>'
    sample_link = soup.find_all('a', href=True)[0] #returns a list - even if it is with one result and so we have to choose it using list[0]
    links.append(sample_link['href'])  #this gets us the truncated sample link in the form '/geo/query/acc.cgi?acc=GSM624925'
  return links

#helper function - 5 (called in helper function - 6)
#link refers to an individual sample link, keywords refer to an list of fields under the section "Characteristics" in each sample link for which we want the values
# output is a dictionary per sample that contains keywords as keys, and values for keywords as their values
def get_data_from_links(link, keywords):
    output = {}
    data = readFromUrl(link)
    for i in keywords:
      result = re.findall('(?<={}:\s)\w.*?(?=<br>)'.format(i), data) 
      # ?<= in regex is Lookbehind. This means immediately before the needed output, there should exist, ({}:\s) which refers to the pattern 'keyword: ' in the sample link.
      # (\w.+?) means the output can be zero (this will capture single whole numbers) or more of any characters (this will capture decimals/words) following the first word character (a-z/ A-Z/ 0-9/ -) after the whitespace, non-greedy. (?=<br>) means the result should be followed by, but not include the first instance of '<br>'
      # gives a list of results matching search. if HTML code for the sample link had '<br>hemoglobin a1c: 5.6<br>', and i = 'hemoglobin a1c', result would be ['5.6'].
      # if length of result (which is a list), is 0, target value is not present, and so, no need to append to output 
      if (len(result) > 0):
        output[i] = result[0]
    return output #eg. output = {'gender': 'female', 'tissue': 'skeletal muscle', 'hemoglobin a1c': '5.6', 'age \\(years\\)': '39'} for sample GSM624925

#helper function - 6
# tPrefix refers to the prefix that has to be added to the truncated sample link to make it a complete URL
# tIndividualLinks is a list of complete URLS
# fieldsToPick is a list of keywords already defined
# output is a list of dataframes, containing sample metadata, one per sample
def processIndividualLinks(tPrefix,tIndividualLinks,fieldsToPick):
  arrayOfDataFrames = []
  for link in tIndividualLinks:
    completeLink = tPrefix + link #forms a complete, functional sample URL eg.
    dataDict_per_sample = get_data_from_links(completeLink,fieldsToPick) # creates a dictionary containing keys/fields (columns) we need and values that correspond to them, one per sample, refer to output for helper function 5
    df = pd.DataFrame([dataDict_per_sample]) #changing final_data dictionary to list first and then the list to a df 
    arrayOfDataFrames.append(df) # creates a list of dataframes
  return arrayOfDataFrames
  