import json


def Shortcut_LNK_Files(userprofile):
    data = {"ART0022": {"name": "Shortcut_LNK_Files", "isEvent": False, "data": []}}

    try:
        with open(r"{}\Shortcut_LNK_Files.txt".format(userprofile)) as txt_file:
            result = txt_file.readlines()

            for i in result:
                re = i.split('\t')
                data["ART0022"]["data"].append({"name": re[0], "modified_time": re[9], "path": re[11]})

        json_data = data

        with open("ART0022_Shortcut_LNK_Files.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()

    except:
        pass