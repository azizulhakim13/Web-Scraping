import requests
from bs4 import BeautifulSoup

url = "https://www.dsebd.org/old_news.php?inst=CITYBANK&criteria=3&archive=news"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# find all the news items and iterate over them
news_items = soup.find_all('div', {'class': 'news-box'})
eps_values = []

for item in news_items:
    # find the EPS value from the news item
    eps_text = item.find(string=lambda text: "EPS was Tk." in text)

    # extract the Quarter, Date, and EPS value
    if eps_text:
        eps_value = eps_text.split("EPS was Tk. ")[1].split()[0]
        quarter = eps_text.split()[0]
        date = eps_text.split()[-1].replace(".", "")

        # if EPS value is negative, add a minus sign
        if eps_value.startswith("("):
            eps_value = "-" + eps_value.strip("()")

        # append the EPS data to the list
        eps_values.append({"Quarter": quarter, "Date": date, "EPS": eps_value})

# print the EPS values for CITYBANK
print(eps_values)
