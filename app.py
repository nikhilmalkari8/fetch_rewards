from flask import Flask, request, jsonify
import re
import math

# Create a Flask web application
app = Flask(__name__)

# Function to preprocess text by removing non-alphanumeric characters and converting to lowercase
def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    return text

# Function to tokenize text into words and create a dictionary of word frequencies
def tokenize(text):
    words = re.findall(r'\w+', text)
    return {word: 1 for word in words}

# Function to calculate cosine similarity between two texts
def cosine_similarity(text1, text2):
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)

    # Find common words in both texts
    common_words = set(tokens1.keys()).intersection(tokens2.keys())

    # Calculate dot product, magnitude of vectors, and similarity
    dot_product = sum(tokens1.get(word, 0) * tokens2.get(word, 0) for word in common_words)
    magnitude1 = math.sqrt(sum(tokens1.get(word, 0)**2 for word in tokens1))
    magnitude2 = math.sqrt(sum(tokens2.get(word, 0)**2 for word in tokens2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity

# Function to calculate Jaccard similarity between two texts
def jaccard_similarity(text1, text2):
    tokens1 = set(tokenize(text1).keys())
    tokens2 = set(tokenize(text2).keys())

    # Calculate intersection and union of sets
    intersection = len(tokens1.intersection(tokens2))
    union = len(tokens1.union(tokens2))

    if union == 0:
        return 0

    similarity = intersection / union
    return similarity

# Define a route for comparing texts via POST request
@app.route('/compare', methods=['POST'])
def compare_texts():
    # Get JSON data from the POST request
    data = request.get_json()
    
    # Preprocess the input texts
    text1 = preprocess_text(data.get('text1', ''))
    text2 = preprocess_text(data.get('text2', ''))

    # Calculate cosine and Jaccard similarities
    cosine_similarity_score = cosine_similarity(text1, text2)
    jaccard_similarity_score = jaccard_similarity(text1, text2)

    # Create a result dictionary with similarity scores
    result = {
        'cosine_similarity': cosine_similarity_score,
        'jaccard_similarity': jaccard_similarity_score
    }

    # Return the result as JSON
    return jsonify(result)

# Run the Flask app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
