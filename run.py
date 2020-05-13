from selenium import webdriver
import time

name = 'Hirza Nazhari'
email = 'aaa@ggg.com'
tel = '1111111111'
address = 'adress'
zip = 'zip'
city = 'city'
number = 'card number'
cvv = 'cvv'


chromedriver_location = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2")

add_to_cart_button = '//*[@id="add-remove-buttons"]/input'
driver.find_element_by_xpath(add_to_cart_button).click()

checkout_button = '//*[@id="cart"]/a[2]'
driver.find_element_by_xpath(checkout_button).click()

name_xpath = '//*[@id="order_billing_name"]'
driver.find_element_by_xpath(name_xpath).send_keys(name)

email_xpath = '//*[@id="order_email"]'
driver.find_element_by_xpath(email_xpath).send_keys(email)

tel_xpath = '//*[@id="order_tel"]'
driver.find_element_by_xpath(tel_xpath).send_keys(tel)

adress_xpath = '//*[@id="bo"]'
driver.find_element_by_xpath(adress_xpath).send_keys(adress)

zip_xpath = '//*[@id="order_billing_zip"]'
driver.find_element_by_xpath(zip_xpath).send_keys(zip)

city_xpath = '//*[@id="order_billing_city"]'
driver.find_element_by_xpath(city_xpath).send_keys(city)

state_xpath = '//*[@id="order_billing_state"]/option[56]'
driver.find_element_by_xpath(state_xpath).click()

number_xpath = '//*[@id="rnsnckrn"]'
driver.find_element_by_xpath(number_xpath).send_keys(number)

card_month_xpath = '//*[@id="credit_card_month"]/option[1]'
driver.find_element_by_xpath(card_month_xpath).click()

card_year_xpath = '//*[@id="credit_card_year"]/option[1]'
driver.find_element_by_xpath(card_year_xpath).click()

cvv_xpath = '//*[@id="orcer"]'
driver.find_element_by_xpath(cvv_xpath).send_keys(cvv)

i_agree_xpath = '//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins'
driver.find_element_by_xpath(i_agree_xpath).click()

process_payment_xpath = '//*[@id="pay"]/input'
driver.find_element_by_xpath(process_payment_xpath).click()

print("Web Driver Run")