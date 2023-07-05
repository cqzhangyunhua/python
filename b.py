#coding=utf8
import asyncio
import time
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def main():
    # browser = await launch(headless=False)
    #{'ip': '49.76.41.188', 'port': 4218}
    
    browser=await launch(headless=False, handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False,args=[ "--no-sandbox","--proxy-server=http://49.76.41.188:4218"])
    page = await browser.newPage()
    await stealth(page)  # <-- Here
    await page.setUserAgent("Mozilla/5.0 (Linux; Android 8.1.0; vivo Y71A Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.0.14 (Baidu; P1 8.1.0)")
    # print(page)
    # await page.goto("https://bot.sannysoft.com/")
    url="https://cpu.baidu.com/1080/bd991372?im=rYOdU1kQ5hUHLWrHsNqnrUXgHiTBh7t5DU/3bDjZf5MA5+4H3SGLwL1VVrfgdYI4H8vP+NuUkxR9U+gIX5L7uynpdafiXxnjPg2l9pB+W78WLaXkXdd5wa14oaGoTEcWqlGWeeIBsaxeB12GR0egsYydnxnmguRf7LyTXFFxMbS/KGh/AmKQtW+BxKT1IorHevaWD+1OG0OyUdrsyazyczxRO9+1wrQcyipKAJLwvbvPYzPeRb8x2iG9e+EVuL0m/RIMxpack/wW9XzlUih+A1DTGqXXQuW/6NERHDYcSjaZdPieEHUS0sJgxKw/z5glMay+qR4Mt3punnZYcCKCGQ==&imMd5=YWk2WwjurcHVCsaEH7io4W9/sXjH+3LCMr669/025TuTYudQ566Q/35x68AAVYjyrRJazDxWE7/Id5eaf9staQkV3Pxdg9JhElFDc8dZUcz6hHc70hC7POtZkhuHDABvKcAmbyfdBwO+TZ8WNmIayZQUMBrISdCKQ9VhdEjhnDRgFht//rzBo6FLu+IE4z6WsRGrzw6GyvtQXshSj8DuRCkBQGS4poVX8rLELsRhIEQhA1iIG8ZdLxJWadqLa8lt8/N9YVN0E3750vIb5HsokGI+T+CAvkYkeHNptbfg2CgwJ3jajiPsU9PQkdTkxoGlSkiioC3uzUV/n6rbeGmjZw==&aid=JoQeFKD+IaoLFJuDdcCCMhU7xs5c6oYC3mYcEk0QSy6vvkDek0fBX2OZA+KFDKOcF3LbUlKyhzwN2bH8xPSdxQvRvo4S6skmfdMQTxwLqNJzSu54Aw3ZxdVR1J4l4JgyoxF1Rs2dIBNPVIUMcdidXvgp87SteeFEijNNjz8xkp1ofdAoG7oIhBDK10l0qRVklCu/9BsERIWbpm03zyBOq6Jt2H2jgUO4LovG1kQvXyY6rpxfUFHv2sEQo9I6ZA2MFjJhLOwgUxe2H0hI3ZW/vKQOMXm6s9q3QG7iho/qZt12Te7ntPwfTVINf2RqfUwH/CDTfisE7Tyroi7E/PJ0GA=="
    await page.goto("https://bot.sannysoft.com/")
    t1 = time.time()
    time.sleep(5000)  
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())



# from pyppeteer import launch


# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://top.baidu.com/board?tab=realtime')
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())

