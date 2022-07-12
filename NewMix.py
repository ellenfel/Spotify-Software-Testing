from Libs import *

def Mix():
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


    ### Create a new mix ###
    newMix_button = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/nav/div[1]/div[2]/div/div[1]/button")
    newMix_button.click()
    driver.implicitly_wait(50)

    search_field = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/section/div/div/input")
    search_field.clear()
    search_field.send_keys("Selenium")

    add_button = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/button")
    add_button.click()
    driver.implicitly_wait(50)

    source = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/nav/div[1]/div[2]/div/div[5]/div[4]/div/div/ul/div/div[2]/div[1]")
    #action chain object
    action = ActionChains(driver)
    action.context_click(source).perform()

    del_button = driver.find_element_by_xpath("/html/body/div[15]/div/ul/li[5]/button")
    del_button.click()

    del_conformation = driver.find_element_by_xpath("/html/body/div[18]/div/div/div/div/button[2]")
    del_conformation.click()

    driver.implicitly_wait(50)

    driver.close() #closes the browser
    print("Creating a new Mix, adding a song & deleting it tested successfully")
    driver.quit()