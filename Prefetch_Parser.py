import json
import csv
import os

def Prefetch(csv_files):
    data = {"ART0010" : {"name" : "Prefetch", "isEvent" : False, "data":[]}}
    
    for csv_file in csv_files:
        with open(csv_file, 'rt', encoding="utf-8") as f:
            csvReader = csv.DictReader(f)

            for rows in csvReader:
                data["ART0010"]["data"].append(rows)

    for i, item in enumerate(data["ART0010"]["data"]):
        itemd = item.copy()

        Ndel = ["ExecutableName", "FilesLoaded", "LastRun"]

        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]

        my_list = item["FilesLoaded"].split(',')
        files = []

        for file in my_list:
            files.append(os.path.basename(file))

        item["FilesLoaded"] = files

        item["실행확장자"] = item.pop("ExecutableName")
        item["접근파일"] = item.pop("FilesLoaded")
        item["최근실행시간"] = item.pop("LastRun")

        data["ART0010"]["data"][i] = item

    with open(r"ART0010_Prefetch.json", "w", encoding='utf-8') as json_file: 
        json.dump(data, json_file, indent=4, ensure_ascii=False, sort_keys="True")
        json_file.close()