from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # tags = soup.find('h5')
    # print(tags)
    course_html_tags = soup.find_all('h5')
    for course in course_html_tags:
        print(course.text)