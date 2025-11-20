import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:

    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        #load model
        model = load_model(os.path.join("artifacts","trained_model","model.h5"))

        #load and preprocess image
        imagename = self.filename
        img = image.load_img(imagename, target_size=(224, 224)) #imagename actually acts as a directory
        # Convert PIL image to a NumPy array (H, W, C)
        img = image.img_to_array(img)
        # Add batch dimension → shape becomes (1, 224, 224, 3)
        img = np.expand_dims(img, axis=0)
        # Run model prediction and get the class index with highest probability
        result = np.argmax(model.predict(img), axis=-1)
        print(result)



        if result[0] == 0:     #class 0 is predicted based on alphabetical order of folders during training
            return "Coccidiosis"
    
        else:
            return "Healthy"
