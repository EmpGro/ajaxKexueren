import requests
import json
##import pprint

'''
获得的是json数据
先用json.loads将json数据python化
采用pprint格式化输出数据便于分析
然后根据数据结构获取想要的内容
'''


def get_page(url):
    '''获取页面'''
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Host': 'www.guokr.com',
        'Referer': 'http://www.guokr.com/scientific/'
    }

    return requests.get(url, headers=headers)


def get_datas(offset):
    '''从页面中获取数据'''
    items = {}
    url = 'http://www.guokr.com/apis/minisite/article.json?retrieve_type=by_subject&limit=1&offset=' + str(offset) + '&_=1508134471173'
    html = get_page(url)
    #datas = json.loads(html.text)
    #pprint.pprint(datas['result'])
    datas = json.loads(html.text)['result'][0]
    items['type'] = datas['author']['nickname']
    items['keyword'] = datas['subject']['name']
    items['title'] = datas['title']
    items['summary'] = datas['summary']
    #pprint.pprint(items)
    with open('result.txt', 'a',  encoding='utf-8') as fo:
        fo.write(str(items)+'\n')


def main():
    for offset in range(0, 60):
        get_datas(offset)


if __name__ == '__main__':
    main()