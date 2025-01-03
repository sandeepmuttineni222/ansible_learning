import csv
device_facts={
        "Router_01": {
            "net_api": "cliconf",
            "net_gather_network_resources": [],
            "net_gather_subset": [
                "default"
            ],
            "net_hostname": "Router_01",
            "net_image": "tftp://255.255.255.255/unknown",
            "net_iostype": "IOS",
            "net_model": "7206VXR",
            "net_operatingmode": "autonomous",
            "net_python_version": "3.12.3",
            "net_serialnum": "4279256517",
            "net_system": "ios",
            "net_version": "15.2(4)S6",
            "network_resources": {}
        },
        "Router_02": {
            "net_api": "cliconf",
            "net_gather_network_resources": [],
            "net_gather_subset": [
                "default"
            ],
            "net_hostname": "Router_02",
            "net_image": "tftp://255.255.255.255/unknown",
            "net_iostype": "IOS",
            "net_model": "nokia",
            "net_operatingmode": "autonomous",
            "net_python_version": "3.12.3",
            "net_serialnum": "123456",
            "net_system": "ios",
            "net_version": "15.2(4)S6",
            "network_resources": {}
        }
    }

csv_file_path='/home/sunny/Learning/ansible_learning/Ansible_python_module/generated_csv.csv'
csv_header=['inventory_name','hostname','model','serial_number']

with open(csv_file_path,'w') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=csv_header)
    writer.writeheader()
    for device,details in device_facts.items():
        writer.writerow({
            'inventory_name':device,
            'hostname':details['net_hostname'],
            'model':details['net_model'],
            'serial_number': details['net_serialnum']

        })