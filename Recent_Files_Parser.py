import json, xmltodict

def Recent_Files(userprofile):
    data = {"ART0006":{"name":"Recent_Files", "isEvent":False, "data":[]}}
    
    with open("{}\\RecentFiles.xml".format(userprofile), encoding='utf-16') as xml_file: 
        data_dict = xmltodict.parse(xml_file.read()) 

    xml_file.close()
    
    for item in data_dict["last_opened_files"]["item"]:
        del item['missing_file']
        del item['stored_in']
        
        item["파일경로"] = item.pop("filename")
        item["확장자"] = item.pop("extension")
        item["수정시간"] = item.pop("modified_time")
        item["생성시간"] = item.pop("created_time")
        item["실행시간"] = item.pop("execute_time")
        item["파일명"] = item.pop("file_only")
        
        data["ART0006"]["data"].append(item)

    json_data = data

    with open("ART0006_Recent_Files.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()