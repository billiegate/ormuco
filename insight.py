
def getGoogleContent(q) :
    url = "https://www.google.com/search?q="+q
    # query the website and return the html to the variable ‘page’
    try : 
        # For Python 3.0 and later
        from urllib.request import urlopen
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen

    page = urlopen(url)
    return page.read()

def init():
    query = input("Enter a search string: ")
    print(getGoogleContent(query))

init()