
# Python program to update
# JSON
import json
from datetime import datetime
from urllib.request import Request, urlopen
# function to add to JSON
def write_json(new_data, filename:str):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        # file_data["emp_details"].append(new_data)
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
def addPlugin(pluginName: str):
    y = {"Name": pluginName, "AssemblyVersion": "Unknown", "Status": "Unknown", "Date": "Unknow"}
    if(pluginName != ""):
        write_json(y,"json/pluginlist.json")
        # print ("NAME: "+pluginName)
        print(pluginName+" Added to List")
    else:
        print("Plugin name cannot be empty!")
def addPluginTest(plugin):
    y = {"Name": plugin.get('Name',"null"), "AssemblyVersion": "Unknown", "Status": "Unknown", "Date": "Unknow", "DownloadLinkInstall":plugin.get('DownloadLinkInstall',"null")}
    write_json(y,"json/pluginlist.json")
    # print ("NAME: "+pluginName)
    print(plugin.get('Name',"null")+" Added to List")


# addPlugin("Happ")

def popPlugin(pluginName: str):
    found = False
    with open('json/pluginlist.json', 'r') as file:
        file_data = json.load(file)
    for idx, dictionary in enumerate(file_data):
        if dictionary['Name'] == pluginName:
            file_data.pop(idx)
            print(pluginName+" Removed From PluginList!")
            found = True
    if found == False:
        print("No plugin with Name "+pluginName+" Found")
    with open('json/pluginlist.json', 'w') as file:
        file.write(json.dumps(file_data,indent = 4))
    file.close()
# popPlugin("Happ")

def popPluginTest(plugin):
    found = False
    pluginName = plugin.get('Name',"null")
    pluginLink = plugin.get('DownloadLinkInstall',"null")
    with open('json/pluginlist.json', 'r') as file:
        file_data = json.load(file)
    for idx, dictionary in enumerate(file_data):
        if dictionary['DownloadLinkInstall'] == pluginLink:
            file_data.pop(idx)
            print(pluginName+" Removed From PluginList!")
            found = True
    if found == False:
        print("No plugin with Name "+pluginName+" Found")
    with open('json/pluginlist.json', 'w') as file:
        file.write(json.dumps(file_data,indent = 4))
    file.close()

def addJson(JsonLink: str):
    y = {"Url": JsonLink}
    if(JsonLink != ""):
        write_json(y,"json/resourceList.json")
        # print ("NAME: "+pluginName)
        print(JsonLink+" Added to JsonList")
    else:
        print("Json Link cannot be empty!")


def checkSingleJson(data: dict,ord: int):
    with open('json/pluginlist.json', 'r') as f:
        installedPlugin = json.load(f)
    for value in data:
        Status = "/"
        epoch=value.get('LastUpdate', 0)
        if int(epoch) == 0:
            epoch = value.get('LastUpdated', 0)
        if int(epoch) > 9999999999:
            epoch = int(epoch)/1000
        datetime_obj=datetime.fromtimestamp(int(epoch)).strftime('%Y-%m-%d')
        for value2 in installedPlugin:
            if value['DownloadLinkInstall']== value2['DownloadLinkInstall']:
                Status="Installed"
        y = {"Name": value.get('Name', "NULL"), "AssemblyVersion": value.get('AssemblyVersion', "NULL"), "LastUpdate": str(datetime_obj), "Status": Status, "Author": value.get('Author', "NULL"), "DownloadLinkInstall": value.get('DownloadLinkInstall', "NULL"),"No.URL":ord}
        write_json(y,"json/avaliablePlugins.json")
        print(value['Name']+" Added to List")
        # for names in installedPlugin:
        #     if value['Name'] == names['Name']:
        #         value['Status'] == "Installed"
    # Closing file
    f.close()
def clearAvaliablePlugins():
    with open('json/avaliablePlugins.json', 'w') as f2:
        f2.write(json.dumps([],indent = 4))
    f2.close()
    print("reseted Avaliable plugins")
# clearAvaliablePlugins()
def checkAvaliablePlugins():
    clearAvaliablePlugins()
    f = open('json/resourceList.json')
    data = json.load(f)
    ord = 1
    for value in data:
        url = value['Url']
        print("Checking the url: "+ url)
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(request_site)
        data_json = json.loads(response.read())
        checkSingleJson(data_json,ord)
        ord+=1
    f.close()
# checkAvaliablePlugins()
def removeObjectFromJson(dir:str,key:str,name:str):
    found = False
    with open(dir, 'r') as file:
        file_data = json.load(file)
    for idx, dictionary in enumerate(file_data):
        if dictionary[key] == name:
            file_data.pop(idx)
            print(name +" Removed From "+dir)
            found = True
    if found == False:
        print("No plugin with Name "+name+" Found")
    with open(dir, 'w') as file:
        file.write(json.dumps(file_data,indent = 4))
    file.close()

def modiflyWithKey(dir:str,key:str,name:str,setKey:str,set:str):
    found = False
    with open(dir, 'r') as file:
        file_data = json.load(file)
    for idx, dictionary in enumerate(file_data):
        if dictionary[key] == name:
            #print(dictionary[setKey]+" Set to "+set)
            dictionary[setKey] =set
            found = True
    if found == False:
        print("No plugin with "+key+" "+name+" Found")
    with open(dir, 'w') as file:
        file.write(json.dumps(file_data,indent = 4))
    file.close()