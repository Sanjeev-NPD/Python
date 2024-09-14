import requests

API_KEY = 'YOUR_API_KEY'  # Replace with your API key or token

def search_job_listings(query):
    url = 'https://api.example.com/jobs'  # Replace with actual job listings API endpoint
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    params = {
        'query': query,
        'location': 'Your Location',  # Optional
        'count': 200  # Number of results to fetch
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        jobs = response.json()
        for job in jobs.get('results', []):
            print(f"Job Title: {job.get('title', 'N/A')}")
            print(f"Company: {job.get('company', 'N/A')}")
            print(f"Location: {job.get('location', 'N/A')}")
            print(f"Description: {job.get('description', 'N/A')}")
            print()
    else:
        print("Failed to retrieve job listings.")

search_job_listings("Field Sales Executive")    # you can mention any job profile here for which you are searching



# How make this code working: 

# To get your LinkedIn API key, you can do the following:
# Go to the LinkedIn Developers site  : https://developer.linkedin.com/
# Select Create Application
# Fill out the form with your company name, description, logo, and contact information
# Accept the terms and conditions
# Click Submit 