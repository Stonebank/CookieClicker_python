import os
import subprocess
import time

from PIL import ImageGrab
from selenium import webdriver

browser = webdriver.Safari()
browser.maximize_window()
browser.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)

while True:
    browser.find_element_by_id("bigCookie").click()
    battery = int(subprocess.getoutput("pmset -g batt").split("%")[0].split(" ")[6].split("\t")[1])
    if battery <= 24:
        snapchot = ImageGrab.grab()
        snapchot.save("/Users/hk/Desktop/screenshot.png")
        subprocess.call(['osascript', '-e',
                         'tell app "System Events" to shut down'])

