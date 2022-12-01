import json, xmltodict

def Jump_Lists(userprofile):
    data = {"ART0008" : {"name" : "Jump_Lists", "isEvent" : False, "data":[]}}
    
    with open("{}\\Jump_Lists.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    
    for item in data_dict["jump_lists"]["item"]:
        itemd = item.copy()
        
        Ndel = ["filename", "full_path", "accessed_time"]
        
        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]
        
        data["ART0008"]["data"].append(item)

    json_data = data

    with open("ART0008_Jump_Lists.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()