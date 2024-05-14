import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        output_format = {'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None
                        }
        return output_format

    elif response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        dom_emotion = max(emotion, key=emotion.get)
        anger = emotion['anger']
        disgust = emotion['disgust']
        fear = emotion['fear']
        joy = emotion['joy']
        sadness = emotion['sadness']
        output_format = {
                        'anger': anger,
                        'disgust': disgust,
                        'fear': fear,
                        'joy': joy,
                        'sadness': sadness,
                        'dominant_emotion': dom_emotion
                        }
        output_format["dominant_emotion"] = max(emotion, key=emotion.get)
    return output_format
   
    #return response.text