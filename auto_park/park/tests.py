from django.test import TestCase
from datetime import datetime

# Create your tests here.

date = "2021-10-10T15:20:57Z"


new_date = datetime.replace(date)

print(new_date)
