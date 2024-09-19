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
import os

# Download the required NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load the data
df = pd.read_csv('scraped_content_final.csv')

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
df['headings'] = df['headings'].apply(tokenize_text)

# Apply the tokenize function to the 'paragraphs' column
df['paragraphs'] = df['paragraphs'].apply(tokenize_text)

# Apply the tokenize function to the 'file_downloads' column
df['file_downloads'] = df['file_downloads'].apply(tokenize_text)

# Print a subset of the updated dataframe to verify the changes
print(df.head())

# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create a new directory for the output file if it doesn't exist
output_dir = os.path.join(current_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the updated DataFrame to a new CSV file
df.to_csv(os.path.join(output_dir, 'processed_content.csv'), index=False)

# Load the processed data
df = pd.read_csv(os.path.join(output_dir, 'processed_content.csv'))

# Define the conditions for the np.select function
conditions = [
    df['title'].str.contains('admission', case=False),
    df['title'].str.contains('courses', case=False),
    df['title'].str.contains('faculty', case=False),
    df['title'].str.contains('facilities', case=False)
]

# Define the choices for the np.select function
choices = [0, 1, 2, 3]

# Define a default value for np.select
default = 4

# Assign the intent labels
df['intent_label'] = np.select(conditions, choices, default=default)

# Split the data into training and testing sets
X = df[['title', 'headings']]
y = df['intent_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a vectorizer object
vectorizer = CountVectorizer()

# Fit the vectorizer to the training data and transform it into a numerical array
X_train_vectorized = vectorizer.fit_transform(X_train['title'] +'' + X_train['headings'])

# Transform the test data into a numerical array
X_test_vectorized = vectorizer.transform(X_test['title'] +'' + X_test['headings'])

# Train a Naive Bayes classifier on the vectorized training data
clf = MultinomialNB()
clf.fit(X_train_vectorized, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test_vectorized)

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)