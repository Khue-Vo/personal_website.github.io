from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Renders "About Me" 
    return render_template('index.html')

@app.route('/projects/')
def projects():
    # Renders 5 entries (SOAR narratives & failure story)
    return render_template('projects.html')

@app.route('/resume/')
def resume():
    # Renders 1-2 page resume
    return render_template('resume.html')
from flask import send_from_directory, current_app
import os

@app.route('/resume/view')
def serve_resume():
    # Points to static/docs directory
    directory = os.path.join(current_app.static_folder, 'docs')
    filename = 'resume.pdf'
    
    return send_from_directory(
        directory, 
        filename, 
        as_attachment=False, # Prevents forcing a download
        mimetype='application/pdf' # Tells browser how to render it
    )

if __name__ == '__main__':
    app.run(debug=True)