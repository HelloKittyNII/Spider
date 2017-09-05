# coding:utf-8
import urlparse

from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def parser(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        links = soup.find_all('a', href=re.compile(r'/article/'))

        for link in links:
            new_url = link["href"]
            new_url_full = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_url_full)

        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # <div class="lemma-summary" label-module="lemmaSummary">
        content = soup.find("div", class_="content")
        res_data['content'] = content.get_text()

        print content

        return res_data