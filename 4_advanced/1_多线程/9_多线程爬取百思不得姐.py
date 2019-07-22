#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-03-30  14:26

import requests, threading, time, re
from lxml import etree
from queue import Queue

# url = "http://www.budejie.com/audio/1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
}

proxies = {
    "http": "116.209.56.35:9999"
}


def main():
    q_page = Queue()
    q_audio = Queue()

    pages = int(input("页数？"))

    for page in range(pages):
        url = "http://www.budejie.com/audio/{}".format(str(page+1))
        q_page.put(url)
        # GetPage(url, q_page, q_audio).start()

    for i in range(10):
        GetPage(q_page, q_audio).start()
        # break
    for i in range(10):
        DownloadAudio(q_page, q_audio).start()


class GetPage(threading.Thread):
    """生产者"""
    def __init__(self, q_page, q_audio, *args, **kwargs):
        super(GetPage, self).__init__(*args, **kwargs)
        self.q_page = q_page
        self.q_audio = q_audio

    def run(self):

        while True:
            self.get_page()
            if not self.q_page.empty():
                break
            time.sleep(1)

    def get_page(self):
        url = self.q_page.get()
        html = requests.get(url=url, headers=headers, timeout=3).content.decode('utf-8')
        eles = etree.HTML(html)

        # titles = eles.xpath("//div[@class='j-r-list-c-desc']/text()")
        audio_url = eles.xpath("//a[@class='ipad-down-href']/@href")

        for i in audio_url:
            self.q_audio.put(i)
            # print(i)

class DownloadAudio(threading.Thread):
    """消费者"""
    def __init__(self, q_page, q_audio, *args, **kwargs):
        super(DownloadAudio, self).__init__(*args, **kwargs)
        self.q_page = q_page
        self.q_audio = q_audio

    def run(self):
        while True:
            try:
                audio_url = self.q_audio.get()
                self.download_audio(audio_url)
                time.sleep(1)
            except:
                continue
            if self.q_audio.qsize == 0 and self.q_page.qsize == 0:
                break

    def download_audio(self, audio_url):
        audio = requests.get(audio_url, timeout=3)
        # filename = re.sub(re.compile("？"), "", title)
        filename = time.time()
        print(audio_url,">>> 正在下载！")
        with open("audio/{}.mp3".format(filename), "wb") as fp:
            fp.write(audio.content)
        print(audio_url, "<<< 下载完成！")

if __name__ == '__main__':
    main()

