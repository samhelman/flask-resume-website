from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '94aac65b82f07a908038adb9383f58ddca82a30df2bc0f8f66590c4a98e0b657'

from mainapp import routes