from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://hcs.eduro.go.kr/#/loginHome")
elem = driver.find_element_by_id("btnConfirm2").click()
elem = driver.find_element_by_class_name("searchBtn").click()
elem = driver.find_element_by_id("sidolabel").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td/select/option[3]").click()
elem = driver.find_element_by_class_name("nodata").click()
elem = driver.find_element_by_id("crseScCode").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td/select/option[5]").click()
elem = driver.find_element_by_class_name("nodata").click()
elem = driver.find_element_by_class_name("searchArea")
elem.send_keys("부산소프트웨어마이스터고")
elem = driver.find_element_by_class_name("searchBtn").click()
import pyautogui
pyautogui.moveTo(700,700)
pyautogui.click()
pyautogui.click()
elem = driver.find_element_by_id("user_name_input")
elem.send_keys("진유림")
elem = driver.find_element_by_id("birthday_input")
elem.send_keys("050120")
elem = driver.find_element_by_id("btnConfirm").click()
from time import sleep
sleep(0.4)
elem = driver.find_element_by_class_name("input_text_common")
elem.send_keys("0120")
elem = driver.find_element_by_id("btnConfirm").click()
from time import sleep
sleep(0.6)
pyautogui.moveTo(120,800)
pyautogui.click()
pyautogui.click()
from time import sleep
sleep(0.5)
elem = driver.find_element_by_id("survey_q1a1").click()
elem = driver.find_element_by_id("survey_q2a1").click()
elem = driver.find_element_by_id("survey_q3a1").click()
elem = driver.find_element_by_id("btnConfirm").click()
