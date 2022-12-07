import csv
import json


def Recycle_Bin(userprofile):
    data = {"ART0033": {"name": "Recycle_Bin", "isEvent": False, "data": []}}
    csv_data = []
    try:
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

            item['name'] = item.pop('FileName')
            item['deleted_time'] = item.pop('DeletedOn')

            for key in item:
                if item[key] is not None:
                    data["ART0033"]["data"].append(item)
                    break

        with open(r"ART0033_Recycle_Bin.json", "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            json_file.close()

    except FileNotFoundError:
        pass
