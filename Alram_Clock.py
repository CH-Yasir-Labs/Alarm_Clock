#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     04/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import datetime
import pygame
import keyboard

def set_alarm(alarm_time):
    print(f"Alarm Set for {alarm_time}")

    sound_file = "D:\\python\\Alram_Song.mp3"  # Ensure this path and file are correct
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Wait for the alarm to finish playing or stop when Enter is pressed
            while pygame.mixer.music.get_busy():
                if keyboard.is_pressed("enter"):  # Check if the Enter key is pressed
                    print("Alarm Stopped!")
                    pygame.mixer.music.stop()  # Stop the music
                    is_running = False  # Exit the loop
                    break
                time.sleep(1)  # Reduce CPU usage during the wait

        time.sleep(1)  # Check the time every second


if __name__ == '__main__':
    print("-- Alarm Clock --")
    print("\n---")
    alarm_time = input("Enter the Alarm Time {HH:MM:SS}: ")
    set_alarm(alarm_time)
