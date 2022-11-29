import json, xmltodict, os

def UserAssist(userprofile):
    data = {"ART0011" : {"name" : "UserAssist", "isEvent" : False, "data":[]}}
    
    with open("{}\\UserAssist.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    
    for item in data_dict["userassist_items_list"]["item"]:
        
        data["ART0011"]["data"].append({"이름" : os.path.basename(item["item_name"]), "경로" : item["item_name"], "수정 시간" : item["modified_time"]})

    json_data = data

    with open("ART0011_UserAssist.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()