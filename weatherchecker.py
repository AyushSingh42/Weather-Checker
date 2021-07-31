from tkinter import *
import requests, json
import sys

root = Tk()
root.geometry("500x500")
root.title("Weather")

l = Label(root, text = "What city would you like to know the weather for? ")
l.pack(pady=20)

e = Entry(root, width= 40)
e.pack(pady=10)

def button():
    button.pack_forget()
    l.pack_forget()
    e.pack_forget()
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = e.get()
    API_KEY = "10c5c30c9c9ee16717b5d60f6de0f807"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        report = data['weather']

        temperature = round((temperature - 273.15) * 9 / 5 + 32)
        temperature = str(temperature)

        final = "It is currently "+temperature+" degrees in "+CITY
        finalreport = f"Weather Report: {report[0]['description']}"

        finalreport = str(finalreport)

    else:
        print(response.status_code)
        print(e.get())
        sys.exit()

    l1 = Label(root, text=final, font=("Helvetica", 18))
    l1.pack(pady=80)

    l2 = Label(root, text=finalreport, font=("Helvetica", 18))
    l2.pack()

button = Button(root, text= "Go!", width = 20, command=button)
button.pack(pady=10)

root.mainloop()