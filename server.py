from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def get_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return format_response(response)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


def format_response(response):
    '''
    For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy.
    '''
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    text = f'For the given statement, the system response is'

    if anger:
        text = text + f' anger: {anger}'
    if disgust:
        text = text + f', disgust: {disgust}'
    if fear:
        text = text + f', fear: {fear}'
    if joy:
        text = text + f', joy: {joy}' 
    if sadness:
        text = text + f', sadness: {sadness}'
    if dominant_emotion:
        text = text + f'. The dominant emotion is {dominant_emotion}.'
    
    return text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)