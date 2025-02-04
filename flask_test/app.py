from flask import Flask, request, jsonify, send_file, render_template
import os
import torch
from PIL import Image
import subprocess
import re

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
DATA_PATH='/Users/anurithalokesh/Downloads/shelf-product-identifier-main/data'

def get_text_lines(text_path):
    with open(text_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]  # Strip to remove \n
    return lines

def detect_image(image_path):
    """Convert image to grayscale and save it."""
    subprocess.run(["python", "/Users/anurithalokesh/Downloads/shelf-product-identifier-main/main.py", "--input", f"{image_path}"])
    DATA_PATH='/Users/anurithalokesh/Downloads/shelf-product-identifier-main/data'
    filename=os.path.basename(image_path)
    clean_file=re.sub(r'\.[^.]+$', '', filename)
    NEW_PATH = f"{DATA_PATH}/{clean_file}/{filename}"
    get_path= f"{DATA_PATH}/{clean_file}/predictions.txt"
    MID_PATH = f"{DATA_PATH}/{clean_file}"
    img = Image.open(NEW_PATH) 
    processed_path = os.path.join(PROCESSED_FOLDER, os.path.basename(image_path))
    img.save(processed_path)
    text=get_text_lines(get_path)
    return processed_path,text[:10]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)
    p_path,caption = detect_image(image_path)
    #caption = generate_caption(image_path)
    
    return jsonify({
        'processed_image': f'/processed/{file.filename}',
        'caption': caption
    })

@app.route('/processed/<filename>')
def get_processed_image(filename):
    return send_file(os.path.join(PROCESSED_FOLDER, filename))

if __name__ == '__main__':
    app.run(debug=True)