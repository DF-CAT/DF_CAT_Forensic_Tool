import json


def Bookmarks(userprofile):
    data = {"ART0060": {"name": "Bookmarks", "isEvent": False, "data": []}}
    js_data = []

    try:
        with open(r"{}\Bookmarks.json".format(userprofile), encoding="utf-16") as infile:
            js_data = json.load(infile)

        for item in js_data:
            itemd = item.copy()

            Ndel = ["Title", "URL", "Folder Path", "Created Time", "Web Browser"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['name'] = item.pop('Title')
            item['url'] = item.pop('URL')
            item['path'] = item.pop('Folder Path')
            item['created_time'] = item.pop('Created Time')
            item['browser'] = item.pop('Web Browser')

            for key in item:
                if item[key] is not None:
                    data["ART0060"]["data"].append(item)
                    break

        with open("ART0060_Bookmarks.json", 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)

    except:
        pass
