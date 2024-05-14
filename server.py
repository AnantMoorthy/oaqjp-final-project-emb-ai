''' Executing this function initiates the application of emotion detection to be
    executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

'''this is to avoid error'''
@app.route("/emotionDetector")
def sent_detector():
    '''function for receiving text and running through emotion detector'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    if response["dominant_emotion"] is not None:
        return (f"For the given statement, the system response is 'anger': {response['anger']},"
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.")
    return None

@app.route("/")
def render_index_page():
    """Render HTML template."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
