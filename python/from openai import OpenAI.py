#from openai import OpenAI

# 記得key不要洩漏出去
#api_key = 'sk-proj-Cvd0skppF7FuIHR7msjLT3BlbkFJQATKIg6XwcfQGiZYmnug'
#client = OpenAI(api_key = api_key)
#completion = client.chat.completions.create(
 # model="gpt-3.5-turbo",
  #messages=[
   # {"role": "assistant", "content": "你是一個專業的AI教學顧問，請根據問題使用繁體中文回覆"},
    #{"role": "user", "content": "我想學習deep learning要從哪邊開始入手"}
  #]
#)

#print(completion.choices[0].message)
#conversation_history = [
 #   {"role": "assistant", "content": "你是一個專業的AI教學顧問，請根據問題使用繁體中文回覆"},
  #  {"role": "user", "content": "我想學習deep learning要從哪邊開始入手"}
#]

# 新的提問
#new_user_input = "請問有推薦的入門書籍或資源嗎？"

# 將新提問加到對話歷史
#conversation_history.append({"role": "user", "content": new_user_input})

# 呼叫API，發送完整的對話歷史
#completion = client.chat.completions.create(
 # model="gpt-3.5-turbo",
  #messages=conversation_history
#)

# 回答並將再加入到對話歷史中
#new_answer = completion.choices[0].message
#print(new_answer)
#import requests 
#from bs4 import BeautifulSoup

from selenium import webdriver
driver=webdriver.Chrome('')  #改版後，保持 ''
url='https://www.google.com'
driver.get(url)

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#=======
driver=webdriver.Chrome('')
url='https://www.google.com'
driver.get(url)
#name="q"

search_box=driver.find_element(By.NAME,'q')
search_box.send_keys('好喝咖啡')
search_box.send_keys(Keys.RETURN)

#等待時間
time.sleep(5)


#url = "https://www.ptt.cc/bbs/index.html"#網站????
#我們要假裝自己是Google機器人才不會被伺服器擋掉
#headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
#res = requests.get(url, headers = headers)
#同時我們需要使用一個叫做html.parser的HTML解析器來讀取HTML
#soup = BeautifulSoup(res.text,"html.parser")
#articles = soup.find_all("div", class_= "b-ent")

#for i in articles:
 #   title = i.find("div", class_ = "board-class")
  #  nuser = i.find("div", class_ = "board-nuser")
   #
   #  print("看板名稱:" + title.text , "  " , "點擊率:" , nuser.text)
