# shimzukawa-02
import urllib.request
from urllib.parse import urljoin  # URLを扱うモジュールを追加
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site
        self.urls = set()  # 収集済みURLを入れておく変数

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = 'html.parser'
        soup = BeautifulSoup(html, parser)
        with open("output.txt", "w") as f:
            for tag in soup.find_all('a'):
                url = tag.get('href')
                if url is None:
                    continue
                if 'atcl/contents' not in url:  # 'atcl/contents' を含まないURLは対象外にする
                    continue
                full_url = urljoin(response.url, url)  # ドメイン名を含むURLに変換
                if full_url in self.urls:  # 既に収集済みのURLは対象外にする
                    continue
                self.urls.add(full_url)  # 収集済みURLに追加
                print('\n' + full_url)  # URLを表示
                f.write(url + "\n")


news = 'https://xtrend.nikkei.com/atcl/contents/new/'  # ニュース取得元サイトを変更
Scraper(news).scrape()