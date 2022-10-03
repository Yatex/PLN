from pysentimiento import SentimentAnalyzer
from langdetect import detect, DetectorFactory

def analyzeSentiment(text):
    DetectorFactory.seed = 0
    language = detect(text)
    if language != 'es':
        language = 'en'
    analyzer = SentimentAnalyzer(lang=language)
    result = analyzer.predict(text)
    return result.output
    return None