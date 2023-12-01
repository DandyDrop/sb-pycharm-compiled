# from seleniumbase import Driver
#
# driver = Driver(wire=True)
#
# try:
#     driver.get("https://wikipedia.org")
#     print(hasattr(driver, 'requests'))
#
#     print(type(driver))
#     print(vars(driver))
# finally:
#     driver.quit()

from seleniumwire import webdriver


webdriver.Chrome()

