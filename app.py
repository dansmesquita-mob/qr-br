import base64

from flask import Flask, render_template, request
from flask_qrcode import QRcode

app = Flask(__name__)
qrcode = QRcode(app)
app.secret_key = 'notsharemycodenever'


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('home.html')

@app.route("/qrcode", methods=["POST", "GET"])
def qr():
    if request.method == "POST":
        dataqr = request.form["data"]
        if not dataqr:
            return render_template('home.html')
        try:
            img = qrcode(dataqr)
            imgAscii =img.encode('ascii')
            #base64 para download:
            bs64txt = base64.b64encode(imgAscii).decode('utf-8')

            return render_template('home.html', dataqr=dataqr, img=img, bs64txt=bs64txt)
        except Exception as erro:
            return render_template('erro.html', erro=erro)
    else:
        return render_template("home.html")
