'''
 Created on Wed Oct 16 2019

 Copyright (c) 2019 Smart Gateway

 Made by Philip Andrew Wee De Wang
'''


import os
import multiprocessing
import time
import sys

is_rpi = True
#Check if it is an rpi and set up the environment if so
try:
    if os.uname().nodename == 'raspberrypi':    
            
        #!/usr/bin/python
        # Example using a character LCD connected to a Raspberry Pi
        import time
        import board
        import digitalio
        import adafruit_character_lcd.character_lcd as character_lcd

        # Raspberry Pi pin setup
        lcd_rs = digitalio.DigitalInOut(board.D26)
        lcd_en = digitalio.DigitalInOut(board.D19)
        lcd_d7 = digitalio.DigitalInOut(board.D11)
        lcd_d6 = digitalio.DigitalInOut(board.D5)
        lcd_d5 = digitalio.DigitalInOut(board.D6)
        lcd_d4 = digitalio.DigitalInOut(board.D13)
        lcd_backlight = digitalio.DigitalInOut(board.D2)

        LCD_RS = 26
        LCD_E  = 19
        LCD_D4 = 13 
        LCD_D5 = 6
        LCD_D6 = 5
        LCD_D7 = 11


        # Define LCD column and row size for 16x2 LCD.
        lcd_columns = 16
        lcd_rows = 2

        lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

except:
    is_rpi = False

#This function is for printing a message for a 16x2 LCD
def print_msg(msg):
    if is_rpi:
        lcd.message = msg
    else:
        print(msg)


class time_handler():

    #This function continuously displays the time
    def show_time_instance(self):
        while True:
            if self.show_time_bool == True:
                print_msg("Time: %s" %time.strftime("%H:%M:%S"))
            sys.stdout.flush()
            time.sleep(0.5)
            

    #Create the thread that constant prints the time
    def __init__(self):
        self.time_process = multiprocessing.Process(target=self.show_time_instance)
        self.time_process.start()
        self.show_time_bool = False

    #This function handles the time thread
    def show_time(self, show):
        if __name__ == "__main__":
            if show == True:
                self.show_time_bool = True
            elif show == False:
                self.show_time_bool = False


    
