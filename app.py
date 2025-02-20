from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Dummy data for DJ posts
posts = [
    {
        'id': 1,
        'title': "Theres a Flood in the lands",
        'date': "2025-02-15",
        'content': "What does one do to endure such extreme weather?",
        'image': "images/yard.jpeg",
        'audio': "audio/knights.mp3"
    },
    {
        'id': 2,
        'title': "Who actually knows how to fly a plane?",
        'date': "2025-02-20",
        'content': "Youre in a plane and then all of a sudden the pilot cant control it",
        'image': "images/snowy.jpeg",
        'audio': "audio/djset2.mp3"
    }
]

# Inject current year into templates
@app.context_processor
def inject_now():
    return {'year': datetime.utcnow().year}

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((item for item in posts if item["id"] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

if __name__ == '__main__':
    app.run(debug=True)
