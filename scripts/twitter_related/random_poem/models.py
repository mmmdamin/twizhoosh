import random
import urllib.request

from bs4 import BeautifulSoup

from core.utils.logging import log


class PoemSite():
    TARGET_URL = ""

    def get_poem(self, soup):
        return

    @classmethod
    def get_body_as_soup_object(cls, target_url=""):
        if not target_url:
            target_url = cls.TARGET_URL
        source = urllib.request.urlopen(target_url).read()
        soup = BeautifulSoup(source)
        return soup


class MinisherPoemSite(PoemSite):
    TARGET_URL = "http://minisher.blogfa.com"

    @classmethod
    def get_poem(cls, soup):
        category_list = []
        for item in soup.find_all('a'):
            if isinstance(item.get('href'), str) and item.get('href').startswith('/tag'):
                category_list.append(item)
        post_divs = []

        while not post_divs:
            x = random.randint(0, len(category_list) - 1)
            next_url = "%s%s" % (cls.TARGET_URL, category_list[x].get('href'))
            soup = cls.get_body_as_soup_object(target_url=next_url)
            log("poem post url: {0}".format(next_url))
            # print(soup)

            for item in soup.find_all('div', attrs={'class': 'PostTitle'}):
                if u"شعر کوتاه" in item.text:
                    post_divs.extend(item.find_next_siblings(attrs={'class': 'postbody'}))

        print(post_divs)
        # TODO: extract poem from body of post

        return ""