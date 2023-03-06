
import csv
def write_to_csv(filename, header, data_input):
    """
        filename: the file where the csv data is added,
        header: the header of the file
        data_input: the data to be written 

    """

    try:
        with open(filename, 'w') as csv_file:
            csv_write = csv.writer(csv_file)
            csv_write.writerow(header)
            csv_write.writerows(data_input)


    except(IOError, OSError) as err:
        print('unable to write to csv file execption: {}'.format(err))


if __name__ == '__main__':
    filename = "sample_file.csv"
    header = ['name', 'age', 'gender']
    data = [['Richard', 32, 'M'],['bam', 23, 'M'], ['alemu', 40, 'M'], ["chaltu", 20, 'F']]
    write_to_csv(filename, header, data)

