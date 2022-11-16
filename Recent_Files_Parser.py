import json
import xmltodict

def Recent_Files(userprofile):
    with open("{}\\RecentFiles.xml".format(userprofile), encoding='utf-16') as xml_file: 
        data_dict = xmltodict.parse(xml_file.read()) 

    xml_file.close()

    data_dict["Recent Files"] = data_dict.pop("last_opened_files")
    data_dict["Recent Files"]["ART0006"] = data_dict["Recent Files"].pop("item")
    
    for i, item in enumerate(data_dict["Recent Files"]["ART0006"]):
        del item['missing_file']
        del item['stored_in']
        
        item["파일경로"] = item.pop("filename")
        item["확장자"] = item.pop("extension")
        item["수정시간"] = item.pop("modified_time")
        item["생성시간"] = item.pop("created_time")
        item["실행시간"] = item.pop("execute_time")
        item["파일명"] = item.pop("file_only")
        
        data_dict["Recent Files"]["ART0006"][i] = item

    json_data = data_dict

    with open("RecentFiles.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()