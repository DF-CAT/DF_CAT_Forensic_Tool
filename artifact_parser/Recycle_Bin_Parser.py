import json, csv, os

def Recycle_Bin(userprofile):
    data = {"ART0033" : {"name" : "Recycle_Bin", "isEvent" : False, "data":[]}}
    csv_data = []
    with open("{}\\Recycle_Bin.csv".format(userprofile), 'rt', encoding="utf-8") as f:
        csvReader = csv.DictReader(f)
        
        for rows in csvReader:
            csv_data.append(rows)

    for item in csv_data:
        itemd = item.copy()

        Ndel = ["FileName", "DeletedOn"]

        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]

        data["ART0033"]["data"].append({"이름" : os.path.basename(item["FileName"]), "경로" : item["FileName"], "삭제시간" : item["DeletedOn"]})

    with open(r"ART0033_Recycle_Bin.json", "w", encoding='utf-8') as json_file: 
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        json_file.close()