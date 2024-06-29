import json
from download import *
from urllib.request import Request, urlopen
from datetime import datetime
def update(data: dict):
    with open('json/pluginlist.json', 'r') as f2:
        list_data = json.load(f2)
    for value in data:
        for item in list_data:
            if value['DownloadLinkInstall'] == item['DownloadLinkInstall']:
                if value['AssemblyVersion'] != item['AssemblyVersion']:
                    print("Updated "+ value['Name'] +" From "+ item["AssemblyVersion"] + " To " + value['AssemblyVersion'])
                    item['AssemblyVersion'] = value['AssemblyVersion']
                    tempLink = value["DownloadLinkInstall"]
                    download(tempLink, dest_folder="resource/file/"+value['Name']+"/"+value['AssemblyVersion'])
                    item["Status"] = "Latest"
                    item["Date"] = datetime.today().strftime('%Y-%m-%d %H:%M')
                else:
                    item["Status"] = "Latest"
    # Closing file
    with open('json/pluginlist.json', 'w') as f2:
        f2.write(json.dumps(list_data,indent = 4))
    f2.close()

def resetStatus():
    with open('json/pluginlist.json', 'r') as f2:
        list_data = json.load(f2)
    for item in list_data:
        item['Status'] ="Not Found"
        # Closing file
    with open('json/pluginlist.json', 'w') as f2:
        f2.write(json.dumps(list_data,indent = 4))
    f2.close()

def updateAll():

    print("Resetting status")
    resetStatus()
    f = open('json/resourceList.json')
    data = json.load(f)
    print("Fetching data")
    for value in data:
        url = value['Url']
        print("json/Checking the url: "+ url)
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(request_site)
        data_json = json.loads(response.read())
        update(data_json)
    f.close()
    print("All plugin has been updated")