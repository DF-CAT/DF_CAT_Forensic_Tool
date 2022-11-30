import json, xmltodict

def User_Accounts(userprofile):
    data = {"ART_Non4" : {"name" : "User_Accounts", "isEvent" : False, "data":[]}}
    
    with open("{}\\User_Accounts.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    
    for item in data_dict["profiles_list"]["item"]:
        itemd = item.copy()
        Ndel = ["user_name", "profile_path", "folder_created_time", "registry_modified_time", "logon_time"]
        
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
        
        data["ART_Non4"]["data"].append(item)

    json_data = data

    with open("ART_Non4_User_Accounts.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()