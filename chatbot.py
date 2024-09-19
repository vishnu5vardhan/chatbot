import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Load the dataset (replace 'file_path' with your actual file path)
file_path = 'D:/GK/chatbot/data/scraped_content_final.csv'

df = pd.read_csv(file_path)

# Basic data cleaning
df.dropna(subset=['paragraphs'], inplace=True)  # Remove rows with empty content
df['combined_text'] = df['title'] + ' ' + df['headings'] + ' ' + df['paragraphs']

# Define input (questions) and output (answers) for training
X = df['combined_text']  # Use the combined text as input
y = df['paragraphs']  # Use paragraphs as the expected response (labels)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a pipeline with TF-IDF vectorizer and Logistic Regression model
model_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),  # TF-IDF vectorization
    ('clf', LogisticRegression(max_iter=1000))  # Logistic Regression as the classifier
])

# Train the model
model_pipeline.fit(X_train, y_train)

# Evaluate the model on test data
y_pred = model_pipeline.predict(X_test)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Function to predict response for user input
def predict_response(user_query):
    response = model_pipeline.predict([user_query])
    return response[0]

# Example usage
while True:
    user_input = input("Ask a question: ")
    if user_input.lower() == 'exit':
        break
    print("Predicted Response:", predict_response(user_input))
