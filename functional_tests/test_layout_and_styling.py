# _*_ coding: utf-8 _*_
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # 에디스는 메인 페이지를 방문한다.
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        # 그녀는 입력 상자가 가운데 배치된 것을 본다
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEquals(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=10
        )
        
        # 그녀는 새로운 리스트를 시작하고 입력 상자가
        # 가운데 배치된 것을 확인한다
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEquals(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=10
        )

