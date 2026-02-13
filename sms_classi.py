import pandas as pd

df = pd.read_csv("spam.csv", encoding="latin-1")
df.head()
df = df[['v1', 'v2']]
df.columns = ['label', 'message']
df.head()
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
df['label'].value_counts()
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

df['clean_message'] = df['message'].apply(clean_text)
df[['message', 'clean_message']].head()
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=3000)

X = vectorizer.fit_transform(df['clean_message'])
y = df['label']
df.isnull().sum()
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
y_pred_nb = nb_model.predict(X_test)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

accuracy_nb = accuracy_score(y_test, y_pred_nb)
conf_matrix_nb = confusion_matrix(y_test, y_pred_nb)
class_report_nb = classification_report(y_test, y_pred_nb)

accuracy_nb, conf_matrix_nb
print(class_report_nb)
import pickle

pickle.dump(nb_model, open("nb_model.pkl", "wb"))
pickle.dump(vectorizer, open("tfidf.pkl", "wb"))

