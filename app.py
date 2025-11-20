from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import os
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')
app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(filename= self.filename)

@app.route('/', methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train', methods = ['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"

@app.route('/predict', methods = ['POST'])
@cross_origin()
def PredictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)  #decodeimage download the image and save into the current working directory
        result = clApp.classifier.predict()
        return jsonify({'result': result})

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug= True)

