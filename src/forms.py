from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms import validators


class TweetForm(Form):
    tweet_text = StringField('tweet_text', [validators.required(),
                             validators.length(max=15)])


class DecryptForm(Form):
    decrypt_text = TextAreaField('decrypt_text', [validators.required(),
                                 validators.length(max=200)])
