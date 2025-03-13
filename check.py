from datetime import datetime, timedelta
from convertdate import persian

if __name__ == "__main__":
    today = datetime.today()
    end_date_persian = persian.from_gregorian(today.year, today.month, today.day)
    print(end_date_persian) 