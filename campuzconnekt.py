import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Download the required NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load the data
train_data = pd.read_csv('processed_content.csv')

# Define a function to tokenize the text
def tokenize_text(text):
    if isinstance(text, str):
        text = re.sub(r'http\S+', '', text)  # Remove URLs
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token.isalpha()]  # only alphabetic tokens
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.lower() not in stop_words]  # Filter out stop words
        return ''.join(tokens)  # Join tokens with spaces
    else:
        return ''

# Apply the tokenize function to the 'headings' column
train_data['headings'] = train_data['headings'].apply(tokenize_text)

# Define the conditions for the np.select function
conditions = [
    train_data['title'].str.contains('admission', case=False),
    train_data['title'].str.contains('courses', case=False),
    train_data['title'].str.contains('faculty', case=False),
    train_data['title'].str.contains('facilities', case=False)
]

# Define the choices for the np.select function
choices = [0, 1, 2, 3]

# Create the 'intent_label' column
train_data['intent_label'] = np.select(conditions, choices, default=4)

# Split the data into training and testing sets
X_train = train_data['headings']
y_train = train_data['intent_label']

# Create a vectorizer object
vectorizer = CountVectorizer()

# Fit the vectorizer to the training data and transform it into a numerical array
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train a Naive Bayes classifier on the vectorized training data
clf = MultinomialNB()
clf.fit(X_train_vectorized, y_train)

# Ask a query
query = input("Please enter a question or statement: ")

# Tokenize the query
query_tokenized = tokenize_text(query)

# Vectorize the query
query_vectorized = vectorizer.transform([query_tokenized])

# Make a prediction
prediction = clf.predict(query_vectorized)

# Find the relevant data
if prediction == 0:
    relevant_data = train_data[train_data['intent_label'] == 0]
elif prediction == 1:
    relevant_data = train_data[train_data['intent_label'] == 1]
elif prediction == 2:
    relevant_data = train_data[train_data['intent_label'] == 2]
elif prediction == 3:
    relevant_data = train_data[train_data['intent_label'] == 3]
else:
    relevant_data = train_data[train_data['intent_label'] == 4]

# Print the reply
if relevant_data.empty:
    print("Sorry, I couldn't find any relevant information.")
else:
    print(relevant_data['description'].iloc[0])