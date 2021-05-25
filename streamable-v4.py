import random
import os, sys
import requests
import win32api
import keyboard
import platform
import subprocess
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

init()
mouse = Controller()

OSNAME = platform.system()

"""
Getting Chrome version code has been taken from
https://github.com/yeongbin-jo/python-chromedriver-autoinstaller
Thanks goes to him.
"""
if OSNAME == 'Linux':
    OSNAME = 'lin'
    with subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE) as proc:
        version = proc.stdout.read().decode('utf-8').replace('Google Chrome', '').strip()
elif OSNAME == 'Darwin':
    OSNAME = 'mac'
    process = subprocess.Popen(
        ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
    version = process.communicate()[0].decode(
        'UTF-8').replace('Google Chrome', '').strip()
elif OSNAME == 'Windows':
    OSNAME = 'win'
    process = subprocess.Popen(
        ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
    )
    version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
else:
    print('{} OS is not supported.'.format(OSNAME))
    sys.exit()

major_version = version.split('.')[0]

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
        sleep(2.5)
        print(Fore.GREEN)
        self.threadz = int(input('Enter the Amount of Threads (Recommended 10): '+Fore.RED))

        if self.threadz == '':
           print('You Didnt Enter a Valid Thread Amount.')
        sleep(1)
        clear()
        logo()
        for i in range(os.get_terminal_size().columns):
           print(Fore.RED + '─', end='')
        print(Fore.GREEN+'Running Bot..')
        for i in range(os.get_terminal_size().columns):
           print(Fore.RED + '─', end='')

        self.added = 0


    def FAutoPlay(self):
        while True:
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
            sleep(1)
            driver = webdriver.Chrome(options=options,
                                desired_capabilities=opons)
            sleep(1)
            driver.get(link)
            timeout = 400
            try:
                element_present = EC.presence_of_element_located((By.ID, 'player-js'))
                WebDriverWait(driver, timeout).until(element_present)
            finally:
                driver.execute_script(watch_video_js)
                sleep(1.5) #1.5
                driver.refresh()
                sleep(.5)
                driver.refresh()
                sleep(.5)
                driver.refresh()
                sleep(1)
                self.added += 2
                sleep(.5)
                driver.quit()
                sleep(3)
        if self.added >= self.amount:
            os.system("taskkill /F /IM chrome.exe")
            print(Fore.GREEN+"You Have Received The Requested Amount of Views!, Thank you for using Aytu Crypt.")
            sleep(.3)
            sys.exit()
            
    def start_title(self):

        while self.added < self.amount:
            # Elapsed Time / Added * Remaining

            os.system(
                f"title Aytu's Streamable ViewBot - Added: {self.added} Views/{self.amount} Views "
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count() - 2} ^| Botting: {link}'
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
        for _ in range(self.threadz):
            while True:
                if threading.active_count() <= 300:
                    threading.Thread(target=self.FAutoPlay).start()
                    break

if __name__ == '__main__':
    main = AutoPlayF()
    main.start()
