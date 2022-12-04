import json

import xmltodict


def Network_Interfaces(userprofile):
    data = {"ART0003": {"name": "Network_Interfaces", "isEvent": False, "data": []}}

    try:
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

            for key in item:
                if item[key] is not None:
                    data["ART0003"]["data"].append(item)
                    break

        json_data = data

        with open("ART0003_Network_Interfaces.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()

    except:
        pass
