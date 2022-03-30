import csv
import pandas as pdb

#Row[11] and Row[12] are weather conditions
#Row[2] are months
#Row[3] are days
#Row[4] are months

print("Enter month to predict (as number ie. January = 1): ")
month = input()
print("Enter day to predict: ")
day = input()
rain=0
partC=0
clear=0
snow=0
overcast=0

with open('TorontoWeatherFormatted2.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if month in {row[2]} and day in {row[3]}:
                print(row[11])
                if row[11] == 'Rain' or row[12] == 'Rain':
                    rain += 1
                elif row[11] == 'Partly Cloudy' or row[12] == 'Partly Cloudy':
                    partC += 1
                elif row[11] == 'Clear' or row[12] == 'Clear':
                    clear += 1
                elif row[11] == 'Snow' or row[12] == 'Snow':
                    snow += 1
                elif row[11] == 'Overcast' or row[12] == 'Overcast':
                    overcast += 1
                #print(f'\tDate: {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
