
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

import nltk
import benepar

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 3
SENTENCE_LIMIT = 20

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(url, body):
    soup = BeautifulSoup(body, 'html.parser')
    if "github.com" in url:
            soup = soup.find("div", {"id": "readme"})
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return [t.strip() for t in visible_texts]

def extract_vp(parent):
    for node in parent:
        if type(node) is nltk.Tree:
            label = node.label()
            if label == "VP":
                surface = " ".join(node.leaves())
                return surface

if __name__ == "__main__":
    syntactic_parser = benepar.Parser("benepar_en2")

    #for lib, category, url in dataset:
    results = []
    with open("dataset.txt") as target:
        for line in target:
            try:  
                app, url = line.strip().split("\t")
                html = urllib.request.urlopen(url).read()
                raw_sequences = text_from_html(url, html)
                raw_sequences = [seq for seq in raw_sequences if seq and len(seq.split()) > 3]
                raw_sequences = raw_sequences[:SENTENCE_LIMIT]
                passage = ""
                for seq in raw_sequences:
                    passage += seq
                    if seq[-1] not in ["!", ".", "?"]:
                        passage += ". "
                    else:
                        passage += " "

                parser = PlaintextParser.from_string(passage, Tokenizer(LANGUAGE))
                stemmer = Stemmer(LANGUAGE)

                summarizer = Summarizer(stemmer)
                summarizer.stop_words = get_stop_words(LANGUAGE)

                sentences = str(list(summarizer(parser.document, SENTENCES_COUNT)))
                results.append([app, url, sentences])
                #tree = syntactic_parser.parse(sentence)
                #vp = extract_vp(tree)
                #results.append([app, vp, sentence, passage])
            except Exception:
                print(app, url)


        
    import pandas as pd
    df = pd.DataFrame(results, columns=["ThirdParty", "URL", "SENTENCES"])                                                                                                                                                    
    df.to_csv('list.csv', index=False)  
