


from flask import Flask, request, render_template,redirect
from PIL import Image
from segment import process
import os

UPLOAD_FOLDER = 'predicted'

app = Flask(__name__, static_folder='predicted')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predicted")
def predicted():
    return render_template('predicted.html')

@app.route("/predict", methods=["post"])
def predict():

    img = request.files['file']
    if not img is None:            # Выполнение блока, если загружено изображение                                # Открытие изображения
        results = process(img)         # Обработка изображения с помощью функции, реализованной в другом файле

        results[0].save(os.path.join(app.config['UPLOAD_FOLDER'], 'source_image.jpg'))
        results[1].save(os.path.join(app.config['UPLOAD_FOLDER'], 'mask.png'))
        results[2].save(os.path.join(app.config['UPLOAD_FOLDER'], 'image_mask.jpg'))

    return redirect('/predicted')


if __name__ == "__main__":
    app.run()
