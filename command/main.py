import numpy as np
import logging
from tensorflow.keras import models
from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("prediction_log.txt"),
        logging.StreamHandler() 
    ]
)

commands = ['bairshil', 'bayrtai', 'holbogd', 'orchuul', 'seruuleg', 'temdeglel', 'tsag',
            'tsagAgaar', 'wikipedia']

loaded_model = models.load_model("saved_model.keras")

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    
    logging.info(f"Predicted label: {command}")
    
    return command

if __name__ == "__main__":
    while True:
        command = predict_mic()
        if command == "bayrtai":
            logging.info("Stopping the program.")
            terminate()
            break
