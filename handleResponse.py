import random
from functions.getWeather import get_weather_response
from functions.getTime import get_time_response


def handle_response(tag, sentence, intents, bot_name):
    if tag == "weather":
        weather_info = get_weather_response(sentence)
        return f"{bot_name}: {weather_info}"
    
    elif tag == "time":
        current_time = get_time_response()
        for intent in intents['intents']:
            if intent["tag"] == "time":
                response = random.choice(intent['responses']).format(current_time=current_time)
                return f"{bot_name}: {response}"
    else:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return f"{bot_name}: {random.choice(intent['responses'])}"
                
    return f"{bot_name}: Sorry, I couldn't catch that."