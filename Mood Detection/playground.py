import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

emotion_dataset = pd.read_csv("emotions.csv")
model = joblib.load("emotion_classifier_model.pkl")

features = emotion_dataset['Clean Text']
cv = CountVectorizer()
cv.fit_transform(features)

text = ""
while True:
    text = input("Enter your entry to test (or type \"quit\" to stop): ")
    if text == "quit":
        break
    entry = [text]
    vect = cv.transform(entry).toarray()
    print(model.predict(vect))