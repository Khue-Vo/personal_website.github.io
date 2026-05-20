# utils.py
from datetime import datetime
import os
import frontmatter

def format_date(date_str):
    """Converts '2026-05-20' into a clean format like 'May 20, 2026'."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")
    except (ValueError, TypeError):
        return date_str

def get_all_projects(directory_path):
    """Reads, parses, and returns a sorted list of all project markdown files."""
    projects = []
    if not os.path.exists(directory_path):
        return projects

    for filename in os.listdir(directory_path):
        if filename.endswith('.md'):
            slug = filename[:-3]  # Strip '.md' extension
            file_path = os.path.join(directory_path, filename)
            
            try:
                post = frontmatter.load(file_path)
                project_data = {
                    "slug": slug,
                    "title": post.get("title", slug.replace("-", " ").title()),
                    "pub_date": post.get("pub_date", "2026-01-01"),
                    "summary": post.get("summary", ""),
                    "tags": post.get("tags", [])
                }
                projects.append(project_data)
            except Exception as e:
                # Log or handle corrupted files gracefully if necessary
                continue
            
    # Sort projects by publication date, newest first
    projects.sort(key=lambda x: x['pub_date'], reverse=True)
    return projects
