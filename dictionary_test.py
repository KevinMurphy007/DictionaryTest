"""
Sample dictionary init from CSV
in the simple case of the CSV being
exactly key-value pairs

"""
import os
import csv
my_dict = dict()

my_dir = os.path.dirname(os.path.realpath(__file__))

filename = 'dictionary_test.csv'

# TODO: read the data from the csv file and put into dictionary
with open(my_dir + '/' + filename) as infile:
    reader = csv.reader(infile)
    for row in reader:
        key = int(row[0])
        value = row[1].strip()
        my_dict[key] = value
# print(read_data)


print(my_dict)

# This should print out 'Joe'
print(my_dict[1])
