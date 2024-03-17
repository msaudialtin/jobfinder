import bcrypt
from prisma import Client

prisma = Client()
prisma.connect() 

userData = [
    {
        'name': 'Alice',
        'email': 'alice@prisma.io',
        'password': 'password123',
    },
    {
        'name': 'Nilu',
        'email': 'nilu@prisma.io',
        'password': 'qazwsx123',
    },
    {
        'name': 'Mahmoud',
        'email': 'mahmoud@prisma.io',
        'password': 'password456',
    },
]

def seed_companies():
    companies_data = [
        {
            "name": "Company 1",
            "logo": "static/img/com-logo-1.jpg",


        },
        {
            "name": "Company 2",
            "logo": "static/img/com-logo-2.jpg",



        },
        {
            "name": "Company 3",
            "logo": "static/img/com-logo-3.jpg",


        },
        {
            "name": "Company 4",
            "logo": "static/img/com-logo-4.jpg",

        },
        {
            "name": "Company 5",
            "logo": "static/img/com-logo-5.jpg",

        },
        {
            "name": "Company 6",
            "logo": "static/img/com-logo-2.jpg",

        },
        {
            "name": "Company 7",
            "logo": "static/img/com-logo-1.jpg",

        },
        {
            "name": "Company 8",
            "logo": "static/img/com-logo-4.jpg",


        },
    ]

    for company_data in companies_data:
        # Insert company data into the database using Prisma Client
        created_company = prisma.company.create(data=company_data)
        print(f"Company '{created_company.name}' seeded with ID {created_company.id}")

def seed_jobs():
    jobs_data = [
        {
        "title": "Software Engineer",
        "location": "Lagos, Nigeria",
        "employmentType": "Full Time",
        "salaryRange": "N500,000 - N550,000",
        "description": "We are seeking a skilled Software Engineer to join our dynamic team. In this role, you will be responsible for developing, testing, and maintaining high-quality software applications. If you are passionate about technology and enjoy working in a collaborative environment, we would love to hear from you!",
        "responsibilities": "\n".join([
            "Design and implement software solutions",
            "Collaborate with cross-functional teams to define, design, and ship new features",
            "Troubleshoot, debug, and optimize application performance",
            "Stay up-to-date with emerging technologies and industry trends",
        ]),
        "qualifications": "\n".join([
            "Bachelor's degree in Computer Science or related field",
            "Proven experience as a Software Engineer",
            "Proficient in one or more programming languages (e.g., Python, Java, JavaScript)",
            "Strong problem-solving and communication skills",
        ]),
        "companyId": 1
    },
    {
        "title": "Cybersecurity Analyst",
        "location": "Lagos, Nigeria",
        "employmentType": "Full Time",
        "salaryRange": "N500,000 - N700,000",
        "description": "Join our cybersecurity team as a Cybersecurity Analyst and play a crucial role in protecting our organization from cyber threats. As a Cybersecurity Analyst, you will assess security vulnerabilities, implement security measures, and respond to security incidents. If you have a strong understanding of cybersecurity principles and a commitment to keeping data secure, we welcome your expertise!",
        "responsibilities": "\n".join([
            "Conduct regular security assessments and risk analysis",
            "Implement and manage security measures, including firewalls and encryption protocols",
            "Monitor security incidents and respond to breaches",
            "Stay updated on emerging cybersecurity threats and technologies",
        ]),
        "qualifications": "\n".join([
            "Bachelor's degree in Cybersecurity, Information Technology, or related field",
            "Proven experience as a Cybersecurity Analyst",
            "Knowledge of cybersecurity frameworks and standards",
            "Certifications such as CISSP, CompTIA Security+, or CEH are a plus",
        ]),
        "companyId": 2
    },
    {
        "title": "Marketing Manager",
        "location": "Lagos, Nigeria",
        "employmentType": "Full Time",
        "salaryRange": "N150,000 - N250,000",
        "description": "We are looking for an experienced Marketing Manager to join our team. In this role, you will be responsible for developing and executing marketing strategies to drive business growth. If you have a creative mindset and a proven track record in marketing, we want to hear from you!",
        "responsibilities": "\n".join([
            "Develop and implement marketing plans and campaigns",
            "Analyze market trends and competitors to identify opportunities",
            "Manage and coordinate marketing projects and events",
            "Collaborate with cross-functional teams to achieve marketing goals",
        ]),
        "qualifications": "\n".join([
            "Bachelor's degree in Marketing or related field",
            "Proven experience in marketing roles",
            "Excellent communication and interpersonal skills",
            "Creative and strategic thinking",
        ]),
        "companyId": 3
    },
    {
        "title": "Data Scientist",
        "location": "Lagos, Nigeria",
        "employmentType": "Full Time",
        "salaryRange": "N450,000 - N500,000",
        "description": "We are seeking an experienced Data Scientist to join our data analytics team. In this role, you will be responsible for analyzing complex datasets to extract valuable insights and support data-driven decision-making. If you have a strong background in data science and a passion for solving challenging problems, we want to hear from you!",
        "responsibilities": "\n".join([
            "Develop and implement machine learning models",
            "Analyze large datasets to identify trends and patterns",
            "Collaborate with cross-functional teams on data-related projects",
            "Present findings and insights to stakeholders",
        ]),
        "qualifications": "\n".join([
            "Master's or Ph.D. in Data Science, Statistics, or related field",
            "Proven experience as a Data Scientist",
            "Strong programming skills (Python, R, etc.)",
            "Excellent analytical and problem-solving abilities",
        ]),
        "companyId": 4
    },
    {
        "title": "UX/UI Designer",
        "location": "Lagos, Nigeria",
        "employmentType": "Full Time",
        "salaryRange": "N125,000 - N250,000",
        "description": "We are looking for a creative and detail-oriented UX/UI Designer to join our design team. In this role, you will be responsible for creating visually appealing and user-friendly interfaces. If you have a passion for design and a strong portfolio showcasing your work, we would love to hear from you!",
        "responsibilities": "\n".join([
            "Create wireframes, prototypes, and visual designs",
            "Collaborate with product and development teams on design concepts",
            "Conduct user research to inform design decisions",
            "Stay up-to-date with design trends and industry best practices",
        ]),
        "qualifications": "\n".join([
            "Bachelor's degree in Design, HCI, or related field",
            "Proven experience as a UX/UI Designer",
            "Proficiency in design tools (Sketch, Figma, Adobe XD, etc.)",
            "Strong communication and collaboration skills",
        ]),
        "companyId": 5
    },
    {
        "title": "Network Engineer",
        "location": "Lagos, Nigeria",
        "employmentType": "Full Time",
        "salaryRange": "N300,000 - N450,000",
        "description": "We are hiring a skilled Network Engineer to join our IT team. In this role, you will be responsible for designing, implementing, and managing our organization's network infrastructure. If you have a strong background in network administration and enjoy solving technical challenges, we want to hear from you!",
        "responsibilities": "\n".join([
            "Design and implement network solutions",
            "Troubleshoot and resolve network issues",
            "Collaborate with IT teams to ensure network security",
            "Stay informed about industry trends and advancements",
        ]),
        "qualifications": "\n".join([
            "Bachelor's degree in Computer Science or related field",
            "Proven experience as a Network Engineer",
            "Certifications such as CCNA or CCNP are a plus",
            "Excellent problem-solving and communication skills",
        ]),
        "companyId": 6
    },
    {
        "title": "Frontend Developer",
        "location": "Lagos, Nigeria",
        "employmentType": "Full Time",
        "salaryRange": "N250,000 - N455,000",
        "description": "We are seeking a talented Frontend Developer to join our development team. In this role, you will be responsible for implementing user interfaces and enhancing the overall user experience. If you have a passion for web development and a strong portfolio showcasing your skills, we'd love to hear from you!",
        "responsibilities": "\n".join([
            "Develop responsive and user-friendly web interfaces",
            "Collaborate with back-end developers to integrate UI elements",
            "Optimize web applications for maximum speed and scalability",
            "Stay updated on emerging frontend technologies and best practices",
        ]),
        "qualifications": "\n".join([
            "Bachelor's degree in Computer Science or related field",
            "Proven experience as a Frontend Developer",
            "Proficiency in HTML, CSS, and JavaScript",
            "Experience with frontend frameworks (React, Vue, Angular, etc.)",
        ]),
        "companyId": 7
    },
    {
        "title": "HR Manager",
        "location": "Lagos, Nigeria",
        "employmentType": "Full Time",
        "salaryRange": "N200,000 - N450,000",
        "description": "We are looking for an experienced HR Manager to lead our human resources department. In this role, you will be responsible for recruiting, training, and managing the overall well-being of our employees. If you have a strong background in human resources and excellent interpersonal skills, we want to hear from you!",
        "responsibilities": "\n".join([
            "Lead the recruitment and onboarding processes",
            "Develop and implement HR policies and procedures",
            "Handle employee relations and conflict resolution",
            "Ensure compliance with labor laws and regulations",
        ]),
        "qualifications": "\n".join([
            "Bachelor's degree in Human Resources or related field",
            "Proven experience as an HR Manager",
            "Excellent communication and leadership skills",
            "Familiarity with HR software and tools",
        ]),
        "companyId": 8
    },
    ]

    for job_data in jobs_data:
        # Insert job data into the database using Prisma Client
        created_job = prisma.job.create(data=job_data)
        print(f"Job '{created_job.title}' seeded with ID {created_job.id}")
        
# Call the seed_companies() function to populate the database with companies
seed_companies()

# Call the seed_jobs() function to populate the database
seed_jobs()

# # Disconnect from the Prisma client after seeding
# prisma.disconnect()