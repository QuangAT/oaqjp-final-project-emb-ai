from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask,render_template,request

#Initiate the flask app : 
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion_detector():
    emotions = emotion_detector('I love my life')
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant_emotion = emotions['dominant_emotion']
    return f"For the given statement, the system response is 'anger\': {anger_score}, 'disgust\': {disgust_score}, 'fear\': {fear_score}, 'joy\': {joy_score}, and 'sadness\': {sadness_score}. The dominant education is {dominant_emotion}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0",port=5000)