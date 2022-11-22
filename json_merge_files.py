import glob, json, re

def merge_files():
    data = {"included" : {"artifacts": [], "events": []}}
    art_len = len(glob.glob(r"*.json"))
    
    for f in glob.glob(r"*.json"):
        if re.search("ART", f):
            num = re.sub(r'[^0-9]', '', f)
            data["included"]["artifacts"].append("ART"+str(num))
        else:
            num = re.sub(r'[^0-9]', '', f)
            data["included"]["events"].append("E"+str(num))
        
        with open(f, encoding="utf-8") as infile:
            data.update(json.load(infile))
    
    with open("Collect_Result_{}.json".format(art_len),'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    
    return art_len