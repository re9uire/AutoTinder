from selenium import webdriver
import time
import random

driver = webdriver.Chrome(r"Driverパス")
driver.get("https://tinder.com/")
driver.implicitly_wait(1) # 秒

login_button = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()
time.sleep(5)

login_button_facebook = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_button_facebook.click()
time.sleep(5)

# windowを切り替える
handle_array = driver.window_handles
driver.switch_to.window(handle_array[1])

# アドレス入力フォームのxpath取得
mail_form = driver.find_element_by_xpath('//*[@id="email"]')

# 入力
mail_form.send_keys("facebookメアド")

# パスワード入力フォームのxpath取得
pass_form = driver.find_element_by_xpath('//*[@id="pass"]')

# 入力
pass_form.send_keys("facebookパスワード")

# # ログインボタンのxpath取得
login_button = driver.find_element_by_xpath(r"/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")

# ログインボタンクリック
login_button.click()

# windowの切り替え
handle_array = driver.window_handles
print(handle_array)
driver.switch_to.window(handle_array[0])

popup_button2 = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[2]/div/div/div[1]/button')
popup_button2.click()
time.sleep(5)

popup_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
popup_button.click()
time.sleep(5)

popup_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
popup_button.click()

while True:
   # 0-1の乱数を生成
   random_num = random.random()
   try:
       if (random_num <= 0.85):
           like_button = driver.find_element_by_xpath(
               r"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button")
           like_button.click()
           time.sleep(2)
       else:
           dislike_button = driver.find_element_by_xpath(
               r'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
           dislike_button.click()
           time.sleep(2)
   except:
       try:
           not_intersted_button = driver.find_element_by_xpath(
             r'/html/body/div[2]/div/div/div[2]/button[2]')
           not_intersted_button.click()
           time.sleep(2)
       except:
           not_intersted_button = driver.find_element_by_xpath(
             r'//*[@id="t--1700653258"]/div/div/button[2]')
           not_intersted_button.click()
           time.sleep(2)
   time.sleep(2)