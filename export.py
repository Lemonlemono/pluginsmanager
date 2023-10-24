import os, json
from download import *
from urllib.request import Request, urlopen
from datetime import datetime
import zipfile
from datetime import datetime
def getZip(data: dict,version: str):
    with open('json/pluginlist.json', 'r') as f2:
        list_data = json.load(f2)
    for value in data:
        for item in list_data:
            if value['Name'] == item['Name']:
                print("Downloading ["+value['Name']+"]...")
                tempLink = value["DownloadLinkInstall"]
                filepath = downloadZip(tempLink, dest_folder="presents/temp/")
                extractPath = "presents/"+version+"/"+value['Name']+"/"+value['AssemblyVersion']
                # print(filepath)
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                    zip_ref.extractall(extractPath)
                os.remove(filepath)
                print("Extracted ["+value["Name"]+"] to "+extractPath)
    # Closing file
    f2.close()

def export(versionName:str):#Read Json
    f = open('json/resourceList.json')
    data = json.load(f)
    f2 = open('json/config.json')
    with open('json/config.json', 'r') as f2:
        configData = json.load(f2)

    for info in configData:
        versionInt = info['Version']
        info['Version']+=1
    with open('json/config.json', 'w') as f2:
        f2.write(json.dumps(configData,indent = 4))
    f2.close() 
    if versionName!="":
        versionName = "["+versionName+"]"
    version = str(versionName+datetime.today().strftime('%Y%m%d'))+str(versionInt)

    for value in data:
        url = value['Url']
        print("Checking the url: "+ url)
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(request_site)
        data_json = json.loads(response.read())
        getZip(data_json,version)
    f.close()