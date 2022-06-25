
from Libs import *
    
def LogInOut():
    # create webdriver object
    profile = webdriver.FirefoxProfile('/home/ellenfel/.mozilla/firefox/4bcejejs.4testing')
    driver = webdriver.Firefox(profile)
    # get url
    driver.get("https://open.spotify.com")

    ### logging-in ###
    login_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]")
    login_button.click()

    driver.implicitly_wait(10)

    username_field = driver.find_element_by_id("login-username")
    username_field.clear()
    username_field.sengitd_keys(username)

    password_field = driver.find_element_by_id("login-password")
    password_field.clear()
    password_field.send_keys(password)

    driver.find_element_by_id("login-button").send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    
    #def LogOut():
    ### log-out ###
    pp = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/button")
    pp.click()

    #/html/body/div[4]/div/div[2]/div[1]/header/div[5]/div/div/ul/li[4]/button
    logout = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/div[5]/div/div/ul/li[4]/button")
    logout.click()
