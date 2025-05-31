# Import the requests library to handle HTTP requests
import requests 
import json

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def sentiment_analyzer(text_to_analyse):  
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)  
    
    # Extracting sentiment label and score from the response
    formatted_response = json.loads(response.text)
    
    # Extracting sentiment label and score from the response
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

     # Return the response text from the API
    return {'label': label, 'score': score}

def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)
    
    # Extract the label and score from the response
    label = response['label']
    score = response['score']
    
    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)