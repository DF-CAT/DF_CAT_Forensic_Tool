import glob, json

def merge_files():
    data = []
    
    for f in glob.glob(r"*.json"):
        with open(f, encoding="utf-8") as infile:
            data.append(json.load(infile))
    
    with open("All_Artifacts.json",'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)