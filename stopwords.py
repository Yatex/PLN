from dis import show_code
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from langdetect import detect, DetectorFactory

# Previous steps
DetectorFactory.seed = 0
nltk.download('stopwords')
nltk.download('punkt')

stopwords_es = set(stopwords.words('spanish'))
stopwords_en = set(stopwords.words('english'))

def give_stopwords_en():
    return add_extra_signs(stopwords_en)

def give_stopwords_es():
    return add_extra_signs(stopwords_es)

def remove_stop_words(text):
    print(text)
    language = detect(text)
    if language == 'es':
        stopwords_language = stopwords_es
    else:
        stopwords_language = stopwords_en
    stopwords_language = add_extra_signs(stopwords_language)
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stopwords_language]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stopwords_language:
            filtered_sentence.append(w)
    return filtered_sentence

def add_extra_signs(stopwords_language):
    stopwords_language.add('.')
    stopwords_language.add('\'')
    stopwords_language.add('\n')
    stopwords_language.add('!')
    stopwords_language.add('..')
    stopwords_language.add('...')
    stopwords_language.add('(')
    stopwords_language.add(')')
    stopwords_language.add(',')
    stopwords_language.add('Translated')
    stopwords_language.add('Google')
    stopwords_language.add('Original')
    return stopwords_language