import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from emoji import demojize

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    text = demojize(text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags = re.MULTILINE)
    text = re.sub(r'\@\w+', '@mention', text)
    text = text.replace("’", "'")
    negations = {
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "haven't": "have not",
    "hasn't": "has not",
    "hadn't": "had not",
    "won't": "will not",
    "wouldn't": "would not",
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "can't": "cannot",
    "couldn't": "could not",
    "shouldn't": "should not",
    "mightn't": "might not",
    "mustn't": "must not"
    }
    for negation, expanded in negations.items():
        text = text.replace(negation, expanded)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def tokenize_text(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

def preprocess_text(text):
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)
    filtered_tokens = remove_stopwords(tokens)
    return ' '.join(filtered_tokens)

if __name__ == '__main__':
    sample_text = 'This is a sample tweet with #Hashtag and a URL http://example.com'
    processed_text = preprocess_text(sample_text)
    print(processed_text)