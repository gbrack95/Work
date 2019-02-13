# NSSE Survey Script

This script was created to send individualized Canvas emails to students for the NSSE survey.

## Installation

Use the package manager pip to install the [CanvasAPI](https://canvasapi.readthedocs.io/en/latest/) library needed to execute the script.
```bash
pip install canvasapi
```

## Setup

To set it up, you need to create an access token with admin level privileges:
1. Log in to Canvas with user that has admin level privileges.

2. Select "Account" from the left navigation bar, then select "Settings" from the pop up menu.

3. Scroll down to the bottom of the "Approved Integrations" section and just above the "Feature Options" section, click the red "+ New Access Token" button. You will then fill out the "New Access Token" popup window.

    * The "Purpose" field is simply a reminder name for yourself about what the token is used for.

    * The "Expires" field is a date for when you want the token to expire, after which you will need to generate a new one. It is always the best practice to regenerate tokens as soon as possible.

4. Once the popup is filled out click the "Generate Token" button. Make sure to copy the token from the following "Access Token Details" popup, since once this popup is closed you cannot retrieve the token, you will have to generate a new one.

5. You will insert the copied access token and the full school Canvas URL into the script, then initiate a new Canvas object:

```python
# Import the Canvas class, Canvas Exceptions, csv and time(optional)
from canvasapi import Canvas
from canvasapi.exceptions import CanvasException
import csv
import time

# Institutions fully qualified domain name as Canvas API URL
API_URL = "https://school.instructure.com"
# Previously copied user access token as Canvas API Key
API_KEY = "user access token"

# Initiate a new Canvas object
canvas = Canvas(API_URL, API_KEY)
```

6. You will need to prepare a csv file that contains the SIS ID, first name, last name and unique survey link for every student the message is intended for.

7. You will need to adjust the naming convention to reflect that of your file and previously specified columns so the script knows what to look for:

```python
# Change 'survey_link_file.csv' to the name of the csv file saved from step 6
with open('survey_link_file.csv', newline='') as csv_file:

# Change 'SIS_ID' to the column name for the SIS ID numbers column
user = row['SIS_ID']

# Change 'FIRSTNAME' to the column name for the first name column
fname = row['FIRSTNAME']

# Change 'LASTNAME' to the column name for the last name column
lname = row['LASTNAME']

# Change 'SURVEYLINK' to the column name for the unique survey link column
survey = row['SURVEYLINK']
```

8. Finally, you will need to change to content of the message you want to be sent: (*note only change the body and subject*)

```python
# Edit or replace the message in the body to reflect what is to be sent
# Then pass in the survey link from the variable saved above called 'survey'
body='This is the survey link ' + survey,

# Edit or replace the message in the subject to reflect what is to be sent
subject='New Test',
```

## How it Works

1. The script opens the csv file and reads the contents line by line.

2. One line at a time, it pulls the SIS ID and does and API call to Canvas to check their existence. If the user does not exist, it will save them to an error list and move on.

3. If the user exists it will then create an individual Canvas email which will include the body and subject message that is to be sent. If the Canvas email was unable to be created the user will be saved to an error list and the it will move on to the next user.

4. Once the script has repeated this process for every record in the csv file, it will print the count of successful emails, the list of error users and the time elapsed in seconds. This is all for reference and verification. 
