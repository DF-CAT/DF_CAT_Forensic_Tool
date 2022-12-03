import json

import xmltodict


def UserAssist(userprofile):
    data = {"ART0011": {"name": "UserAssist", "isEvent": False, "data": []}}

    with open("{}\\UserAssist.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    for item in data_dict["userassist_items_list"]["item"]:
        if item["modified_time"] is None:
            continue

        itemd = item.copy()

        Ndel = ["item_name", "modified_time"]

        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]

        item['name'] = item.pop('item_name')
        item['modified_time'] = item.pop('modified_time')

        data["ART0011"]["data"].append(item)

    json_data = data

    with open("ART0011_UserAssist.json", "w", encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()
