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
def checking(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
def wait():
    m.getch()
print("now, it's time for user log-in the tiktok accound")
time.sleep(5)
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

driver.get("https://app.golike.net/home")
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/form/div[1]/input').send_keys("kidcher1412")
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/form/div[2]/input').send_keys("thonglovelan123")
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/form/div[3]/button').click()
print("waiting for use chose #2!")
print("press Enter keys...")
wait()
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/i').click()
print("wating for user chosser #3!")
print("press Enter keys...")
wait()
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/span/div[3]/div/div/div[1]/div[2]/div/div').click()
print("time for user chose accout work good luck and set up")
print("press Enter keys...")
wait()



check_flow = "TĂNG LƯỢT THEO DÕI"
check_tim = "TĂNG LIKE CHO BÀI VIẾT"
index='/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[2]/div'

def big_op():
    set_driver(driver)
    click('Nhận Job ngay')
    time.sleep(3)
    if Button("OK").exists():
        click('OK')
        big_op()
        
    element=driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/span')
    for value in element:
        print ("===================valse= ",(value.text).encode('utf8')) 
    if (value.text).encode('utf8')==check_flow.encode('utf8'):
        print("Nhan Job Theo Doi!")
        click('TikTok')
        driver.switch_to.window(driver.window_handles[1])
        set_driver(driver)
        time.sleep(6)
        click('Follow')
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        set_driver(driver)
        time.sleep(3)

        click('Hoàn thành')
        time.sleep(6)
        if Button("OK").exists():
            print('phat hien nut OK - Xong nhiem vu lanh lua')
            click('OK')
            big_op()
        else:
            print('phat hien checkpoint, thuc hien bypass!')
            click(Point(100, 150))
            time.sleep(4)
            if Button("Hoàn thành").exists():
                driver.find_element_by_xpath("//button[contains(text(),'Hoàn thành')]").click()
                big_op()
            else:
                print("phat hien death lock! thuc hien bypass")
                driver.get('https://app.golike.net/jobs/tiktok')
                set_driver(driver)
                click('Nhận Job ngay')
                click('Báo lỗi')
                click('Gửi báo cáo')
                click('OK')
                big_op()
        print("success!")
    else:
        set_driver(driver)
        print("nhan job tang tim!")
        click('TikTok')
        driver.switch_to.window(driver.window_handles[1])
        set_driver(driver)
        time.sleep(6)

        driver.execute_script('document.querySelector("button.tiktok-1xiuanb-ButtonActionItem.ee8s79f0").click()')

        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        set_driver(driver)
        time.sleep(3)
        click('Hoàn thành')
        time.sleep(6)
        if Button("OK").exists():
            print('phat hien nut OK - Xong nhiem vu lanh lua')
            click('OK')
            big_op()
        else:
            print('phat hien checkpoint, thuc hien bypass!')
            click(Point(100, 150))
            time.sleep(4)
            if Button("Hoàn thành").exists():
                driver.find_element_by_xpath("//button[contains(text(),'Hoàn thành')]").click()
                big_op()
            else:
                print("phat hien death lock! thuc hien bypass")
                driver.get('https://app.golike.net/jobs/tiktok')
                set_driver(driver)
                click('Nhận Job ngay')
                click('Báo lỗi')
                click('Gửi báo cáo')
                click('OK')
                big_op()
        print("success!")
    big_op()
print("complete!!!")
print("bat dau lam viec !")
big_op()






