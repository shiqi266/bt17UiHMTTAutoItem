import time

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    # 选择状态ul->li
    def web_base_click_ul_li(self, placeholder_text, click_text):
        # 组合placeholder 文本信息定位元素信息
        loc = By.XPATH, "//*[@placeholder='{}']".format(placeholder_text)

        # 查找元素并点击
        self.base_click(loc)
        time.sleep(2)
        # 定位ul->列表
        loc = By.CSS_SELECTOR, "ul>li"
        # 遍历text 内容等于 click_text 条件成立click()
        for i in self.base_finds(loc):
            if i.text == click_text:
                i.click()
                break

    # 判断元素是否存在
    def web_base_element_exists(self,text):
        loc = By.XPATH,"//*[contains(text(),'{}')]".format(text)
        try:
            self.base_find(loc,timeout=3)
            print("找到元素了")
            return True  #说明元素页面存在元素
        except:
            print('没有找到元素')
            return False  #页面不存在元素

