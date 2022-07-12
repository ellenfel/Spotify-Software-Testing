from Libs import *

def Settings():
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
    username_field.send_keys(username)

    password_field = driver.find_element_by_id("login-password")
    password_field.clear()
    password_field.send_keys(password)

    driver.find_element_by_id("login-button").send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    ### locating account page ###
    #/html/body/div[4]/div/div[2]/div[1]/header/button
    pp = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/button")
    pp.click()
    driver.implicitly_wait(10)

    account = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/div[5]/div/div/ul/li[1]/button")
    account.click()

    #prints the window handle in focus
    print(driver.current_window_handle)
    #to fetch the first child window handle
    chwnd = driver.window_handles[1]
    #to switch focus the first child window handle
    driver.switch_to.window(chwnd)

    driver.implicitly_wait(500)

    makbuz = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div/ul/li[8]/a")
    makbuz.click()

    makbuz_last = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[4]")
    makbuz_last.click()

    driver.close() #closes the browser
    print("receipts and settings funcs tested successfully")
    driver.quit()