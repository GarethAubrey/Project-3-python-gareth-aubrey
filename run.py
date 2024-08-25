import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Work_hours')

def get_actual_data():
    """
    Get hours worked (actual) data fom user
    """
    print("Please enter number of hours worked by each employee.")
    print("Data should be 10 numbers, seperated by commas")
    print("Example: 12,8,6,0,0,0,12,8,6,0\n")

    hours_worked = input("Enter hours here:")
    print(f"Hours provided are {hours_worked}")

    actual_data = hours_worked.split(",")
    validate_data(actual_data)

def validate_data(values):
    """
    Inside the try, converts all string values into float.
    Raises valueError if strings cannot be converted into float,
    or if there isn't the correct amount of values (10)
    """
    try:
        if len(values) != 10:
            raise ValueError(
                f"Exactly 10 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")        

get_actual_data()