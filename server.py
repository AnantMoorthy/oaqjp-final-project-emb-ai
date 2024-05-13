from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['label']
    score = response['score']
    if label is None:
        return "Invalid input ! Try again."
    if label is not None:
        return f"The given text is {label.split('_')[1]} with a score of {score}."
    return None

@app.route("/")
def render_index_page():
    """Render HTML template."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
