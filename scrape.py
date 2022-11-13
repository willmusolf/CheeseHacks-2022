import json
from bs4 import BeautifulSoup
import requests
from flask import jsonify


def get_courses():
    courses_dict = {}
    courses_soup = BeautifulSoup(requests.get("https://guide.wisc.edu/courses/").content, "html.parser")
    courses_links_soup = courses_soup.find_all('li')
    course_hrefs = []

    for link in courses_links_soup:
        if link.find_next('a') is not None:
            link = link.find_next('a')
            href = link.get('href')
            if href is not None and '/courses/' != href and '/courses/' in href and '/courses/courses' not in href:
                subject_name = link.text.split('(')[0].strip()
                course_hrefs.append([subject_name, href])
    for subject_info in course_hrefs:
        subject_name = subject_info[0]
        href = subject_info[1]
        phrases = href[9:-1].split('_')
        subject = ""

        for phrase in phrases:
            subject += phrase + " "

        subject = subject.strip().upper()

        courses_dict[subject] = {
            "subject": subject_name,
            "courses": {}
        }
        link = "https://guide.wisc.edu/" + href
        soup = BeautifulSoup(requests.get(link).content, "html.parser")

        if soup.find_all("div", class_="courseblock") is not None:
            names = soup.find_all("div", class_="courseblock")

            for name in names:
                if name is not None:
                    if name.find_next("p", class_="courseblockcredits") is not None:
                        credits = name.find_next("p", class_="courseblockcredits").text
                        if credits[2] == 'c':
                            if credits[0] != " ":
                                credits = [int(credits[0])]
                        else:
                            if credits[0] != " " and credits[2] != " ":
                                credits = [int(credits[0]), int(credits[2])]

                        ps = name.find_all_next('p', class_="courseblockextra")

                        for p in ps:
                            if p.find_next("span", class_="cbextra=label").find_next("strong").find_next(
                                    "strong") is not None and p.find_next("span", class_="cbextra=label").find_next(
                                "strong").find_next("strong").text == "Course Designation: ":
                                course_designation = [designation for designation in
                                                      p.find_next("span", class_="cbextra-data").contents if
                                                      getattr(designation, 'name', None) != 'br']

                                for i in range(len(course_designation)):
                                    course_designation[i] = course_designation[i].text.replace("\u00a0", " ").replace(
                                        "\u200b", " ").replace("\u2014", "-")

                                designation_dict = {
                                    "Breadth": None,
                                    "Level": None,
                                    "Gen Ed": None,
                                    "Ethnic Studies": False
                                }

                                for designation in course_designation:
                                    if "Breadth" in designation:
                                        designation_dict["Breadth"] = designation[designation.index("-") + 2:]
                                    elif "Level" in designation:
                                        designation_dict["Level"] = designation[designation.index("-") + 2:]
                                    elif "Gen Ed" in designation:
                                        designation_dict["Gen Ed"] = designation[designation.index("-") + 2:]
                                    elif "Ethnic St" in designation:
                                        designation_dict["Ethnic Studies"] = True

                                break

                        if name.find_next('span', class_="courseblockcode") is not None and name.find_next("span",
                                                                                                           class_="cbextra-data") is not None:
                            courses_dict[subject]["courses"][
                                name.find_next('span', class_="courseblockcode").text[-3:]] = {
                                "credits": credits,
                                "requisites": name.find_next("span", class_="cbextra-data").text.replace("\u00a0",
                                                                                                         " ").replace(
                                    "\u200b", " ").replace("\u2014", "-"),
                                "designation": designation_dict
                            }

    return courses_dict


def get_majors():
    soup = BeautifulSoup(requests.get("https://guide.wisc.edu/undergraduate/#majorscertificatestext").content,
                         "html.parser")

    links_soup = soup.find_all("li")

    major_hrefs = []

    for link in links_soup:
        if link.find("a") is not None:
            link = link.find("a").get("href")
            if "/undergraduate" in link:
                slashes = 0
                for char in link:
                    if char == '/':
                        slashes += 1
                if slashes > 3: major_hrefs.append(link)

    majors_dict = {}

    for href in major_hrefs:
        parts_of_href = href.split('/')

        if parts_of_href[2] != "letters-science":
            continue

        link = "https://guide.wisc.edu" + href + "#requirementstext"
        soup = BeautifulSoup(requests.get(link).content, "html.parser")
        name = soup.find('h1', class_="page-title").text

        split_name = name.split(',')
        name = ''
        cert = False
        for i, part in enumerate(split_name):

            if i + 1 < len(split_name):
                name += part + ', '
            elif part == ' Certificate':
                cert = True
        if cert: continue

        name = name[:-2]

        try:
            majors_dict[name]
            continue
        except KeyError:
            pass

        tables = soup.find_all('table')
        courses = []

        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                for a in row.find_all('a'):
                    course_name = a.text.replace("\u00A0", " ").replace("/\u200b", "/").replace("\u00a0", " ")
                    if course_name not in courses:
                        course_name_split = course_name.split(' ')

                        course_name = ''

                        for i, word in enumerate(course_name_split):
                            course_name += word + ' '

                        course_name = course_name.strip()

                        if course_name.isnumeric():
                            split_course = courses[-1].split(' ')

                            subject = ''

                            for i, word in enumerate(split_course):
                                if i + 1 < len(split_course):
                                    subject += word + ' '

                            course_name = subject + course_name
                        elif len(course_name) == 4 and course_name[-3:].isnumeric():
                            split_course = courses[-1].split(' ')

                            subject = ''

                            for i, word in enumerate(split_course):
                                if i + 1 < len(split_course):
                                    subject += word + ' '

                            course_name = subject + course_name[-3:]
                        if course_name[-3:].isnumeric():
                            courses.append(course_name)

        majors_dict[name] = {
            "href": href,
            "courses": courses,
            "image": 'https://guide.wisc.edu/' + soup.find_all('img')[1]['src']
        }

    return majors_dict


def scrape():
    print("Scraping initiated.")

    majors = get_majors()
    courses = get_courses()

    with open('data/courses.json', 'w') as f:
        json.dump(courses, f)

    with open('data/majors.json', 'w') as f:
        json.dump(majors, f)

    return jsonify({"status": "success"})


if __name__ == '__main__':
    scrape()
