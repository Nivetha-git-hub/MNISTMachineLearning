from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField 
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/css/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/WebApp', methods=['GET',"POST"])
def WebApp():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data 
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)