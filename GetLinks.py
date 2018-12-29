import re
import urllib.request


def getlink(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url).read()
    file = file.decode('utf-8')
    pattern = '(https?://[^\s)";]+(\.(\w|/)*))'
    links = re.compile(pattern).findall(file)
    # 去重
    links = list(set(links))
    # links = [w[0] for w in links]
    # valid_links = 0
    # error_links = 0
    #
    # for link in links:
    #     with urllib.request.urlopen(link) as file:
    #         if file.reason == 'OK':
    #             valid_links += 1
    #         else:
    #             error_links += 1
    # return valid_links, error_links
    return links

# url = "http://blog.csdn.net/"
# linklist = getlink(url)
# # print(v, '    ', e)
# for link in linklist:
#     print(link[0])
# print(len(linklist))
# getlink()