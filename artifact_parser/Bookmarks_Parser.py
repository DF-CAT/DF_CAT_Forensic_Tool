import json

def Bookmarks(userprofile):
    data = {"ART_Non6":{"name":"Bookmarks", "isEvent":False, "data":[]}}
    js_data = []
        
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
        
        data["ART_Non6"]["data"].append(item)
    
    with open("ART_Non6_Bookmarks.json",'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)