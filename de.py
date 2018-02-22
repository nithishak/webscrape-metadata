# from functions import *


# fieldnames = getColumnValuesFromList(inputConfig['fieldsOfInterest'], 'name')
# print fieldnames
# # print type(fieldnames)
# # print fieldnames[1]

# link = readFromUrl(inputConfig['inputUrl'])
# filterbypat = filterByPattern (inputConfig['pattern'], link)
# # print len(filterbypat)
# links = []
# # print soup.find_all('a', href=True)[0]['href']
# for i in filterbypat: 
#     soup = BeautifulSoup(i, "lxml") #parses data from content and makes a BeautifulSoup object (HTML code) on which methods like find_all can be used. eg: '<html><body><a href="/geo/query/acc.cgi?acc=GSM624925" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM624925</a></body></html>'
#     sample_link = soup.find_all('a', href=True)[0]
#     #print sample_link ['href']
#     links.append(sample_link['href'])  


# #values = get_data_from_links('https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM624925', fieldnames)
# output = {}
# data = readFromUrl('https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM624925')
# for i in fieldnames:
#   result = re.findall('(?<={}:\s)\w.+?(?=<br>)'.format(i), data) 
#   if (len(result) > 0):
#     output[i] = result[0]


# df = pd.DataFrame([output])
# final_df = df[fieldnames]
# print df
# print final_df

splitWords = 'fieldsOfInterest.#array.name'.split('.')
print splitWords