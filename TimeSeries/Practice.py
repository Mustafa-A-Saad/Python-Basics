import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Excels\\aapl_no_dates.csv")

rng = pd.date_range(start="2017-07-01",periods=14,freq="B")
df.set_index(rng,inplace=True)

print(df)

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

ush = CustomBusinessDay(calendar=USFederalHolidayCalendar())

from pandas.tseries.holiday import AbstractHolidayCalendar,Holiday

class myBirthday(AbstractHolidayCalendar):
    rules = {
        Holiday("Tefa's Birthday",day=7,month=7)
    }

customday = CustomBusinessDay(calendar=myBirthday())
