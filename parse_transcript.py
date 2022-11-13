from PyPDF2 import PdfReader
from flask import jsonify
import os


def parse_transcript():
    reader = PdfReader('transcript.pdf')

    transcript = ''

    for page in reader.pages:
        transcript += page.extractText()

    lines = transcript.split('\n')

    courses = {}

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isnumeric():
                try:
                    if line[j - 1] != ' ' or line[j + 3] != ' ' \
                            or not line[j + 1].isnumeric() or not line[j + 2].isnumeric():
                        break

                    attemptedPassed = False
                    credit = -1

                    for k, char2 in enumerate(line):
                        if line[k] == '.':
                            if attemptedPassed:
                                credit = int(line[k - 1])
                                break
                            attemptedPassed = True

                    if credit == -1:
                        nextLine = lines[i + 1]

                        for k, char2 in enumerate(nextLine):
                            if nextLine[k] == '.':
                                if attemptedPassed:
                                    credit = int(nextLine[k - 1])
                                    break
                                attemptedPassed = True

                    if credit > 0:
                        course_name = ''

                        for part in line[:j + 3].split(' '):
                            if part.isalpha() or part.isnumeric():
                                course_name += part + ' '

                        courses[course_name.strip()] = credit

                except IndexError:
                    continue

    os.remove('transcript.pdf')

    if courses:
        return courses

    return jsonify({'status': 'invalid pdf'})
