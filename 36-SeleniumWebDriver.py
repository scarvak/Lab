from selenium import webdriver
# from selenium.webdriver.common.by import By

myD1 = webdriver.Chrome()
myD2 = webdriver.Firefox()

myD1.get("https://itelearn.com/")
myD2.get("https://anyaut.com/")
