from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("Red")
elem.send_keys(Keys.ENTER)

#~~스크롤 내리기
SCROLL_PAUSE_TIME = 0.1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            elem = driver.find_elements_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height
    #~~
image = elem = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
cnt = 1
for image in image:
    try:
        time.sleep(2)
        imgUrl = elem = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, str(cnt) + ".jpg")
        cnt = cnt + 1
    except:
        pass

driver.close()