from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class YoutubeTest(unittest.TestCase):

    def setUp(self):
        pass
        # Method, that will be called before every test_ method in current class

    def test_A(self):
        self.driver = webdriver.Chrome('C:\\Users\\Julia\\Downloads\\chromedriver.exe')
        self.driver.get("http://www.youtube.com")
        elem = self.driver.find_element_by_id("search")
        elem.send_keys("Alabama Shakes Future People")
        #self.driver.find_element_by_id('search-icon-legacy').click()
        elem.send_keys(Keys.ENTER)
        #self.assertIn('alabama+shakes+future+people',self.driver.current_url.lower())
        self.driver.implicitly_wait(500)

        videos = self.driver.find_elements_by_css_selector('#description-text')
        videos[1].click()
        self.driver.implicitly_wait(2000)
        print(self.driver.current_url)
        print(self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
