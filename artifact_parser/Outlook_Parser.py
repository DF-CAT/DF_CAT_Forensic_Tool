import json, xmltodict

def Outlook(userprofile):
    data = {"ART_Non5" : {"name" : "Outlook", "isEvent" : False, "data":[]}}
    
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
        
        item["이름"] = item.pop("filename")
        item["from_mail_address"] = item.pop("from_email")
        item["to_mail_address"] = item.pop("to_email")
        item["받은 시간"] = item.pop("message_delivery_time")
        item["크기"] = item.pop("file_size")
        item["from_domain"] = item.pop("domain")
        
        data["ART_Non5"]["data"].append(item)

    json_data = data

    with open("ART_Non5_Outlook.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()