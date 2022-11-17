import glob, json

def merge_files():
    data = {"included" : {"artifacts": [], "events": []}}
    
    for f in glob.glob(r"*.json"):
        print(f)
        with open(f, encoding="utf-8") as infile:
            data.append(json.load(infile))
    
    with open("All_Artifacts.json",'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)