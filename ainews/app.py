from flask import Flask, render_template, request, jsonify
from ainews.crew import generate_news
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']
        try:
            content = generate_news(topic)
            return jsonify({'content': content})
        except Exception as e:
            logging.error(f"Error generating news: {str(e)}")
            return jsonify({'error': 'An error occurred while generating the news article.'}), 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
