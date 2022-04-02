import csv
import pandas as pdb

#Row[11] and Row[12] are weather conditions
#Row[2] are months
#Row[3] are days
#Row[4] are months
#Row[5] are max temperature
#Row[6] are min temperature

########Initialize all variables###########
conditions ={'Rain': 0, "Partly Cloudy": 0, "Clear": 0, "Snow": 0, "Overcast": 0}
maxTemp = 0
minTemp = 0
yearCount = 0
###########################################

print("Enter month to predict (as number ie. January = 1): ")
month = input()
print("Enter day to predict: ")
day = input()


with open('TorontoWeatherFormatted2.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: #looks at first line but does nothing as these are just titles
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else: #parse through the rest of the data
            if month in {row[2]} and day in {row[3]}: #match the day and month in data file with the query
                maxTemp += float(row[5])
                minTemp += float(row[6])
                yearCount += 1
                if row[11] == 'Rain' or row[12] == 'Rain':
                    conditions["Rain"] += 1
                elif row[11] == 'Partly Cloudy' or row[12] == 'Partly Cloudy':
                    conditions["Partly Cloudy"] += 1
                elif row[11] == 'Clear' or row[12] == 'Clear':
                    conditions["Clear"] += 1
                elif row[11] == 'Snow' or row[12] == 'Snow':
                    conditions["Snow"] += 1
                elif row[11] == 'Overcast' or row[12] == 'Overcast':
                    conditions["Overcast"] += 1
            line_count += 1

weather = max(conditions, key=conditions.get)
print("On ", month, "/", day, ": \nMaximum Temperature: ", round(maxTemp/yearCount,1) , "\nMinimum Temperature: ", round(minTemp/yearCount, 1) , "\nWeather Condition: ", weather)
