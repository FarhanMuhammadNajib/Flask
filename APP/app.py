from flask import Flask, render_template, request
# from Predict import preds
from PIL import Image
import os
import base64
import io
import cv2
# from colorMap import get_new_color_img

app= Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

# ALLOWED_EXTENSIONS = {'java', 'py', 'php', 'js', 'go'}
# def allowed_file_extensions(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route("/predict", methods=['POST'])
# def predict():
#     if request.method == "POST":
#         predictfile=request.files['predictFile']
#         if predictfile is None or predictfile.filename == "":
#             im = Image.open("./static/PredictFile/ErrorImage/NoFile.png")
#             data = io.BytesIO()
#             im.save(data, "PNG")
#             encoded_img_data = base64.b64encode(data.getvalue())
            
#             return  render_template("Predict.html", prediction = "No file submited", img_path = encoded_img_data.decode('utf-8'))
#         elif not allowed_file_extensions(predictfile.filename):
#             im = Image.open("./static/PredictFile/ErrorImage/NotSupported.png")
#             data = io.BytesIO()
#             im.save(data, "PNG")
#             encoded_img_data = base64.b64encode(data.getvalue())
#             return  render_template("Predict.html", prediction = "No file submited", img_path = encoded_img_data.decode('utf-8') )
        
#         filePath="./static/PredictFile/" + predictfile.filename
#         predictfile.save(filePath)
        
#         im = get_new_color_img(filePath)
#         img_path = filePath + '.png'

#         cv2.imwrite(img_path, im)

#         try:
#             p = preds(img_path)
#             im = Image.open(img_path)
#             data = io.BytesIO()
#             im.save(data, "PNG")
#             encoded_img_data = base64.b64encode(data.getvalue())
            
#             if os.path.exists(img_path) and os.path.exists(filePath):  
#                 os.remove(img_path)
#                 os.remove(filePath)
#             return render_template("Predict.html", prediction = p, img_path = encoded_img_data.decode('utf-8'))
#         except Exception as err:
#             # return jsonify({'error': 'Error during prediction'})
#             return render_template("Predict.html", prediction = err)
        
        # # prediction=prediksi(filePath)
        
        # # im = Image.open(filePath)
        # # data = io.BytesIO()
        # # im.save(data, "JPEG")
        # # encoded_img_data = base64.b64encode(data.getvalue())
        
        # # if os.path.exists(filePath):  
        # #     os.remove(filePath)
        
        # # return render_template("Predict.html", prediction = prediction, img_path = encoded_img_data.decode('utf-8'))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')