from flask import Flask, render_template

app = Flask(__name__)

# Sample
blog_posts = [
    {"id": 1, "title": "First Post", "summary": "This is the summary of the first post.", "publish_date": "2024-01-08"},
    
]

@app.route('/')
def home():
    return render_template('home.html', blog_posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
