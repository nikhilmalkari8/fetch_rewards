# Flask Text Comparison API

## Overview
This Flask application provides an API for comparing two text strings using Cosine and Jaccard similarity measures. It preprocesses text strings, tokenizes them, and calculates similarity scores, offering an easy-to-use RESTful API endpoint.

## Running using Docker 

[![Docker Pulls](https://img.shields.io/docker/pulls/nikhilmalkari/fetch_rewards)](https://hub.docker.com/r/nikhilmalkari/fetch_rewards)

## Installation

### Prerequisites
- Python 3.x
- Flask
- Dependencies listed in `requirements.txt`

### Setup
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/nikhilmalkari8/fetch_rewards.git
cd fetch_rewards
pip install -r requirements.txt
```
## Running the Application

Start the application with the following command:

```bash
python app.py
```
The application will be available at http://localhost:5000.

## API Endpoints

### POST /compare
Compares two text strings and returns their Cosine and Jaccard similarity scores.

Request Format:

```bash
{
    "text1": "string",
    "text2": "string"
}
```
Response Format:

```bash
{
    "cosine_similarity": float,
    "jaccard_similarity": float
}
```

## Functions Description

### preprocess_text(text)
Preprocesses the input text by converting it to lowercase and removing non-alphanumeric characters.

#### Parameters:
text (str): The text to preprocess.
#### Returns:
(str): The preprocessed text.

### tokenize(text)
Tokenizes the preprocessed text into words and creates a dictionary with words as keys.

#### Parameters:
text (str): The text to tokenize.
#### returns:
(dict): A dictionary of tokens.

### cosine_similarity(text1, text2)
Calculates the Cosine similarity between two text strings.

#### Parameters:
text1 (str): The first text string.
text2 (str): The second text string.
#### Returns:
(float): The Cosine similarity score.

### jaccard_similarity(text1, text2)
Calculates the Jaccard similarity between two text strings.

#### Parameters:
text1 (str): The first text string.
text2 (str): The second text string.
#### Returns:
(float): The Jaccard similarity score.
