from selenium import webdriver
import time

#Precio del Bitcoin con Web Scraping (Python y Selenium)

PATH = 'C:/chromedriver/chromedriver.exe'


driver = webdriver.Chrome(PATH)
#driver = webdriver.Firefox(executable_path="C:/firefox_webdriver/geckodriver.exe")

driver.get("https://www.google.com/finance/quote/USD-COP?sa=X&ved=2ahUKEwisroD-2pL7AhVETDABHffXDBEQmY0JegQIBhAc")

time.sleep(5)


precioDolar = driver.find_element("xpath",'//*[@id="yDmH0d"]/c-wiz/div/div[4]/div/main/div[2]/div[1]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div') 


print('El precio del dolar es : '+ precioDolar.text)

driver.quit()