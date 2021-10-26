# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://reading.pen.go.kr/r/newReading/main/main.jsp")
elem = driver.find_element_by_id("btn_menu_mobile").click()
import pyautogui
pyautogui.moveTo(940,300)
pyautogui.click()
pyautogui.click()
elem = driver.find_element_by_id("s_id")
elem.send_keys("moofa7699")
elem = driver.find_element_by_id("s_pwd")
elem.send_keys("sun010521!")
elem = driver.find_element_by_id("s_login").click()
elem = driver.find_element_by_id("btn_menu_mobile").click()
time.sleep(1)
pyautogui.moveTo(1200,500)
pyautogui.click()
pyautogui.click()
time.sleep(0.5)
# elem = driver.find_element_by_id("bookName")
# elem.send_keys("초격차")
# elem = driver.find_element_by_id("publisherName")
# elem.send_keys("쌤앤파커스")
# elem = driver.find_element_by_id("searchBtn").click()
# time.sleep(4)
# elem = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div/div[3]/div[1]/form/div/div/div[2]/div[2]/ul/li/div[2]/a/span").click()
elem = driver.find_element_by_id("title")
elem.send_keys("‘초격차’을 읽고")
pyautogui.moveTo(1100,900)
pyautogui.click()
pyautogui.click()
elem = driver.execute_script("window.scrollTo(0, 500)")
elem = driver.find_element_by_class_name("write_content")
elem.send_keys("우리나라 기업 1등 삼성 그 중 삼성전자의 전 회장이신 권오현 전 회장님의 서적이다. 처음에는 책 소개하는 영상을 보고 이 책을 읽고 싶었지만 책의 내용을 보면서 훨씬 더 읽고 싶은 마음이 강했다. 처음 삼성은 반도체 사업에 후발주자로 시장에 뛰어들었다. 그리고 권오현 전 회장님은 그런 반도체 사업을 맡았다. 그리고 두 가지의 구호를 가지고 평생을 살았고 아직도 신조로 굳건히 자리 잡고 있다고 한다. 1. 안 된다는 생각을 버려라. 2. 큰 목표를 가져라.  구호에도 힘이 있고 부정적인 생각을 버리고 큰 목표를 가지고 그 목표를 향해 노력을 한다면 성장할 수 있다고 한다. 리더의 기질은 선천적인 것이 아니라 청소년기에 형성된다고 한다. 진솔함, 겸손, 무사욕은 내적 덕목이고 통찰력, 결단력, 실행력, 지속력은 외적인 덕목이라고 한다. 하나가 아니라 모두 갖추어야 한다. 그리고 리더는 뇌가 되어야 한다고 한다. 그리고 리더의 유형은 4 가지가 있고 그 유형들을 역사와 연관을 지어 설명해 주었다. 최고의 리더는 차별화된 가치를 창출하는 사람이다. 생존과 성장을 넘어 사회에 기여해야 하고 리더가 교체가 되어도 가치가 더 큰 원동력이 될 수 있어야 한다. 그리고 최악의 리더는 미래를 망치는 리더이다. 지금의 성과에 매여 본인이 물러난 후 어려움을 발생시킨다. 그것은 심각한 실패라고 했다. 변화하는 방법은 하지않아도 될 일을 정하는 것이다. 마음을 동기부여 하면서 해야할 일을 정할 것이 아닌 하지않아도 될 일을 정하면 더 무엇을 해야할지 어떻게 시관 관리를 할지 알 수 있다고 하였다. 의사결정을 할 때에는 개방적인 자세를 유지하고 여유를 가지자고 하였다. 주변의 의견을 경청하는 자세를 유지하고 신체적, 금전적, 시간적 여유가 있어야 올바른 결정을 할 수 있다고 한다. 무언가에 쫒기면 시야가 좁아지기 때문이다. 현재의 이익을 극대화 시킬 것인가, 미래를 성장시킬 것인가 이것이 리더들의 고민이라고 했다. 그리고 저자는 “현재의 호황 국면에 현혹되지 말고 미래의 위험을 무릅쓰라는 것입니다.”를 강조했다. 나는 이 책을 읽고 정말 많은 것을 배웠다. 내 마음이 조급해서 이제껏 보지 못했던 것들이 많고 해야할 일을 몰라서 무엇을 해야할지 몰랐던 날 방황에서 조금 벗어나게 해 주었다. 나도 지금 현재를 즐길 것이 아니라 미래에 더 즐길 수 있도록 노력하고 싶다. 그리고 내가 없는 겸손함에 대해 이 책은 매우 잘 날 꾸짖었다. 겸손함이 중요한 것인 걸 알면서 잘 하지 못했던 날 반성했다. ")
