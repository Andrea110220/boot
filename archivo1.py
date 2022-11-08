from selenium import webdriver
import time

#Precio del Bitcoin con Web Scraping (Python y Selenium)

PATH = 'C:/chrome_webdriver/chromedriver.exe'


driver = webdriver.Chrome(PATH)
#driver = webdriver.Firefox(executable_path="C:/firefox_webdriver/geckodriver.exe")

driver.get("https://www.tdea.edu.co/index.php/valores-de-matricula")

time.sleep(5)


precioTDEA = driver.find_element("xpath",'//*[@id="t3-content"]/div/article/section/h4[6]') 


print('Estudiar en el tdea cuesta : '+ precioTDEA.text)

driver.quit()