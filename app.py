from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Redirect to login after registration
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Redirect to meme_output after login
        return redirect(url_for('meme_output'))
    return render_template('login.html')

@app.route('/meme_output', methods=['GET', 'POST'])
def meme_output():
    if request.method == 'POST':
        emotion = request.form.get('emotion').lower()
        # Sample images for each emotion
        sample_images = {
            'anger': ['../images/anger1.jpeg','../images/anger2.jpg','../images/anger3.jpeg'],
            'cry': ['../images/cry1.jpeg','../images/cry2.jpeg','../images/cry3.jpeg'],
            'fear': ['../images/fear1.png','../images/fear2.jpg','../images/fear3.jpg'],
            'funny': ['../images/funny1.jpg','../images/funny2.jpeg','../images/funny3.jpg'],
            'happiness': ['../images/happiness1.jpeg','../images/happiness2.jpg','../images/happiness3.jpg'],
            'sadness': ['../images/sadness1.jpeg','../images/sadness2.jpg','../images/sadness3.jpg'],
            'surprise': ['../images/suprise1.jpeg','../images/suprise2.jpg','../images/suprise3.jpg']
        }
        images = sample_images.get(emotion, [])
        return render_template('meme_output.html', images=images, emotion=emotion)
    return render_template('meme_output.html')

if __name__ == '__main__':
    app.run(debug=True)
