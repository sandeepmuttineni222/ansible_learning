from ansible.module_utils.basic import AnsibleModule
import csv

def main():
    module = AnsibleModule(
        argument_spec=dict(
        device_facts=dict(type='dict', required=True),
        dest_csv_path=dict(type='str', required=False, default='/home/sunny/Learning/ansible_learning/Ansible_python_module'),
        dest_csv_file=dict(type='str', required=False, default='generated_csv.csv')
        )
    )

    device_facts=module.params['device_facts']
    csv_filename=f"{module.params['dest_csv_path']}/{module.params['dest_csv_file']}"
    csv_file_path=csv_filename
    #csv_file_path='/home/sunny/Learning/ansible_learning/Ansible_python_module/generated_csv.csv'
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

    module.exit_json(changed=True,output='Saved content to csv')

if  __name__ == '__main__':
    main()
