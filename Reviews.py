import math
import pandas as pd
from stopwords import remove_stop_words, give_stopwords_es, give_stopwords_en
from wordclouds import wordcloud
from sentimentAnalysis import analyzeSentiment

# Variables a utilizar a futuro
dict_reviews_rating = []
total_text_review = []
comment_text = ''
data_resto = pd.read_excel('LaPalitaReviews.xlsx')
sentiments = {'NEG': 0, 'NEU': 0, 'POS': 0}

# rellena los NaN con vacio
data_resto.fillna('', inplace=True)

# Guardo los datos que quiero en un array de diccionarios, donde el primer campo es review y el segundo es rating de esa review
for k in range(data_resto.shape[0]):
	# Vacio es que es un Nan
	if data_resto['review_text'][k] != '':
		# Sentiment Analysis
		sentiment = analyzeSentiment(data_resto['review_text'][k])
		if sentiment == 'NEG':
			sentiments['NEG'] += 1
		elif sentiment == 'NEU':
			sentiments['NEU'] += 1
		elif sentiment == 'POS':
			sentiments['POS'] += 1
		# Limpia las palabras basura
		important_text = remove_stop_words(data_resto['review_text'][k])
		# Para el wordcloud
		comment_text += " "+data_resto['review_text'][k]+" "
		total_text_review.append(important_text)
		dict = {'review': important_text,'rating':data_resto['review_rating'][k],'sentiment': sentiment}
		dict_reviews_rating.append(dict)

print(sentiments)

# In charge of wordclouds
# wordcloud(give_stopwords_es() , comment_text)

# print(dict_reviews_rating)