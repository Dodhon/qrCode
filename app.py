from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import requests
import os
from io import BytesIO

app = Flask(__name__)

# Define the directory to save QR codes
DIRECTORY = os.path.join(os.getcwd(), 'qr_codes')

if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

def generate_qr_code(link, name):
    endpoint = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={link}"
    image_path = os.path.join(DIRECTORY, f"{name}_qr_code.png")
    response = requests.get(endpoint)
    with open(image_path, 'wb') as f:
        f.write(response.content)
    return image_path

def get_qr_code(link, name):
    endpoint = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={link}"
    response = requests.get(endpoint)
    return response.content

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        url = request.form.get('url').strip()

        if not name or not url:
            flash('Please enter both name and URL.', 'error')
            return redirect(url_for('index'))

        try:
            # Generate QR code and save it
            image_path = generate_qr_code(url, name)
            return send_file(image_path, as_attachment=True)
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
