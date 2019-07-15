import bs4 as bs
from nltk.corpus import stopwords
import requests
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

# gets a resource via HTTP GET
def getContent(url) :
    req = requests.request('GET', url)
    return req.content

# parse and read the needed results
def parseGRes(cont) :
    souped = bs.BeautifulSoup(cont, 'html.parser')
    # print(souped.prettify())
    res = list()
    suggestions = souped.find_all('div', class_='ZINbbc')
    for suggestion in suggestions :
        url = suggestion.find_all('a')[0].get('href')
        insight = [x.text for x in suggestion.find_all('div', class_='s3v9rd')]
        if(len(insight) > 0 and len(res) < 5):
            _res = {
                "href": url.split('?q=')[1],
                "insight": insight[0]
            }
            res.append(_res)
    return res

def analyseData(obj):
    stop = stopwords.words('english')
    content_list = list()
    for search in obj :
        content_dict = {}
        cont = getContent(search['href'])
        souped = bs.BeautifulSoup(cont, 'html.parser')
        content_dict['title'] = souped.title.text
        content_dict['content'] = souped.body.text
        obj[search]['summary'] = generate_summary(content_dict['content'].split("."))
    return obj

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
    all_words = list(set(sent1 + sent2))
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for col in range(len(sentences)):
        for row in range(len(sentences)):
            if col == row: #ignore if both are same sentences
                continue 
            similarity_matrix[col][row] = sentence_similarity(sentences[col], sentences[row], stop_words)
    return similarity_matrix

def generate_summary(sentences, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []
    # Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    # Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)
    # Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    # print("Indexes of top ranked_sentence order are ", ranked_sentence)
    for i in range(top_n):
      summarize_text.append(" ".join(ranked_sentence[i][1]))
    # Output the summarize texr
    return ". ".join(summarize_text)

def init():
    inp = input("Enter a search string: ")
    url = "http://www.google.com/search?q="+inp
    cont = getContent(url)
    _res = parseGRes(cont)
    res = analyseData(_res)
    print(res)

if __name__ == '__main__':
    init()

# USEAGE - cd via terminal to the folder where this file is placed. 
# run `python afolabi_tope_insight.py`
# 00703232849040