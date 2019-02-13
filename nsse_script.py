from canvasapi import Canvas
from canvasapi.exceptions import CanvasException
import csv
import time # time is optional

API_URL = "https://schoool.instructure.com"
API_KEY = "user access token"

canvas = Canvas(API_URL, API_KEY)


def conversation():
    # keep track of successful emails sent
    count = 0

    # keep track of emails not sent due to non-existent user or message send failure
    error_list = []

    # start timer for time elapsed reference (optional)
    start = time.time()

    # replace file name and open file as csc_file
    with open('survey_link_file.csv', newline='') as csv_file:
        # csv library then saves it to reader
        reader = csv.DictReader(csv_file)

        # loop through each record
        for row in reader:
            # all row['item'] need to match column names from csv file
            user = row['SIS_ID']
            fname = row['FIRSTNAME']
            lname = row['LASTNAME']
            survey = row['SURVEYLINK']

            try:
                # find user based on SIS ID and save to student
                student = canvas.get_user(user, 'sis_user_id')
            except CanvasException:
                # if user not found save user to error_list
                error_student = (user + ' - ' + fname + ', ' + lname)
                error_list.append(error_student)
                continue

            try:
                # create conversation/Canvas email
                canvas.create_conversation(
                    # pass in student.id as recipient (only needed the id)
                    recipients=[student.id],
                    # either pass in body message by variable or declare here
                    body='This is the survey link ' + survey,
                    # either pass in subject message by variable or declare here
                    subject='New Test',
                    # set force_new to true to create new message rather than append to existing message.
                    force_new=True
                )
                # increment count by one indicating successful completion
                count += 1
            except TypeError:
                # if conversation was unable to send save user to error_list
                error_student = (user + ' - ' + fname + ', ' + lname)
                error_list.append(error_student)
                continue

        # print successful count, error_list and time (optional) elapsed in seconds
        print('Emails sent successfully: ', count)
        print('There was an error and emails were not sent to: ', error_list)
        end = time.time()
        print('Time elapsed: ', end - start)


conversation()
