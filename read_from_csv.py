import csv

def read_csv(filename):
    try:
        with open(filename) as f:
            csv_reader = csv.reader(f)
            for record in csv_reader:
                print(record)

    except(IOError , OSError) as err:
        print("unable to read a csv file exeption: {}".format(err))

if __name__ == "__main__":
    filename = 'sample_file.csv'
    read_csv(filename)


