import json, xmltodict

def OpenSavePidlMRU(userprofile):
    data = {"ART0001":{"name":"OpenSavePidlMRU", "isEvent":False, "data":[]}}
    
    with open(r"{}\OpenSavePidlMRU.xml".format(userprofile), encoding='utf-16') as xml_file: 
        data_dict = xmltodict.parse(xml_file.read())
    
    for item in data_dict["open_save_files_list"]["item"]:
        itemd = item.copy()
        
        Ndel = ["filename", "extension", "open_time", "file_modified_time", "file_created_time", "file_size"]
        
        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]
        
        for n in Ndel:
            if item[n] == None:
                del item[n]
        
        data["ART0001"]["data"].append(item)

    json_data = data

    with open("ART0001_OpenSavePidlMRU.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()