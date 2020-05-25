from selenium import webdriver
import unittest


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
        self.fail('Finish the test!')

    if __name__ == '__main__':
        unittest.main(warnings='ignore')
