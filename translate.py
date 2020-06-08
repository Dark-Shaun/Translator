import googletrans
from googletrans import Translator

m=googletrans.LANGUAGES

def swap(m):
    m1={v:k for k,v in m.items()}
    return m1

def detect(text):
    translator = Translator()
    k=translator.detect(text)
    j=k.lang
    lng_detect=m[j]
    return lng_detect,j

def translate(text,a,b):
    translator=Translator()
    trans=translator.translate(text,src=a,dest=b)
    trans_1=trans.text
    return trans_1
