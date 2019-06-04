import unittest
from time import sleep

from selenium import webdriver


class TestBaidu(unittest.TestCase):
    chrome_driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/renzongyi/PycharmProjects/AutoTestPlatform/storage/drivers/mac/chromedriver")
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(10)
        sleep(2)
        self.driver.find_element_by_id("wrapper")

    def test_search(self):
        input_box = self.driver.find_element_by_id("kw")
        input_box.send_keys("JJ游戏")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        results = self.driver.find_elements_by_class_name("c-abstract")
        text_of_first_result = results[0].text
        assert (str(text_of_first_result).lstrip().startswith("jj")), "验证失败！"

    def test_open_post(self):
        """打开贴吧测试"""
        post_element = self.driver.find_element_by_link_text("贴吧")
        post_element.click()
        self.driver.find_element_by_class_name("j_search_post")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestBaidu)
    runner = unittest.TextTestRunner()
    runner.run(suit)
