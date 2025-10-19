from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from compressor import compress_image
import os

app = Flask(__name__)

app.secret_key = "345efge298u2hjwbnfa98yft4r4,md98t92lkew,mfds984tr9po42ngfh30orkgj894oiewlkdsm"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'image' not in request.files:
        return redirect("/")

    file = request.files['image']
    k = int(request.form.get('k', 50))

    if file.filename == '':
        return redirect("/")

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join("static\\uploads", filename)
        print(file_path)
        file.save(file_path)

        # Read bytes and compress
        with open(file_path, 'rb') as f:
            image_bytes = f.read()

        compressed_bytes_io = compress_image(image_bytes, k)

        # Save compressed image
        compressed_path = os.path.join("static\\results", f'compressed_{filename}')
        with open(compressed_path, 'wb') as f:
            f.write(compressed_bytes_io.read())

        return render_template('result.html',
                               original_image=url_for('static', filename=f'uploads/{filename}'),
                               compressed_image=url_for('static', filename=f'results/compressed_{filename}'),
                               k=k)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)