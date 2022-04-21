from cgi import print_form
from multiprocessing.connection import wait
from re import A
from selenium import webdriver
import time
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from helium import *
from selenium.common.exceptions import NoSuchElementException        
import msvcrt as m
import random
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
stealth(driver,
     languages=["en-US", "en"],
     vendor="Google Inc.",
     platform="Win32",
     webgl_vendor="Intel Inc.",
     renderer="Intel Iris OpenGL Engine",
     fix_hairline=True,
     )
def wait():
    m.getch()
def auto(dem):
    set_driver(driver)
    if dem>8:
        driver.get('https://traodoisub.com/ex/tiktok_like/')
        driver.find_element_by_id('nhanall').click()
        time.sleep(5)
        dem=0
        auto(dem)
    
    else:
        if Button('love').exists()== True:
            click('love')
            time.sleep(10)
            driver.switch_to.window(driver.window_handles[1])
            set_driver(driver)
            driver.execute_script('document.querySelector("button.tiktok-1xiuanb-ButtonActionItem.ee8s79f0").click()')
            time.sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            set_driver(driver)
            print('so job commit: ',dem)
            timedelay = random.randint(30, 60)
            print('thuc hien cho doi : ',timedelay)
            time.sleep(timedelay)
            dem=dem+1
            auto(dem)
        else:
            print('thuc hien reload la lay job!')
            driver.get('https://traodoisub.com/ex/tiktok_like/')
            driver.find_element_by_id('reload').click()
            time.sleep(5)
            auto(dem)

print("now, it's time for user log-in the tiktok accound")
driver.get("https://www.google.com")
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[2]/a').click()
# time.sleep(3)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('kidcher1415')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(Keys.ENTER)

# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys('thonglovelan')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(Keys.ENTER)
print("press Enter keys...")
wait()

driver.get("https://www.tiktok.com/vi-VN/")
print("press Enter keys...")
wait()

driver.get("https://traodoisub.com/")
set_driver(driver)
driver.find_element_by_id('username').send_keys("kidcher1412")
driver.find_element_by_id('password').send_keys("thongloveuyen")
driver.find_element_by_xpath('/html/body/main/div/div/div/div/div/div/div[2]/div[1]/form/div[4]/button').click()
print("waiting for use installing and set ready #2!")
print("press Enter keys...")
wait()
dem = 0
auto(dem)
