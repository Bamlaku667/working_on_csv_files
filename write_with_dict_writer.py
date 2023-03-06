

import csv

def write_with_dict_writer(filename, header, data):
    try:
        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames= header)
            writer.writeheader()
            writer.writerows(data)

    except(IOError, OSError) as err:
        print("unable to write exceptions: {}".format(err))

if __name__ == "__main__":

    header = ['name', 'age', 'gender']
    data = [{'name': "Richard", 'age': 32, 'gender': 'M'}, \
            {'name': "Mumzil", 'age': 21 , 'gender':'F'}, \
            {'name': 'Melinda', 'age': 25, 'gender': 'F'}

    ]

    file_name = 'sample_file2.csv'
    write_with_dict_writer(filename= file_name, header= header, data= data)

        