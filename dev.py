from selenium import webdriver
from time import sleep

class Insta:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.maximize_window()
    
    def login(self):
        self.driver.get('https://www.instagram.com')

        sleep(1)
        user = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys('M5_believe')
        passd = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        passd.send_keys('D3adp00l')
        lgbn = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button')
        lgbn.click()

        sleep(2)
        notnw = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        notnw.click()

        sleep(2)

        notnw1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        notnw1.click()

    def follow(self):
        seeall = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a/div')
        seeall.click()

        for n in range(1, 50):
            nml = '//*[@id="react-root"]/section/main/div/div[2]/div/div/div[' + str(n) + ']/div[3]/button'
            follow = self.driver.find_element_by_xpath(nml)
            follow.click()


i = Insta()

i.login()
#i.follow()
