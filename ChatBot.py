from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
message = input('Enter your message')
count =int( input('Enter the count'))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath( '//span [@title = "{}"]').format(name)
user.click ()

message_box = driver.find_element_by_class_name('_2bXVy')

for i in range (count):
    message_box.send_keys(message)
    button = driver.find_element_by_class_name('compose-btn-send')
    button.click()



