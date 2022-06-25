from Libs import *

def play():
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


    ### searching and playing funtionallityies getting tested ### 
    search_button = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/nav/div[1]/ul/li[2]/a")
    search_button.click()

    second_button =driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    second_button.send_keys("black norah jones") #search param



    #mouse hover action
    a = ActionChains(driver)
    ele = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[2]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]")
    a.move_to_element(ele).perform()


    #play the expended element
    #/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[2]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/button
    play_button = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[2]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/button")
    play_button.click()
    driver.implicitly_wait(50)