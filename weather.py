import tkinter as tk
import requests
import time

def getweather(canvas):
	city = textfield.get()
	api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=3b9d91db67009a57f32ff6c603902213"
	json_data = requests.get(api).json()
	condition = json_data['weather'][0]['main']
	temp      = int(json_data['main']['temp']-273.15)
	min_temp  = int(json_data['main']['temp_min']-273.15)
	max_temp  = int(json_data['main']['temp_max']-273.15)
	pressure  = json_data['main']['pressure']
	humidity  = json_data['main']['humidity']
	wind      = json_data['wind']['speed']
	sunrise   = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']+19800))
	sunset    = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']+19800))
	final_info = condition + "\n" + str(temp) + "°C"
	final_data = "\n" + "max_temp:" + str(max_temp) + "\n" + "min_temp:" + str(min_temp) + "\n" + "pressure:" + str(pressure) + "\n" "humidity:" + str(humidity) + "\n" + "wind speed:" + str(wind) + "\n" + "sunrise:" + sunrise + "\n" + "sunset:" + sunset
	lable1.config(text = final_info)
	lable2.config(text = final_data)
  
canvas = tk.Tk()
canvas.geometry("575x575")
canvas.title("weather app")

f = ("poppins",20,"bold")
t = ("poppins",34,"bold")

textfield = tk.Entry(canvas,font =t)
textfield.pack(pady = 23)
textfield.focus()
textfield.bind('<Return>',getweather)

lable1 = tk.Label(canvas,font = t)
lable1.pack()
lable2 = tk.Label(canvas,font = f)
lable2.pack()

canvas.mainloop()
