import time

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMisArticle:

    def setup_class(self):
        driver = GetDriver.get_driver(page.url_mis)
        #获取统一入口类
        self.page_in = PageIn(driver)

        self.page_in.page_get_PageMisLogin().page_mis_login_article()

        self.article = self.page_in.page_get_PageMisAudit()

    def teardown_class(self):
        time.sleep(3)
        GetDriver.quit_driver()

    def test_mis_article(self, title=page.article_title, channel=page.article_channel):
        self.article.page_mis_audit(title, channel)
        try:
            assert self.article.page_assert_success(title=title,channel=channel)
        except Exception as e:

            log.error(e)

            self.article.base_get_img()
            raise