import json

import xmltodict


def Recent_Files(userprofile):
    data = {"ART0006": {"name": "Recent_Files", "isEvent": False, "data": []}}

    try:
        with open("{}\\RecentFiles.xml".format(userprofile), encoding='utf-16') as xml_file:
            data_dict = xmltodict.parse(xml_file.read())

        xml_file.close()

        for item in data_dict["last_opened_files"]["item"]:
            if item["filename"] == None:
                continue

            itemd = item.copy()

            Ndel = ["filename", "extension", "modified_time", "created_time", "execute_time", "file_only"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['name'] = item.pop('filename')
            item['extension'] = item.pop('extension')
            item['execute_time'] = item.pop('execute_time')
            item['created_time'] = item.pop('created_time')
            item['modified_time'] = item.pop('modified_time')

            for key in item:
                if item[key] is not None:
                    data["ART0006"]["data"].append(item)
                    break

        json_data = data

        with open("ART0006_Recent_Files.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()

    except:
        pass