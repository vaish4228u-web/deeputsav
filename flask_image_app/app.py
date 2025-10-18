from flask import Flask, send_from_directory, render_template_string
import qrcode
import io
import base64
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
IMAGE_FILENAME = 'image.png'
PUBLIC_URL = f"https://deeputsavrmlau.exam.in/{IMAGE_FILENAME}"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def qr_interface():
    img = qrcode.make(PUBLIC_URL)
    buffer = io.BytesIO()
    img.save(buffer)
    buffer.seek(0)
    qr_code_img = base64.b64encode(buffer.read()).decode('utf-8')
    html = f'''
    <html>
    <head><title>Scan to view image</title></head>
    <body>
        <h2>Scan this QR code to view image at {PUBLIC_URL}</h2>
        <img src="data:image/png;base64,{qr_code_img}" alt="QR Code"/>
    </body>
    </html>
    '''
    return html

@app.route(f'/{IMAGE_FILENAME}')
def serve_image():
    return send_from_directory(UPLOAD_FOLDER, IMAGE_FILENAME)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
