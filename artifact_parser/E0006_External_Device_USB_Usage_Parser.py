import json
import xmltodict


def External_Device_USB_Usage(userprofile):
    data = {"E0006": {"name": "External_Device_USB_Usage", "isEvent": True, "data": []}}

    try:
        with open("{}\\External_Device_USB_Usage.xml".format(userprofile), encoding='euc-kr') as xml_file:
            data_dict = xmltodict.parse(xml_file.read())

        for item in data_dict["usb_devices_list"]["item"]:
            itemd = item.copy()

            Ndel = ["description", "device_type", "serial_number", "registry_time_1", "registry_time_2",
                    "driver_description", "instance_id", "capabilities", "connect_time", "disconnect_time"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['created_time'] = item.pop('registry_time_1')
            item['last_plug_unplug_time'] = item.pop('registry_time_2')

            for key in item:
                if item[key] is not None:
                    data["E0006"]["data"].append(item)
                    break

        json_data = data

        with open("E0006_External_Device_USB_Usage.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()

    except:
        pass