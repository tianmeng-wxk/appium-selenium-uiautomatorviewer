# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time  import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
caps = {}
caps["deviceName"] = "A5RNW18320011338"
caps["platformName"] = "Android"
caps["platformVersion"] = "9"
caps["appPackage"] = "com.wawaxcStudent.Android"
caps["appActivity"] = "com.uzmap.pkg.EntranceActivity"
caps["noReset"] = True
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True
sleep(5)
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
WebDriverWait(driver, 20, 0.5).until(lambda el:driver.find_element_by_xpath(""), message="获取失败")
sleep(5)
TouchAction(driver).tap(x=535, y=1019).perform()
sleep(5)
TouchAction(driver).tap(x=268, y=1864).perform()
sleep(5)
TouchAction(driver).tap(x=174, y=103).perform()
sleep(5)
driver.back()
sleep(2)
TouchAction(driver).tap(x=549, y=1099).perform()
sleep(2)
driver.tap([(22,35)],5000)
driver.swipe(1,2,3,4)
