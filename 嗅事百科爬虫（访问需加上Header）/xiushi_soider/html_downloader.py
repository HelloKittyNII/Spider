#coding utf8

import urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None


        try:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}
            req = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(req);
        except Exception, e:
            print e

        if response.getcode == 200:
            return None

        return response.read()
