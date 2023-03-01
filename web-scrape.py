from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
# print(html_text)

# ########## for single search
# soup = BeautifulSoup(html_text, 'lxml')
# job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
# skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
# publish_date = job.find('span', class_ = 'sim-posted').span.text
# print(publish_date) 
# print(skills)
# print(company_name)

# print(f'''
# Company Name: {company_name}
# Required Skills: {skills}
# Publish Date: {publish_date}
# ''')

# ######### for all jobs
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in (jobs):
    publish_date =  job.find('span', class_ = 'sim-posted').span.text 
    if 'today' in publish_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']

        print(f"Company Name: {company_name.strip()}")
        print(f"Skills Needed: {skills.strip()}")
        print(f"More Info: {more_info}")
        print(f"Publish Date: {publish_date}")

        print("")