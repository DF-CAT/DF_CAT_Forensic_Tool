import json

import xmltodict


def Jump_Lists(userprofile):
    data = {"ART0008": {"name": "Jump_Lists", "isEvent": False, "data": []}}

    try:
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

            item['name'] = item.pop('filename')
            item['path'] = item.pop('full_path')
            item['accessed_time'] = item.pop('accessed_time')

            for key in item:
                if item[key] is not None:
                    data["ART0008"]["data"].append(item)
                    break

        json_data = data

        with open("ART0008_Jump_Lists.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()

    except:
        pass
