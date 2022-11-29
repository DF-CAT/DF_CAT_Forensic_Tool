import json, xmltodict

def Network_Interfaces(userprofile):
    data = {"ART_Non3" : {"name" : "Network_Interfaces", "isEvent" : False, "data":[]}}
    
    with open("{}\\Network_Interfaces.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    
    for item in data_dict["network_interfaces"]["item"]:
        itemd = item.copy()
        
        Ndel = ["device_name", "connection_name", "ip_address", "subnet_mask", "registry_time"]
        
        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]
        
        item["이름"] = item.pop("device_name")
        item["연결 정보"] = item.pop("connection_name")
        item["IP"] = item.pop("ip_address")
        item["서브넷 마스크"] = item.pop("subnet_mask")
        item["연결 시간"] = item.pop("registry_time")
        
        data["ART_Non3"]["data"].append(item)

    json_data = data

    with open("ART_Non3_Network_Interfaces.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()