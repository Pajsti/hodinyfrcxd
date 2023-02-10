def on_logo_long_pressed():
    timeanddate.set24_hour_time(15, 2, 0)
    timeanddate.set_date(2, 9, 2023)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    basic.show_string(timeanddate.time(timeanddate.TimeFormat.HHMMSS2_4HR))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_three_g():
    basic.show_string("" + str((Kitronik_klimate.humidity())))
    basic.pause(2000)
    basic.show_string("" + str((Kitronik_klimate.pressure(Kitronik_klimate.PressureUnitList.PA))))
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

def on_button_pressed_ab():
    basic.show_string(timeanddate.date(timeanddate.DateFormat.MD))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("" + str((Kitronik_klimate.temperature(Kitronik_klimate.TemperatureUnitList.C))))
input.on_button_pressed(Button.B, on_button_pressed_b)
