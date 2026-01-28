import requests 
import json

def emotion_detector(text_to_analyse):

    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            "anger": None, "disgust": None, "fear": None, 
            "joy": None, "sadness": None, "dominant_emotion": None
        }
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    myobj = {
        "raw_document": {
            "text": text_to_analyse  
        }
    }
    
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
            "anger": None, "disgust": None, "fear": None, 
            "joy": None, "sadness": None, "dominant_emotion": None
        }

    formatted_response = json.loads(response.text)

    emotions_dict = formatted_response["emotionPredictions"][0]["emotion"]

    scores = {
        "anger": emotions_dict.get("anger", 0), 
        "disgust": emotions_dict.get("disgust", 0),
        "fear": emotions_dict.get("fear", 0),
        "joy": emotions_dict.get("joy", 0),
        "sadness": emotions_dict.get("sadness", 0)
    }
    
    dominant_emotion = max(scores, key=scores.get)
    
    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant_emotion
    }

    