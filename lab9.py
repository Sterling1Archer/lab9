from guizero import App, Slider, Text, PushButton
from gpiozero import AngularServo, Servo
import time, math, serial

Arduino_serial_transmit = serial.Serial('/dev/ttyACM0',9600)
Arduino_serial_transmit.flush()

def secondfunc():
    
    app.bg = "#00cc99"
    app.width = 550
    app.height= 200
    wanted_text = Text(app, "")
    wanted_text.text_size = 12
    wanted_text.font = "Times New Roman"
    wanted_text.text_color = "#000000"
    
    slider1 = Slider(app ,start=0,end=180,command=slider_top_changed)
    slider2 = Slider(app ,start=0,end=180,command=slider_bottom_changed)
    
    button_capture_top = PushButton(app,text="Top slider value", align = "left",command=top_value_capture)
    button_capture_bottom = PushButton(app,text="Bottom slider value", align = "left",command=bottom_value_capture)
    
    button_set_top = PushButton(app,text="Set top slider", align = "right",command=set_top_slider)
    button_set_bottom = PushButton(app,text="Set bottom slider", align = "right",command=set_bottom_slider)
    
    return app

def set_top_slider():
    Arduino_serial_transmit.write(bytes(top_servo_position)).encode('utf-8')
    sleep(1)
    
def set_bottom_slider():
    Arduino_serial_transmit.write(bytes(bottom_servo_position)).encode('utf-8')
    sleep(1)
    
def top_value_capture():
    top_servo_position = top_angle

def bottom_value_capture():
    bottom_servo_position = bottom_angle

def slider_top_changed(slider_value):
    print("Slider value: ",slider_value)
    top_angle = bytes(slider_value,'utf-8')
    Arduino_serial_transmit.write(top_angle).encode('utf-8')
    sleep(1)
    print("Angle: ",top_angle)
    
def slider_bottom_changed(slider_value):
    print("Slider value: ",slider_value)
    bottom_angle = bytes(slider_value,'utf-8')
    Arduino_serial_transmit.write(bottom_angle).encode('utf-8')
    sleep(1)
    print("Angle: ",bottom_angle)

if __name__ == '__main__':
    top_angle = ""
    bottom_angle = ""
    top_servo_position = ""
    bottom_servo_position = ""
    s_bottom = AngularServo(26, min_angle=0, max_angle=180)
    s_bottom.angle = None
    s_top = AngularServo(21, min_angle=0, max_angle=180)
    s_top.angle = None
    app = App("RC Servo Controller")
    app2 = secondfunc()
    
    app.display(app2)
    Arduino_serial_transmit.close()