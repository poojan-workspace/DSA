# Advanced datatypes in python:
'''
datetime, time, calendar, date, timedelta, arrow, dateutil, collections
'''

# import arrow

# brewing_time = arrow.utcnow()
# brewing_time.to("Europe/Rome")

from collections import defaultdict
from collections import namedtuple

chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])