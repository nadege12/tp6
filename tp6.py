def on_button_pressed_a():
    basic.show_number(min2)
    basic.show_number(max2)
    if currenttemperature == min2 or currenttemperature == max2:
        basic.show_string("System is started")
    else:
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(randint(0, 100))
    if input.temperature() < 60:
        basic.show_string("System started")
    elif input.temperature() > 70:
        basic.show_string("System stopped")
    else:
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if input.light_level() > 120:
        for index in range(4):
            basic.show_leds("""
                # # # # #
                                # # # # #
                                # # # # .
                                . # # # #
                                # . # . .
            """)
            basic.pause(500)
    else:
        basic.show_leds("""
            . . # . #
                        . # . # #
                        # . # . .
                        . # . # #
                        # . # . .
        """)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

currenttemperature = 0
max2 = 0
min2 = 0
min2 = 10
max2 = 18
currenttemperature = input.temperature()
max2 = currenttemperature
min2 = currenttemperature

def on_forever():
    global currenttemperature
    basic.show_string(".")
    currenttemperature = input.temperature()
    if currenttemperature > min2:
        basic.show_string("System is started")
    if currenttemperature < max2:
        basic.show_string("System is started")
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)
basic.forever(on_forever)
