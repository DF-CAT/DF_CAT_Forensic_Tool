import json

def Browser_Downloads(userprofile):
    data = {"ART_Non1":{"name":"Browser_Downloads", "isEvent":False, "data":[]}}
    js_data = []
        
    with open(r"{}\Browser_Downloads.json".format(userprofile), encoding="utf-16") as infile:
        js_data = json.load(infile)
    
    for item in js_data:
        itemd = item.copy()
        
        Ndel = ["Filename", "Download URL 1", "Start Time", "End Time", "Download Size", "Full Path Filename"]
        
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
        
        data["ART_Non1"]["data"].append(item)
    
    with open("ART_Non1_Browser_Downloads.json",'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)