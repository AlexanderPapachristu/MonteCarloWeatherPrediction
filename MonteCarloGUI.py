import csv
import pandas as pdb
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
#from PIL import ImageTK, Image

#Row[11] and Row[12] are weather conditions
#Row[2] are months
#Row[3] are days
#Row[4] are months
#Row[5] are max temperature
#Row[6] are min temperature
#Row[14] are month names

########Initialize all variables###########
conditions ={'Rain': 0, "Partly Cloudy": 0, "Clear": 0, "Snow": 0, "Overcast": 0}
maxTemp = 0
minTemp = 0
yearCount = 0
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
days = []
for i in range(1,32):
    days.append(i)
###########################################

root = tk.Tk()

root.geometry("800x500")
bgSun = PhotoImage(file="images/sunny.png")
bgOver = PhotoImage(file="images/overcast.png")
bgSnow = PhotoImage(file="images/snowy.png")
bgRain = PhotoImage(file="images/rain.png")
#create Label
#my_label = Label(root,image=bg)
#my_label.place(x=0,y=0, relwidth=1, relheight=1)

# Create a canvas
canvas1 = Canvas(root, width=800, height=500)
canvas1.pack()

# Display background image
container = canvas1.create_image(0,0,image=bgSun,anchor="nw")

def show():
    conditions ={'Rain': 0, "Partly Cloudy": 0, "Clear": 0, "Snow": 0, "Overcast": 0}
    maxTemp = 0
    minTemp = 0
    yearCount = 0
    with open('TorontoWeatherFormatted3.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0: #looks at first line but does nothing as these are just titles
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else: #parse through the rest of the data
                if clickedMon.get() in row[14] and clickedDay.get() in row[3]: #match the day and month in data file with the query
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
    if weather == "Clear":
        canvas1.itemconfig(container,image=bgSun)
    elif weather =="Overcast":
        canvas1.itemconfig(container,image=bgOver)
    elif weather =="Snow":
        canvas1.itemconfig(container,image=bgSnow)

    myLabel.configure(text="On "+ clickedMon.get() + " " + clickedDay.get() + ": \nMaximum Temperature: " +
        str(round(maxTemp/yearCount,1)) + "\nMinimum Temperature: "+ str(round(minTemp/yearCount, 1)) + "\nWeather Condition: " + str(weather))



clickedMon = StringVar()
clickedMon.set(months[0])
clickedDay = StringVar()
clickedDay.set(days[0])
myLabel = Label(canvas1,text="", font=("Helvetica", 20))
myLabel.place(x=0,y=100)

dropMonth = OptionMenu(canvas1, clickedMon, *months)
dropMonth.configure(font=("Helvetica",20))
dropMonth.place(x=0,y=10)

dropDay = OptionMenu(canvas1, clickedDay, *days)
dropDay.configure(font=("Helvetica",20))
dropDay.place(x=150,y=10)

myButton = Button(canvas1, text="Confirm", command=show, font=("Helvetica",20))
myButton.place(x=250,y=5)


root.mainloop()
