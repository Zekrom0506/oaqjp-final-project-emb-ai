"""
Emotion Detection Web Application
Flask server integrating EmotionDetection package.
Provides web interface for sentiment analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/")
def render_index_page():
    """
    Render the main index.html page with emotion analysis interface.
    
    Returns:
        Flask Response: Rendered index.html template.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotion in text sent by JavaScript frontend.
    
    Expects GET request with query param 'textToAnalyze'.
    
    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again."
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant = response["dominant_emotion"]
    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
    return result_text
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
