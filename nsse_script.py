from canvasapi import Canvas
from canvasapi.exceptions import CanvasException
import csv
import time

API_URL = "https://schoool.instructure.com"
API_KEY = "user api key"

canvas = Canvas(API_URL, API_KEY)


def conversation():
    count = 0
    error_list = []
    start = time.time()
    with open('survey_link_file.csv', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            user = row['SIS_ID']
            fname = row['FIRSTNAME']
            lname = row['LASTNAME']
            survey = row['SURVEYLINK']

            try:
                student = canvas.get_user(user, 'sis_user_id')
            except CanvasException:
                error_student = (user + ' - ' + fname + ', ' + lname)
                error_list.append(error_student)
                continue

            try:
                canvas.create_conversation(
                    recipients=[student.id],
                    body='This is the survey link ' + survey,
                    subject='New Test',
                    force_new=True
                )
                count += 1
            except TypeError:
                error_student = (user + ' - ' + fname + ', ' + lname)
                error_list.append(error_student)
                continue

        print('Emails sent successfully: ', count)
        print('There was an error and emails were not sent to: ', error_list)
        end = time.time()
        print('Time elapsed: ', end - start)


conversation()