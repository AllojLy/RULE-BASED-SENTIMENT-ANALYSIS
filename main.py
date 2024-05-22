from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)

        # Check for negative sentiment
        if score['neg'] > score['pos']:  # Compare 'neg' and 'pos' values
            return render_template('index.html', message="Negative")
        else:
            return render_template('index.html', message="Positive")

    return render_template('index.html', message="")  # Pass an empty message for initial GET request