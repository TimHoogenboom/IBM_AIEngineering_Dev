# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, request, render_template

# Import the sentiment_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection():
    'This code receives the text from the HTML interface and runs emotion detection.'
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return f"'anger' : {anger}, 'disgust' : {disgust}, 'fear' : {fear}, 'joy' : {joy} and 'sadness' : {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    'This function initiates the rendering of the main application page over the Flask channel'
    return render_template('index.html')

if __name__ == "__main__":
    'This functions executes the flask app and deploys it on localhost:5000'
    app.run(host="0.0.0.0", port=5000)