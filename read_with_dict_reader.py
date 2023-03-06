import csv 

def read_with_dict_reader(filename):
    try:
        with open(filename , 'r') as f:
            csv_reader = csv.DictReader(f)
            for record in csv_reader:
                print(record)

    except(IOError, OSError) as error:
        print("unable to read csv file exceptions: {}".format(error))
        

if __name__ == "__main__":
    file_name = 'sample_file2.csv'
    read_with_dict_reader(file_name)

