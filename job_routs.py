from flask import Flask, Blueprint, redirect, url_for, jsonify, request, render_template
from prisma import Client

job_routes = Blueprint("job_routes", __name__, url_prefix="/app")
prisma = Client()

# Connect the Prisma client
prisma.connect()


@job_routes.route('/api/jobs', methods=['GET'])
def get_jobs():
    try:
        # Get the search query from the request parameters
        search_query = request.args.get('search', '')

        # Fetch job data from the database using Prisma Client
        jobs = prisma.job.find_many(include={'company': True})

        job_data = []

        for job in jobs:
            company = job.company
            if company is not None:
                # Check if the search query matches the job title
                if search_query.lower() in job.title.lower():
                    job_data.append({
                        'id': job.id,
                        # Handle cases where company.logo is None
                        'logo': company.logo if company.logo else '',
                        'title': job.title,
                        'location': job.location,
                        'employmentType': job.employmentType,
                        'salary': job.salaryRange,
                        'description': job.description,
                        'responsibilities': job.responsibilities,
                        'qualifications': job.qualifications
                    })

        return jsonify(job_data)

    except Exception as e:
        # Log the exception details
        print(f"Error fetching job data: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500


@job_routes.route('/job-detail/<int:job_id>')
def job_detail(job_id):
    try:
        # Fetch job data from the database based on the job ID
        job = prisma.job.find_unique(
            where={'id': job_id}, include={'company': True})

        if job:
            # Render HTML template and pass the job data
            return render_template('job-detail.html', job=job)
        else:
            # Handle the case where the job with the specified ID is not found
            return render_template('job-not-found.html')

    except Exception as e:
        # Log the exception details
        print(f"Error fetching job data: {str(e)}")
        return render_template('error.html'), 500


# Register the route with the updated endpoint name
job_routes.add_url_rule('/job-detail/<int:job_id>', 'job_detail', job_detail)


@job_routes.route('/api/search')
def search():
    # Get the search query from the request URL
    search_query = request.args.get('search')

    try:
        # Fetch job data from the database based on the search query
        jobs = prisma.job.find_many(
            where={'title': {'contains': search_query}})

        # Prepare data for rendering in the HTML template
        job_data = []
        for job in jobs:
            company = job.company
            if company is not None:
                job_data.append({
                    'jobId': job.id,
                    'logo': company.logo if company.logo else '',
                    'title': job.title,
                    'location': job.location,
                    'employmentType': job.employmentType,
                    'salaryRange': job.salaryRange
                })

        # Render the search results page with the search query and job data
        return render_template('search.html', search_query=search_query, jobs=job_data)

    except Exception as e:
        # Log the exception details
        print(f"Error fetching search results: {str(e)}")
        return render_template('error.html'), 500


@job_routes.route('/about')
def about():
    return render_template('about.html')


@job_routes.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')


@job_routes.route('/contact')
def contact():
    return render_template('contact.html')


@job_routes.route('/joblist')
def joblist():
    return render_template('joblist.html')


@job_routes.route("/")
def home():
    # Fetch job data from the database
    jobs = prisma.job.find_many()
    # Render HTML template and pass the job data
    return render_template('index.html', jobs=jobs)


@job_routes.route('/job-detail')
def jobdetail():
    return render_template('job-detail.html')


@job_routes.route('/job-apply')
def jobapply():
    return render_template('job-apply.html')


@job_routes.route('/login')
def login():
    return render_template('login-page.html')
