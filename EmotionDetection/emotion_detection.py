import requests

def emotion_detector(text_to_analyze):
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    response = requests.post(url, headers=headers, json=body)
    if response.status_code // 100 == 2:
        json = response.json()
        emotion, score = get_dominant_emotion(json)
        json = response.json()
        emotions = json["emotionPredictions"][0]["emotion"]
        emotions['dominant_emotion'] = emotion
        return emotions
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            'dominant_emotion': None
        }


def get_dominant_emotion(response):
    """
    Returns the dominant emotion and its score from an emotion prediction response.

    Args:
        response (dict): Emotion analysis response.

    Returns:
        tuple: (emotion_name, score)
    """
    emotions = response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    return dominant_emotion, emotions[dominant_emotion]