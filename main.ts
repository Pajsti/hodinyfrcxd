input.onButtonPressed(Button.A, function () {
    basic.showString(kitronik_RTC.readTime())
})
input.onGesture(Gesture.ThreeG, function () {
    basic.showString("" + (Kitronik_klimate.humidity()))
    basic.pause(2000)
    basic.showString("" + (Kitronik_klimate.pressure(Kitronik_klimate.PressureUnitList.Pa)))
})
input.onButtonPressed(Button.AB, function () {
    basic.showString(kitronik_RTC.readDate())
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (Kitronik_klimate.temperature(Kitronik_klimate.TemperatureUnitList.C)))
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
	
})
kitronik_RTC.setTime(21, 13, 30)
kitronik_RTC.setDate(9, 2, 2023)
timeanddate.set24HourTime(kitronik_RTC.readHours(), kitronik_RTC.readMinutes(), kitronik_RTC.readSeconds())
timeanddate.setDate(kitronik_RTC.readMonth(), kitronik_RTC.readDay(), kitronik_RTC.readYear())
