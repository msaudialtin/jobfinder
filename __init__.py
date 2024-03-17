from job_routs import job_routes
from prisma import Client
from flask import Flask, render_template
from app.config import Config  # Updated import path
import sys
from pathlib import Path

# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).parent))

prisma = Client()

app = Flask(__name__)
prisma = Config.PRISMA

# # Connect the Prisma client
# prisma.connect()
# Check if the Prisma client is not already connected before connecting
if not prisma.is_connected():
    # Connect the Prisma client
    prisma.connect()

# Register the job_routes blueprint
app.register_blueprint(job_routes)


@app.route("/")
def home():

    # Render HTML template and pass the job data
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/joblist')
def joblist():
    return render_template('joblist.html')


@app.route('/job-detail')
def jobdetail():
    return render_template('job-detail.html')


@app.route('/job-apply')
def jobapply():
    return render_template('job-apply.html')


@app.route('/login')
def login():
    return render_template('login-page.html')


if __name__ == '__main__':
    app.run(debug=True)
