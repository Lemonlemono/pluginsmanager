
# # Python program to read
# # json file
import json
from checkForUpdate import*
from modiflyPlugin import*
from update import*
# from download import download

# # download("https://love.puni.sh/ment.json", dest_folder="mydir")  
# # Opening JSON file
# f = open('json/ment.json')
# with open('pluginlist.json', 'r') as f2:
#     list_data = json.load(f2)

# # returns JSON object as 
# # a dictionary
# data = json.load(f)
 
# # Iterating through the json
# # list
# nameValues = [item['Name'] for item in list_data]

# print(nameValues)
# print(list_data)

# for value in data:
#     if value['Name'] in nameValues:
#         print(value['Name'], "CurrentVersion: ",value["AssemblyVersion"])
#         tempName = value['Name']
#         tempVersion = value["AssemblyVersion"]
#         tempLink = value["DownloadLinkInstall"]
#         for value in list_data:
#             if value['Name'] in tempName:
#                 if value["AssemblyVersion"] != tempVersion:
#                     print("Updated "+ value['Name'] +" From "+ value["AssemblyVersion"] + " To " + tempVersion)
#                     value["AssemblyVersion"] = tempVersion
#                     download(tempLink, dest_folder="resource/file/"+tempName+"/"+tempVersion)  
                

# Closing file
# f.close()
# with open('pluginlist.json', 'w') as f2:
#     f2.write(json.dumps(list_data))
# f2.close()

def getMyPluginsName():
    f = open('json/pluginlist.json')
    data = json.load(f)
    nameValues = [value['Name'] for value in data]
    f.close()
    return nameValues
def getMyPluginsVersion():
    f = open('json/pluginlist.json')
    data = json.load(f)
    versionValues = [item['AssemblyVersion'] for item in data]
    f.close()
    return versionValues
def getData():
    f = open('json/pluginlist.json')
    data = json.load(f)
    f.close()
    return data
def getAvaliablePluginsData():
    f = open('json/avaliablePlugins.json')
    data = json.load(f)
    f.close()
    return data
def getResourceListData():
    f = open('json/resourceList.json')
    data = json.load(f)
    f.close()
    return data

# print(getMyPluginsName())