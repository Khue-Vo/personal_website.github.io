import os
import re
import frontmatter
import markdown
from flask import Flask, current_app, render_template, send_from_directory, abort

from utils import format_date, get_all_projects

app = Flask(__name__)

# Define the directory where project markdown files are stored
PROJECTS_DIR = os.path.join(app.root_path, 'static', 'projects')

@app.route('/')
def index():
    # Renders "About Me" 
    return render_template('index.html')

@app.route('/projects/')
def projects():
    # Renders entries (SOAR narratives & failure story)
    project_entries = get_all_projects(PROJECTS_DIR)
   
    return render_template(
        'projects.html', 
        entries=project_entries,
        format_date=format_date, 
    )

@app.route('/projects/<entry>/')
def project_detail(entry):
    file_path = os.path.join(PROJECTS_DIR, f"{entry}.md")
    
    if not os.path.exists(file_path):
        abort(404)
        
    post = frontmatter.load(file_path)
    raw_markdown = post.content
    fixed_markdown = fixed_markdown = re.sub(r'\((\.\.\/)*image\/', r'(/static/image/', raw_markdown)
    html_content = markdown.markdown(fixed_markdown)
    
    return render_template(
        'content.html',
        title=post.get("title"),
        content=html_content,
        tags=post.get("tags", [])
    )

@app.route('/resume/')
def resume():
    # Renders 1-2 page resume
    return render_template('resume.html')

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