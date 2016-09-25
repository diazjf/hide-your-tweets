import os
import base64

import bbc_auth
import forms

from cryptography.fernet import Fernet
from flask import Flask
from flask import render_template, flash, redirect
from flask import request


app = Flask(__name__)
app.config.from_object('config')


def get_secret():
    """Authenticates user and obtains the one time use key"""
    barbican = bbc_auth.get_auth()
    secret_url = os.getenv('OS_SECRET_URL', None)
    secret = barbican.secrets.get(secret_url)
    return secret


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Hide Yo Kids, Hide Yo Tweets')


@app.route('/tweet', methods=['GET', 'POST'])
def generate_tweet():
    form = forms.TweetForm()
    if form.validate_on_submit():
        if 'submit' in request.form:
            try:
                txt = str(form['tweet_text'].data)
                secret = get_secret()

                payload = base64.urlsafe_b64encode(secret.payload)
                f = Fernet(payload)

                encrypted_txt = str(f.encrypt(txt))

            except Exception:
                return render_template('wrong.html')

            return redirect("https://twitter.com/intent/tweet?text=" +
                            encrypted_txt, code=302)
    else:
        return render_template('tweet.html',
                               title='Hide Yo Kids, Hide Yo Tweets',
                               form=form)


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    form = forms.DecryptForm()
    if form.validate_on_submit():
        if 'submit' in request.form:
            try:
                txt = str(form['decrypt_text'].data)
                secret = get_secret()
                payload = base64.urlsafe_b64encode(secret.payload)
                f = Fernet(payload)

                decrypted_txt = str(f.decrypt(txt))

                # adds decrypted message to decrypt.html and then renders it
                flash(decrypted_txt)
                return render_template('decrypt.html',
                                       title='Hide Yo Kids, Hide Yo Tweets',
                                       form=form)

            except Exception:
                return render_template('wrong.html')
    else:
        return render_template('decrypt.html',
                               title='Hide Yo Kids, Hide Yo Tweets',
                               form=form)


# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
