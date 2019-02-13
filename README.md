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
_# test_
from canvasapi import Canvas
from canvasapi.exceptions import CanvasException
import csv
import time

API_URL = "https://school.instructure.com"
API_KEY = "user access token"

canvas = Canvas(API_URL, API_KEY)
```
