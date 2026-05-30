"""
Emotion Detection Flask Application.

This module provides a web interface using Flask to analyze text inputs
and return a breakdown of detected emotions along with the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def get_emotion():
    """
    Analyze the provided text from request arguments and return the emotion scores.
    
    If the input is invalid or dominant_emotion is None, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # If dominant_emotion is None, the input text was invalid
    if response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!'

    return format_response(response)


@app.route("/")
def render_index_page():
    """
    Render the main application index page.
    """
    return render_template('index.html')


def format_response(response):
    """
    Format the emotion detector response dictionary into a human-readable string.
    """
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant_emotion = response.get('dominant_emotion')

    # Build the breakdown string for each emotion score
    emotion_strings = [f"'{emo}': {response.get(emo, 0)}" for emo in emotions]
    breakdown = ", ".join(emotion_strings)

    return (
        f"For the given statement, the system response is {breakdown}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
