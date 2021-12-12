import hashlib
import time
import requests


def qianqianMusic():
    # 千千音乐获取歌曲详情（包含曲目直链，vip为试听），使用了md5加密
    time1 = int(time.time())
    r = f"TSID=T10052829768&appid=16073360&timestamp={time1}" + '0b50b02fd0d73a9c4c8c3a781c30845f'
    byte_row = r.encode('utf-8', 'ignore')
    md5 = hashlib.md5()
    md5.update(byte_row)
    sign = md5.hexdigest()

    url = f'https://music.taihe.com/v1/song/tracklink?sign={sign}&appid=16073360&TSID=T10052829768&timestamp={time1}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'
    }
    response = requests.get(url, headers=headers).json()
    print(response)


if __name__ == '__main__':
    qianqianMusic()
