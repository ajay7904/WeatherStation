from weather_station import *
from tkinter import *

window = Tk()
window.title('Weather Station')
window.minsize(width=500, height=600)
window.config(padx=30, pady=30)

label1 = Label(text="Weather Station", font=('Arial',24,'bold'))
label1.grid(row=0, column=0, columnspan=6)

dummy_label1 = Label(text="", font=('Arial', 12, 'normal'))
dummy_label1.grid(row=1, column=0, sticky='w')

label2 = Label(text="Enter a city name (Ex: London, UK)", font=('Arial',12,'normal'))
label2.grid(row=2, column=0, pady=5, sticky='w')

dummy_label2 = Label(text="", font=('Arial', 12, 'normal'))
dummy_label2.grid(row=4, column=0, sticky='w')

label3 = Label(text="Details", font=('Arial', 12, 'normal'))
label3.grid(row=5, column=0, sticky='w')


city_var = StringVar()
city_var.set("Hyderabad, India")
city_obj = Entry(width=25, font=('Arial',13,'normal'))
city_obj.grid(row=3, column=0, sticky='w')
city_obj.config(textvariable=city_var)
city_obj.focus()

def button_pressed():
    output_box.config(state='normal')
    output_box.delete('1.0', END)
    if city_var.get() == "":
        output_box.insert(END, "Please enter city name..!!!")
    else:
        ws_obj = WeatherStation(city_var.get())
        if ws_obj.response_code == 200:
            content = f"Location: {ws_obj.get_location()[0]}, {ws_obj.get_location()[1]}\n" \
                      f"Current Temperature: {ws_obj.get_temperature()[1]} \N{DEGREE SIGN}C\n" \
                      f"Minimum Temperature: {ws_obj.get_temperature()[0]} \N{DEGREE SIGN}C\n" \
                      f"Maximum Temperature: {ws_obj.get_temperature()[2]} \N{DEGREE SIGN}C\n" \
                      f"Lat / Lon: {ws_obj.get_coordinated()[0]} / {ws_obj.get_coordinated()[1]}\n" \
                      f"Description: {ws_obj.get_description()}\n" \
                      f"Pressure: {ws_obj.get_pressure()} hPa\n" \
                      f"Humidity: {ws_obj.get_humidity()} %\n" \
                      f"Visibility: {ws_obj.get_visibility()}\n" \
                      f"Wind Speed: {ws_obj.get_wind_speed()} km/h\n" \
                      f"Sunrise: {ws_obj.get_daytime()[0]}\n" \
                      f"Sunset: {ws_obj.get_daytime()[1]}\n"

            output_box.insert(END, content)
        else:
            output_box.insert(END, "City not found..!!!")
        del ws_obj
    output_box.config(state='disabled')

button = Button()
button.config(text="Get Weather Data", font=('Arial',12,'normal'), command=button_pressed)
button.grid(row=3, column=1, columnspan=3, padx=20, sticky='w')

output_box = Text(height=15, width=35, font=('Arial',13,'normal'), pady=10, padx=10)
output_box.grid(row=6, column=0, columnspan=2, sticky='w')

window.mainloop()

