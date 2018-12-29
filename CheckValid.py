from urllib import request
import GetLinks
import urllib
import time


def send_request(links):
    valid_links = 0
    error_links = 0
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    dead_links = []
    # req = urllib.request.Request(url=link, headers=headers)
    # return urllib.request.urlopen(req).reason
    for link in links:
        # with request.urlopen(link) as file:
        #     if file.reason == 'OK':
        #         valid_links += 1
        #     else:
        #         error_links += 1
        try:
            req = urllib.request.Request(url=link, headers=headers)
            if urllib.request.urlopen(req).reason == 'OK':
                valid_links += 1
            else:
                error_links += 1
                dead_links.append(link)

        except Exception:
            error_links += 1
            dead_links.append(link)
        print(valid_links)
        time.sleep(0.1)
    return valid_links, error_links, dead_links


if __name__ == '__main__':
    links = GetLinks.getlink('http://blog.csdn.net/')

    links = [w[0] for w in links]
    print('sum of links is :', len(links))
    valid_links, error_links, dead_links = send_request(links)
    # for link in links:
    #     if send_request(link) == "OK":
    #         valid_links += 1
    #     else:
    #         error_links += 1
    #     print(valid_links)
    #     time.sleep(1)
    print(valid_links, '   ', error_links)
    for item in dead_links:
        print(item)

