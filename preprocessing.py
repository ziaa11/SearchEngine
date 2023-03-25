import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer

#Requirments
nltk.download('wordnet')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()

def preprocess_sentence(sentence):
    
    sentence = sentence.lower()
    sentence = list(sentence.split())
    # sentence = list(set(sentence.split())) # Removing duplicates
    
    sentence = [word for word in sentence if not word in stop_words] # Removing stopwords
    
    sentence = [stemmer.stem(word) for word in sentence] # Stemming
    
    sentence = [lemmatizer.lemmatize(word) for word in sentence] # Lemmatization
    return sentence
