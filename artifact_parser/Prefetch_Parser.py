import csv
import json
import os
import re


def Prefetch(csv_files):
    csv_data = []
    data = {"ART0009": {"name": "Prefetch", "isEvent": False, "data": []}}
    exts = '''[.]exe|[.]pdf|[.]hwp|[.]doc|[.]docm|[.]docx|[.]dot|[.]dotx|[.]csv|[.]ppt|[.]pptm|[.]pptx|[.]xlm|[
    .]xls|[.]xlsm|[.]xlsx|[.]zip|[.]rar|[.]7z|[.]txt '''
    for csv_file in csv_files:
        try:
            with open(csv_file, 'rt', encoding="utf-8") as f:
                csvReader = csv.DictReader(f)

                for rows in csvReader:
                    csv_data.append(rows)
        except:
            pass

    for item in csv_data:
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
            if re.search(exts, str(os.path.basename(file)), re.I) is not None:
                files.append(os.path.basename(file))

        if not files:
            continue

        item['name'] = item.pop('ExecutableName')
        item['executed_time'] = item.pop('LastRun')
        item["loaded_files"] = files

        for key in item:
            if item[key] is not None:
                data["ART0009"]["data"].append(item)
                break

    with open(r"ART0009_Prefetch.json", "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        json_file.close()
