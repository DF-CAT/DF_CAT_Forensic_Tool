import json
import xmltodict

def OpenSavePidlMRU(userprofile):
    with open(r"{}\OpenSavePidlMRU.xml".format(userprofile), encoding='utf-16') as xml_file: 
        data_dict = xmltodict.parse(xml_file.read()) 

    xml_file.close()

    data_dict["OpenSavePidlMRU"] = data_dict.pop("open_save_files_list")
    data_dict["OpenSavePidlMRU"]["ART0001"] = data_dict["OpenSavePidlMRU"].pop("item")
    
    for i, item in enumerate(data_dict["OpenSavePidlMRU"]["ART0001"]):
        del item['order']
        del item['file_attributes']
        del item['file_owner']
        del item['filename_only']
        
        item["이름"] = item.pop("filename")
        item["확장자"] = item.pop("extension")
        item["실행시간"] = item.pop("open_time")
        item["수정시간"] = item.pop("file_modified_time")
        item["생성시간"] = item.pop("file_created_time")
        item["파일크기"] = item.pop("file_size")
        
        data_dict["OpenSavePidlMRU"]["ART0001"][i] = item

    json_data = data_dict

    with open("OpenSavePidlMRU.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()