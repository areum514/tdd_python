from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# test


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/armarm/Documents/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_ans_retrieve_it_later(self):
        # 아름이는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹사이트를 방문한다.
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_elemnet_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업아이템입력'
        )

        inputbox.send_key('공작 깃털 사기')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기 'for row in rows),
        )

        self.fail('Finish the test!')

    if __name__ == '__main__':
        unittest.main(warnings='ignore')
