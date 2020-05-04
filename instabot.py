from selenium import webdriver
from time import sleep


class Insta:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://www.instagram.com/')

        sleep(3)

        user = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        user.send_keys('username')

        passd = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        passd.send_keys('password')

        lgbn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
        lgbn.click()

        sleep(3)

        notnw = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notnw.click()

    def follow(self):
        hm = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')

        hm.click()
        sleep(1)
        sugges = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/section/div[3]/div[3]/div[1]/a')
        sugges.click()

        sleep(3)

        for n in range(1, 1000):
            nml = '//*[@id="react-root"]/section/main/div/div[2]/div/div/div[' + str(n) + ']/div[3]/button'

            follow = self.driver.find_element_by_xpath(nml)
            follow.click()

    def likes(self):

        hm = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')

        hm.click()

        sleep(3)

        for n in range(1, 1000):

            try:
                nm = '//*[@id="react-root"]/section/main/section/div[1]/div[1]/div/article[' + str(
                    n) + ']/div[2]/section[1]/span[1]/button'

                follow = self.driver.find_element_by_xpath(nm)
                follow.click()
            except:
                pass

    def profilefollw(self):

        pf = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]')
        pf.click()

        sleep(3)

        pfc = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        pfc.click()

        sleep(3)

        test = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = i.driver.execute_script(
                'arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', test)

        fasi = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')

        links = fasi.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        blinks = fasi.find_elements_by_tag_name('button')

        bnames = [name.text for name in blinks if name.text != '']

        z = zip(names, bnames)

        def test123():
            inn = 1
            forz = list(z)
            for a, b in forz:
                if b != 'Following':
                    if b != 'Requested':
                        zn = '/html/body/div[4]/div/div[2]/ul/div/li[' + str(inn) + ']/div/div[2]/button'
                        followclick12 = self.driver.find_element_by_xpath(zn)
                        followclick12.click()
                        f = tuple((a, b))
                        print(f)

                inn += 1

        test123()
        clse = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')
        clse.click()



i = Insta()

i.login()



try:
    i.profilefollw()
except:
    pass


sleep(3)
try:
    i.follow()
except:
    pass

sleep(3)

i.likes()



