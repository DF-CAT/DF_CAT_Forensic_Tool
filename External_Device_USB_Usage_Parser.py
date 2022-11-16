import json
import xmltodict

def External_Device_USB_Usage(userprofile):
    with open("{}\\External_Device_USB_Usage.xml".format(userprofile), encoding='euc-kr') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    xml_file.close()

    data_dict["External Device/USB Usage"] = data_dict.pop("usb_devices_list")
    data_dict["External Device/USB Usage"]["E0006"] = data_dict["External Device/USB Usage"].pop("item")
    
    for i, item in enumerate(data_dict["External Device/USB Usage"]["E0006"]):
        itemd = item.copy()
        
        Ndel = ["description", "device_type", "serial_number", "registry_time_1", "registry_time_2", "driver_description", "instance_id", "capabilities"]
        
        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]
        
        item["장치 설명"] = item.pop("description")
        item["장치 종류"] = item.pop("device_type")
        item["장치 등록번호"] = item.pop("serial_number")
        item["생성날짜"] = item.pop("registry_time_1")
        item["최근 연결날짜"] = item.pop("registry_time_2")
        item["드라이버 설명"] = item.pop("driver_description")
        item["인스턴스 ID"] = item.pop("instance_id")
        item["능력 및 용량"] = item.pop("capabilities")
        
        data_dict["External Device/USB Usage"]["E0006"][i] = item

    json_data = data_dict

    with open("External_Device_USB_Usage.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()