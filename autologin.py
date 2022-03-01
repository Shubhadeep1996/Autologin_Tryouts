import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

email = input('email: ')
password = input('Password: ')

indriver = webdriver.Chrome("chromedriver")

indriver.get("https://www.facebook.com/login")

indriver.find_element_by_id("email").send_keys(email)
indriver.find_element_by_id("pass").send_keys(password)
indriver.find_element_by_name("login").click()

WebDriverWait(driver = indriver, timeout = 10).until(lambda drv: drv.execute_script("return document.readyState == 'complete'"))

errormessage = "The password that you've entered is incorrect."

errormessage1 = "The email address or mobile number you entered isn't connected to an account."

errors = indriver.find_elements_by_class_name("_9ay7")

if any(errormessage in e.text for e in errors):
    print("[!] Login Failed")
elif any(errormessage1 in e.text for e in errors):
    print("[!] Login Failed")
else:
    print("[+] Login Successfully")