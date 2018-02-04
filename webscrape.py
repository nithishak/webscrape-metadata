from config import *
#print inputConfig
import sys


##########################################
#  Author : Nithisha K
#  Description : <description of what this program does>
#
#  Overview : The code is broken into three segments (each of these sections have been labelled)
#      - inputs - these are the inputs needed to run this program
#      - helper functions - a bunch of functions holding key logic and which have a well defined input and output
#      - main code flow - This block contains a bunch of function calls in a specific order
#
##########################################
import re
import urllib
import pandas as pd
from bs4 import BeautifulSoup
############################
# Helper functions
############################


#schema validator
def checkForInputs (checkInputsList, inputDict):
  false = False
  true = True
  for i in checkInputsList:
    if i in inputDict:
      continue
    else:
      splitWords = i.split('.')
      loopVariable = inputConfig
      processArray = false
      

      for word in splitWords:
        if (word == '#arr' or processArray == true):
          if (word == '#arr'):
            processArray = true
            continue
          else:
            processArray = false;
            for innerWord in loopVariable:
              if word not in innerWord:
                return false

        else:
          if word not in loopVariable:
            return false
          else:
            loopVariable = loopVariable[word]
  return true
     
def getColumnValuesFromList(inputList, columnName):
  fieldValues =[]
  for i in inputList:    
    output = i
    for (i,k) in output.items():
      if i == columnName:
        fieldValues.append(k)
  return fieldValues



#helper function - 1
def readFromUrl(tUrl):
  return str(urllib.urlopen(tUrl).read()) #this reads the whole HTML code for the page

#helper function - 2
def filterByPattern(tPattern,tData):
  return re.findall(tPattern, tData) #output is a list of all sentences that contain the pattern <a href="/geo/query.+"?>

#helper function - 3
def getIndividualLinks(tData):
  links = []
  for i in tData: #prints each <a href...> statement eg: <a href="/geo/query/acc.cgi?acc=GSM2437564" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2437564</a></td>
    soup = BeautifulSoup(i) #parses data from content and makes a BeautifulSoup object on which methods like find_all can be used. eg: <html><body><a href="/geo/query/acc.cgi?acc=GSM2437515" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2437515</a></body></html>
    links.append(soup.find_all('a', href=True)[0]['href'])  #finds only part of sample url we need eg: /geo/query/acc.cgi?acc=GSM2437564
  return links

#helper function - 4 (called in helper function - 5)
#extracts the columns specified by target_vals
def get_data_from_links(link, target_vals):
    output = {}
    data = readFromUrl(link)
    for i in target_vals:
      temp = re.findall('(?<={}:\s)\w+'.format(i), data) #gives a list of results matching search. if i = 'group_ID', temp could be ['B']
      #print "heya"
      #print temp
      # only if the array - temp, is larger that size 0, would it make any sense to try and get the value
      # if it is zero, it the target value was not present
      if (len(temp) > 0):
        output[i] = temp[0]
    return output

#helper function - 5
def processIndividualLinks(tPrefix,tIndividualLinks,fieldsToPick):
  arrayOfDataFrames = []
  for link in tIndividualLinks:
    completeLink = tPrefix + link

    print "processing " ,completeLink
    final_data= get_data_from_links(completeLink,fieldsToPick) #dictionary containing keys/fields (columns) we need and values that correspond to them
    df = pd.DataFrame([final_data]) #changing final_data dictionary to list and then the list to a df
    arrayOfDataFrames.append(df) #list of dataframes
  return arrayOfDataFrames
  