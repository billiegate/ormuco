# gets a resource via HTTP GET
def getGoogleContent(q) :
    url = "http://www.google.com/search?q="+q
    import requests
    req = requests.request('GET', url)
    return req.content

# parse and read the needed results
def parseRes(cont) :
    import bs4 as bs
    souped = bs.BeautifulSoup(cont, 'html.parser')
    # print(souped.prettify())
    res = list()
    suggestions = souped.find_all('div', class_='ZINbbc')
    for suggestion in suggestions :
        url = suggestion.find_all('a')[0].get('href')
        insight = [x.text for x in suggestion.find_all('div', class_='s3v9rd')]
        if(len(insight) > 0 and len(res) < 5):
            _res = {
                "href": url,
                "insight": insight[0]
            }
            res.append(_res)
    return res

def init():
    inp = input("Enter a search string: ")
    cont = getGoogleContent(inp)
    res = parseRes(cont)  
    print(res)

init()

# USEAGE - cd via terminal to the folder where this file is placed. 
# run `python afolabi_tope_insight.py`
# 00703232849040