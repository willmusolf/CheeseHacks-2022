import json
from flask import jsonify


def generate_degrees(courses_taken):
    with open('data/majors.json') as f:
        majors = json.load(f)

    with open('data/courses.json') as f:
        courses = json.load(f)

    ls = {
        "Quantitative Reasoning Part A": False,
        "Quantitative Reasoning Part B": False,
        "Ethnic Studies": False,
        "Communication Part A": False,
        "Communication Part B": False,
        "Literature": 0,
        "Humanities": 0,
        "Social Science": 0,
        "Natural Science": 0,
        "Physical Science": 0,
        "Biological Science": 0,
        "B.S. Int./Adv. MATH/STAT/COMP SCI": 0
    }

    for course, credit in courses_taken.items():
        subject = ''

        split_subject = course.split(' ')
        for i, part in enumerate(split_subject):
            if i + 1 < len(split_subject):
                subject += part + ' '

        subject = subject.strip()

        designation = courses[subject]["courses"][course[-3:]]["designation"]

        if designation["Gen Ed"] is not None:
            if "g Part A" in designation["Gen Ed"]:
                ls["Quantitative Reasoning Part A"] = True
            if "g Part B" in designation["Gen Ed"]:
                ls["Quantitative Reasoning Part A"] = True
                ls["Quantitative Reasoning Part B"] = True
            if "n Part A" in designation["Gen Ed"]:
                ls["Communication Part A"] = True
            if "n Part B" in designation["Gen Ed"]:
                ls["Communication Part A"] = True
                ls["Communication Part B"] = True
        if designation["Ethnic Studies"]:
            ls["Ethnic Studies"] = True

        if designation["Breadth"] is not None:
            if "Humanities" in designation["Breadth"] or "Literature" in designation["Breadth"]:
                if "Literature" in designation["Breadth"]:
                    ls["Literature"] += credit
                ls["Humanities"] += credit
            elif "Biological" in designation["Breadth"]:
                ls["Biological Science"] += credit
                ls["Natural Science"] += credit
            elif "Physical" in designation["Breadth"]:
                ls["Physical Science"] += credit
                ls["Natural Science"] += credit
            elif "Social" in designation["Breadth"]:
                ls["Social Science"] += credit

        if subject in ["MATH", "COMP SCI", "STAT"] and designation["Level"] in ["Intermediate", "Advanced"]:
            ls["B.S. Int./Adv. MATH/STAT/COMP SCI"] += credit

    major_progress = {}

    for major, major_courses in majors.items():
        major_progress[major] = 0

        for course, credit in courses_taken.items():
            
            if course in major_courses["courses"]:
                major_progress[major] += credit

    valid_majors = [k for k, v in sorted(major_progress.items(), key=lambda item: item[1], reverse=True)][:6]

    bs = {
        "Literature": 6,
        "Humanities": 12,
        "Social Science": 12,
        "Natural Science": 12,
        "Physical Science": 6,
        "Biological Science": 6,
        "B.S. Int./Adv. MATH/STAT/COMP SCI": 6
    }

    bs_html = ""

    for key, val in ls.items():
        if type(val) == bool:
            bs_html += f'<span class="lsreq">{key}</span> &nbsp;&nbsp;&nbsp; <input type="checkbox" {"checked " if val else " "}onclick="return false;"/><br />'
        else:
            bs_html += f'<span class="lsreq">{key}</span> &nbsp;&nbsp;&nbsp; <span class="{"lsyes" if bs[key] <= val else "lsno"}">{bs[key] if bs[key] <= val else val} / {bs[key]}</span><br />'

    ba = {
        "Literature": 6,
        "Humanities": 12,
        "Social Science": 12,
        "Natural Science": 12,
        "Physical Science": 3,
        "Biological Science": 3
    }

    ba_html = ""

    for key, val in ls.items():
        if type(val) == bool:
            ba_html += f'<span class="lsreq">{key}</span> &nbsp;&nbsp;&nbsp; <input type="checkbox" {"checked " if val else " "}onclick="return false;"/><br />'
        elif key != "B.S. Int./Adv. MATH/STAT/COMP SCI":
            ba_html += f'<span class="lsreq">{key}</span> &nbsp;&nbsp;&nbsp; <span class="{"lsyes" if ba[key] <= val else "lsno"}">{ba[key] if ba[key] <= val else val} / {bs[key]}</span><br />'

    response = {
        "ba": ba_html,
        "bs": bs_html
    }

    for i, major in enumerate(valid_majors):
        response[f"major{i + 1}"] = major
        response[f"major{i + 1}page"] = "https://guide.wisc.edu" + majors[major]["href"]

    return jsonify(response)
