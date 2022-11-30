import json, xmltodict

def Outlook(userprofile):
    data = {"ART0003" : {"name" : "E-mail_Attachments", "isEvent" : False, "data":[]}}
    
    with open("{}\\Outlook.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    
    for item in data_dict["outlook_attachments"]["item"]:
        itemd = item.copy()
        Ndel = ["filename", "from_email", "to_email", "message_delivery_time", "file_size", "domain"]
        
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
        
        data["ART0003"]["data"].append(item)

    json_data = data

    with open("ART0003_E-mail_Attachments.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()