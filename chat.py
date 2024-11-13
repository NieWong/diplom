import random
import json
import torch
import os
from chatbot.missSpelling import MisspellingCorrector
from chatbot.model import NeuralNet 
from chatbot.nltkUtils import bag_of_words, tokenize
from handleResponse import handle_response 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
script_dir = os.path.dirname(os.path.abspath(__file__))
intents_path = os.path.join(script_dir, 'chatbot/data/intents.json')

with open(intents_path, 'r') as json_data:
    intents = json.load(json_data)
FILE = "chatbot/data.pth"
data = torch.load(FILE, weights_only=True)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

corrector = MisspellingCorrector(all_words)
bot_name = "Ivan"
print("Let's chat! (type 'quit' to exit)")

while True:
    sentence = input("You: ").lower()
    if sentence == "quit":
        break

    sentence_tokens = tokenize(sentence)
    corrected_sentence = corrector.correct(sentence_tokens)

    X = bag_of_words(corrected_sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        response = handle_response(tag, sentence, intents, bot_name)
        print(response)
    else:
        print(f"{bot_name}: Sorry, I couldn't catch that.")