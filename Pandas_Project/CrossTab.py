import numpy as np
import pandas as pd

df = pd.read_excel("Excels\\survey.xls")
print(df)

# Crosstab: Frequency distribution of handedness by nationality
print(pd.crosstab(df.Nationality, df.Handedness)) # ( whats represented on X (rows) , represent on y (columns) )

# Frequency distribution of handedness by sex
print(pd.crosstab(df.Sex, df.Handedness))

#  Frequency distribution of handedness by sex and nationality with margins
print(pd.crosstab(df.Sex, [df.Nationality, df.Handedness], margins=True))

# Frequency distribution of handedness by sex and nationality with margins
print(pd.crosstab([df.Sex, df.Nationality], df.Handedness, margins=True))

# Percentage distribution of handedness by sex
print(pd.crosstab(df.Sex, df.Handedness, normalize="index")) # normalize here to get percentage %

# Average age of respondents by sex and handedness
print(pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average))
