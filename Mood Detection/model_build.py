from io import TextIOBase
import pandas as pd
import numpy as np
import neattext.functions as nfx
import csv
from sklearn import model_selection

# First, we convert our txt document that we got from online to a csv file for
# easier reading
# The dataset is from https://www.kaggle.com/praveengovi/emotions-dataset-for-nlp
# NOTE: This code is now commented out, since it only needs to run once

# file = open("train.txt", "r")
# with open('emotions.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Emotion', 'Text']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for line in file.readlines():
#         data = line.split(';')
#         text = data[0]
#         emotion = data[1].strip()

#         writer.writerow({'Emotion' : emotion, 'Text' : text})

# file.close()

# Now that we have the csv file, we can load the dataset
emotion_dataset = pd.read_csv("emotions.csv")

# Let's clean the text by removing noise (stopwords, punctuation, etc)
# I think the training file already doesn't have punctuation, but just in case, because
# I'm not about to check 16000 lines for punctuation manually
emotion_dataset['Clean Text'] = emotion_dataset['Text'].apply(nfx.remove_stopwords)
emotion_dataset['Clean Text'] = emotion_dataset['Clean Text'].apply(nfx.remove_punctuations)

# Now, we add the cleaned text to the csv file
# NOTE: This is also commented out, since we only want to do it once

# with open('emotions.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Emotion', 'Text', 'Clean Text']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     index = 0
#     for data in emotion_dataset['Clean Text']:
#         writer.writerow({'Emotion' : emotion_dataset['Emotion'][index], 
#                         'Text' : emotion_dataset['Text'][index],
#                         'Clean Text' : data})

# Now, we can begin the training!
from sklearn.naive_bayes import MultinomialNB

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split

# First, we have to build some features from out text
XFeatures = emotion_dataset['Clean Text']
ylabels = emotion_dataset['Emotion']

# Convert into vectors
cv = CountVectorizer()
x = cv.fit_transform(XFeatures)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(x, ylabels, test_size=0.3, random_state=42)

# Now we can build the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make a prediction to make sure the model is working
test_text = ["I am sad."]
vect = cv.transform(test_text).toarray()
print(model.predict(vect))

# Save the model for the application
import joblib

model_file = open("emotion_classifier_model.pkl", "wb")
joblib.dump(model, model_file)
model_file.close()