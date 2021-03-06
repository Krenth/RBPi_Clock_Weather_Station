
#!/usr/bin/python3
import tkinter as tk
#from sense_hat import SenseHat
import OWMInterface as OWM

#sense = SenseHat()
#sense.clear()
weather = OWM.getWeatherData()
print(weather)

class Room_Temperature(tk.Frame):
    x = "55"
#    x = str('%0.d' %sense.get_temperature())
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width = 333, height = 50)
        self.label = tk.Label(self, text="°C", 
                              background='#292b5d',
                              foreground="white")
        self.label.pack(side="top", fill="both", expand=True)
        self.update()

    def update(self):
 #       Room_Temperature.x = str('%0.d' %sense.get_temperature())
        Room_Temperature.x = "45"

        bg = self.label.cget("background")
        fg = self.label.cget("foreground")
        self.label.configure(text = str(Room_Temperature.x) + "°C",
                                               background=bg,
                                               foreground=fg,
                                               font=("alfie",72))
        self.after(1000, self.update)

class Room_Pressure(tk.Frame):
#    x = str('%0.d' %sense.get_pressure())
    x = "999"
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width = 333, height = 50)
        self.label = tk.Label(self, text="hPA", 
                              background='#292b5d',
                              foreground="white")
        self.label.pack(side="top", fill="both", expand=True)
        self.update()

    def update(self):
        Room_Pressure.x = "1010"
#        Room_Pressure.x = str('%0.d' %sense.get_pressure())
        bg = self.label.cget("background")
        fg = self.label.cget("foreground")
        self.label.configure(text = str(Room_Pressure.x) + "hPa",
                                               background=bg,
                                               foreground=fg,
                                               font=("alfie",72))
        self.after(1000, self.update)
        
class Room_Humidity(tk.Frame):
#    x = str('%0.d' %sense.get_humidity())
    x = "50"
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width = 333, height = 50)
        self.label = tk.Label(self, text="%", 
                              background='#292b5d',
                              foreground="white")
        self.label.pack(side="top", fill="both", expand=True)
        self.update()

    def update(self):
#        Room_Humidity.x = str('%0.d' %sense.get_humidity())
        Room_Humidity.x = "55"
        bg = self.label.cget("background")
        fg = self.label.cget("foreground")
        self.label.configure(text = str(Room_Humidity.x) + "%",
                                               background=bg,
                                               foreground=fg,
                                               font=("alfie",72))
        self.after(1000, self.update)
        
class Outside_Temperature(tk.Frame):
    weather = OWM.getWeatherData()
    x = str('%0.d' %weather['Temperature'])
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width = 333, height = 50)
        self.label = tk.Label(self, text=Outside_Temperature.x + "°C", 
                              background='#292b5d',
                              foreground="white")
        self.label.pack(side="top", fill="both", expand=True)
        self.update()

    def update(self):
        Outside_Temperature.x = str('%0.d' %weather['Temperature'])
        
        bg = self.label.cget("background")
        fg = self.label.cget("foreground")
        self.label.configure(text = str(Outside_Temperature.x) + "°C",
                                               background=bg,
                                               foreground=fg,
                                               font=("alfie",72))
        self.after(3600000, self.update)
        

class Outside_Pressure(tk.Frame):
    weather = OWM.getWeatherData()
    x = str('%0.d' %weather['Pressure'])
    def __init__(self, parent):
        print(Outside_Pressure.x)
        tk.Frame.__init__(self, parent, width = 333, height = 50)
        self.label = tk.Label(self, text=Outside_Pressure.x + "hPa", 
                              background='#292b5d',
                              foreground="white")
        self.label.pack(side="top", fill="both", expand=True)
        self.update()

    def update(self):
        weather = OWM.getWeatherData()
        Outside_Pressure.x = str('%0.d' %weather['Pressure'])
        print(Outside_Pressure.x)
        bg = self.label.cget("background")
        fg = self.label.cget("foreground")
        self.label.configure(text = str(Outside_Pressure.x) + "hPa",
                                               background=bg,
                                               foreground=fg,
                                               font=("alfie",72))
##        after 1 hour, refresh
        self.after(3600000, self.update)
        
class Outside_Humidity(tk.Frame):
    weather = OWM.getWeatherData()
    x = str('%0.d' %weather['Humidity'])
    def __init__(self, parent):
        print(Outside_Humidity.x)
        tk.Frame.__init__(self, parent, width = 333, height = 50)
        self.label = tk.Label(self, text=Outside_Humidity.x + "%", 
                              background='#292b5d',
                              foreground="white")
        self.label.pack(side="top", fill="both", expand=True)
        self.update()

    def update(self):
        weather = OWM.getWeatherData()
        Outside_Humidity.x = str('%0.d' %weather['Humidity'])
        print(Outside_Humidity.x)
        bg = self.label.cget("background")
        fg = self.label.cget("foreground")
        self.label.configure(text = str(Outside_Humidity.x) + "%",
                                               background=bg,
                                               foreground=fg,
                                               font=("alfie",72))
##        after 1 hour, refresh
        self.after(3600000, self.update)
        
