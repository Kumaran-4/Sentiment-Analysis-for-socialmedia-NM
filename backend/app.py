from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    review = data.get('review', '')
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity

    # Sentiment classification
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return jsonify({
        'review': review,
        'sentiment': sentiment,
        'polarity': polarity
    })

if __name__ == '__main__':
    app.run(debug=True)
