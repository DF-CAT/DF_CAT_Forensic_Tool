import json

import xmltodict


def Shell_Bags(userprofile):
    data = {"ART0006": {"name": "Shell_Bags", "isEvent": False, "data": []}}

    try:
        with open("{}\\Shell_Bags.xml".format(userprofile), encoding='utf-16') as xml_file:
            data_dict = xmltodict.parse(xml_file.read())

        for item in data_dict["folders_list"]["item"]:
            itemd = item.copy()

            Ndel = ["path", "last_modified_time"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['path'] = item.pop('path')
            item['modified_time'] = item.pop('last_modified_time')

            for key in item:
                if item[key] is not None:
                    data["ART0006"]["data"].append(item)
                    break

        json_data = data

        with open("ART0006_Shell_Bags.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()

    except:
        pass