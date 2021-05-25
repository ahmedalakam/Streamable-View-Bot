import random
import os, sys
import requests
import win32api
import keyboard
import undetected_chromedriver as uc
import colorama
import threading
from os import system, name
from selenium import webdriver
import contextlib
from colorama import init, Fore
from pynput.mouse import Button, Controller
from time import strftime, gmtime, time, sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


## currently botting https://streamable.com/v05diu

init()
mouse = Controller()

uc.TARGET_VERSION = major_version

uc.install()

def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

clear()

def logo():
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print(f"""{Fore.RED}
     ▄▄▄·  ▄· ▄▌▄▄▄▄▄▄• ▄▌     ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄
    ▐█ ▀█ ▐█▪██▌•██  █▪██▌    ▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██
    ▄█▀▀█ ▐█▌▐█▪ ▐█.▪█▌▐█▌ x  ██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪
    ▐█ ▪▐▌ ▐█▀·. ▐█▌·▐█▄█▌    ▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·
     ▀  ▀   ▀ •  ▀▀▀  ▀▀▀     ·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀
    {Fore.GREEN}             Streamable Spammer By Aytu.\n
    """+Fore.RESET)


logo()
print()
for i in range(os.get_terminal_size().columns):
    print(Fore.RED + '─', end='')



print(Fore.GREEN)
link = input('Streamable Link: '+Fore.RED)

sleep(1)


watch_video_js= """
           let video = document.querySelector('video')
           video.muted = true
           video.play()
      """




class AutoPlayF:


    def __init__(self):
        self.amount = int(input(Fore.GREEN+'Enter the Amount of Views: '+Fore.RED))
        sleep(.5)
        clear()
        logo()
        print(Fore.RED)
        for i in range(os.get_terminal_size().columns):
            print('─', end='')
        sleep(2)

        self.added = 0


    def FAutoPlay(self):
        while True:
            if self.added >= self.amount:
                os.system(Fore.Red"taskkill /F /IM chrome.exe")
                print(Fore.GREEN+"You Have Received The Requested Amount of Views!, Thank you for using Aytu Crypt.")
                sleep(.6)
                sys.exit()
            options = webdriver.ChromeOptions()
            options.add_argument("--log-level=OFF")
            options.add_argument("--headless")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument("--window-size=1400x1080")
            options.add_argument("--mute-audio")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-gpu')
            opons = DesiredCapabilities.CHROME
            opons["pageLoadStrategy"] = "none"
            sleep(.5)
            driver = webdriver.Chrome(options=options,
                                desired_capabilities=opons)
            sleep(.4)
            driver.get(link)
            timeout = 400
            try:
                element_present = EC.presence_of_element_located((By.ID, 'player-js'))
                WebDriverWait(driver, timeout).until(element_present)
            finally:
                driver.execute_script(watch_video_js)
                sleep(.6) #1.5
                driver.refresh()
                sleep(.3)
                driver.refresh()
                sleep(.3)
                driver.refresh()
                sleep(.8)
                self.added += 2
                sleep(.5)
                driver.quit()
                sleep(3)

    def start_title(self):

        while self.added < self.amount:
            # Elapsed Time / Added * Remaining

            os.system(
                f"title Aytu's Streamable ViewBot - Added: {self.added} Views/{self.amount} Views "
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count() - 2} ^|'
            )
            sleep(0.2)
        os.system(
            f"title Aytu's Streamable ViewBot - Added: {self.added}/{self.amount} "
            f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
            f'{threading.active_count() - 2} ^| Finished!'
        )

    def start(self):
        t2 = threading.Thread(target=self.start_title)
        t2.start()

    def threadspeed(self):
        t = threading.Thread(target=self.FAutoPlay)
        t.start()

if __name__ == '__main__':
    main = AutoPlayF()
    main.start()

print(Fore.GREEN)
threadz = int(input('Enter the Amount of Threads (Recommended 10): '+Fore.RED))

if threadz == '':
    print('You Didnt Enter a Valid Thread Amount.')
sleep(1)
clear()
logo()
for i in range(os.get_terminal_size().columns):
    print(Fore.RED + '─', end='')
print(Fore.GREEN+'Running Bot..')
for i in range(os.get_terminal_size().columns):
    print(Fore.RED + '─', end='')

for _ in range(threadz):
    main.threadspeed()
