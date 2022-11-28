import json
def Shortcut_LNK_Files(userprofile):
    data = {"ART0022":{"name":"Shortcut_LNK_Files", "isEvent":False, "data":[]}}
    
    with open(r"{}\Shortcut_LNK_Files.txt".format(userprofile)) as txt_file:
        result = txt_file.readlines()
        
        for i in result:
            re = i.split('\t')
            data["ART0022"]["data"].append({"이름":re[0], "수정시간":re[9], "경로":re[11]})

    json_data = data

    with open("ART0022_Shortcut_LNK_Files.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()