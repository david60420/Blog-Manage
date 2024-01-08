from flask import Flask, render_template

app = Flask(__name__)

# Sample blog post data
blog_posts = [
    {"id": 1, "title": "First Post", "content": "<p>This is the content of the first post.</p>", "publish_date": "2024-01-08"},
    # Add more posts as needed
]

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

if __name__ == '__main__':
    app.run(debug=True)
