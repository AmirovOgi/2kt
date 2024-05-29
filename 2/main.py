from conftest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def test_1(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "MacBook"))).click()
    
    link = "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link))).click()
    ActionChains(driver).send_keys(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).perform()

def test_2(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "MacBook"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-cart"))).click()

def test_3(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Компьютеры"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "PC (0)"))).click()


def test_4(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Личный кабинет')]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Регистрация"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-firstname"))).send_keys("Name")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-lastname"))).send_keys("Surname")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-email"))).send_keys("example@mail.ru")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-telephone"))).send_keys("89990001111")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-password"))).send_keys("qWeRty")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-confirm"))).send_keys("qWeRty")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]"))).click()

def test_5(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/div[1]/div[1]/div[2]/div[1]/input[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/div[1]/div[1]/div[2]/div[1]/input[1]"))).send_keys("text")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]"))).click()
