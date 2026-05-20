from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Renders your "About Me" unique combination pitch and core skills
    return render_template('index.html')

@app.route('/projects/')
def projects():
    # Renders your 5 required entries (SOAR narratives & failure story)
    return render_template('projects.html')

@app.route('/resume/')
def resume():
    # Renders or embeds your 1-2 page resume
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)