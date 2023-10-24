import json
from download import *
from urllib.request import Request, urlopen
from datetime import datetime
def update(data: dict):
    with open('json/pluginlist.json', 'r') as f2:
        list_data = json.load(f2)
    for value in data:
        for item in list_data:
            if value['Name'] == item['Name']:
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
    # path_to_json_files = 'json/'
    # #get all JSON file names as a list
    # json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

    # for json_file_name in json_file_names:
    #     with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
    #         json_text = json.load(json_file)
    #         update(json_text)
    resetStatus()
    f = open('json/resourceList.json')
    data = json.load(f)
    for value in data:
        url = value['Url']
        print("json/Checking the url: "+ url)
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(request_site)
        data_json = json.loads(response.read())
        update(data_json)
    f.close()
    print("All plugin has been updated")