import requests
from bs4 import BeautifulSoup
import csv

# Set the search parameters for the job listings
keywords = 'python'
location = ''

# Construct the URL for the search results page
url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keywords}&txtLocation={location}'

# Send a GET request to the URL and get the page content
page = requests.get(url).content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page, 'html.parser')

# Find all the job listings on the page
job_listings = soup.find_all('li', {'class': 'clearfix job-bx wht-shd-bx'})

# Create a CSV file to store the extracted data
with open('job_listings.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Write the header row to the CSV file
    writer.writerow(['Company', 'Skills Required', 'Posted'])

    # Loop through each job listing and extract the relevant data
    for job in job_listings:
        # Get the company name
        company = job.find('h3', {'class': 'joblist-comp-name'}).text.strip()

        # Get the skills required
        skills = job.find('span', {'class': 'srp-skills'}).text.strip()

        # Get the posted date
        posted_date = job.find('span', {'class': 'sim-posted'}).text.strip()

        # Write the data for the job listing to the CSV file
        writer.writerow([company, skills, posted_date])
