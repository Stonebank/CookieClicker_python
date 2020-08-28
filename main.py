import subprocess
import time

from PIL import ImageGrab
from selenium import webdriver

shutting_down = False

browser = webdriver.Safari()
browser.maximize_window()
browser.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)

while not shutting_down:
    browser.find_element_by_id("bigCookie").click()
    battery = int(subprocess.getoutput("pmset -g batt").split("%")[0].split(" ")[6].split("\t")[1])
    if battery <= 10:
        screenshot = ImageGrab.grab()
        screenshot.save("/Users/hk/Desktop/screenshot.png")
        subprocess.run(["say", "Bomben er blevet plantet, den vil springe om 40 sekunder."])
        subprocess.call(['osascript', '-e', 'tell app "System Events" to shut down'])
        shutting_down = True

