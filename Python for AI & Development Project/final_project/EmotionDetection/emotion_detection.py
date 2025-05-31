# Import the requests library to handle HTTP requests
import requests 
import json

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header,timeout=10) 

    # Format response as JSON
    formatted_response = json.loads(response.text)
 
    if response.status_code == 200:
        return formated_response
    elif response.status_code == 400:
        formated_response = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None}
    return formated_response

    # Extracting emotion label and score from the response
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotionlist = {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness}
    dominant_emotion = max(emotionlist, key=emotionlist.get)

    # Return the response text from the API
    return {
        'anger': anger, 
        'disgust': disgust, 
        'fear': fear, 
        'joy': joy, 
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
        }


