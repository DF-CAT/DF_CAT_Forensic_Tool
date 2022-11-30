import json, xmltodict

def Last_Visited_MRU(userprofile):
    data = {"ART0007" : {"name" : "Last_Visited_MRU", "isEvent" : False, "data":[]}}
    
    with open("{}\\Last_Visited_MRU.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    
    for item in data_dict["user_actions_and_events_list"]["item"]:
        itemd = item.copy()
        
        Ndel = ["filename", "full_path", "action_time"]
        
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
        
        data["ART0007"]["data"].append(item)

    json_data = data

    with open("ART0007_Last_Visited_MRU.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()