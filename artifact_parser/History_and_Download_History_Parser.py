import json, csv

def History_and_Download_History(userprofile):
    data = {"ART0030" : {"name" : "Web_History", "isEvent" : False, "data":[]}}
    csv_data = []
    with open("{}\\History_and_Download_History.csv".format(userprofile), 'rt', encoding="euc-kr") as f:
        data_dict = csv.DictReader(f)
    
        for rows in data_dict:
                    csv_data.append(rows)
    
    for item in csv_data:
        itemd = item.copy()
        
        Ndel = ["URL", "Visit Time"]
        
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
        
        data["ART0030"]["data"].append(item)

    json_data = data

    with open("ART0030_Web_History.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()