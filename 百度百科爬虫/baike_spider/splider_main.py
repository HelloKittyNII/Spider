#coding:utf8
import url_manager
import html_downloader
import html_outputer
import html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser();
        self.outputer = html_outputer.HtmlOutputer()
    pass

    def craw(self, root_url):
        self.urls._add_new_url(root_url)

        count = 1;

        while self.urls.has_new_url():

            try:
                new_url = self.urls.get_new_url()
                print new_url

                #得到url的内容
                html_content = self.downloader.download(new_url)

                #得到url的内容和url
                new_urls,new_data = self.parser.parser(new_url,html_content)

                self.urls.add_new_urls(new_urls)

                self.outputer.collect_data(new_data)
            except:
                print "splider failed"

            if (count == 10):
                break

            count = count + 1;

        self.outputer.outpute_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"

    obj_splider = SpiderMain()
    obj_splider.craw(root_url)