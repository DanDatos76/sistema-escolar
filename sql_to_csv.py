import pandas as pd
import sqlite3
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import csv
import pandas as pd
import sqlite3
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#conn = sqlite3.connect(r"macri2810.db")

'''
conn.text_factory = str ## my current (failed) attempt to resolve this
cur = conn.cursor()
data = cur.execute("SELECT * FROM sentimiento")

f = open('output.csv', 'w')
print (f, "unix", "tweet", "sentimiento")
for row in data:
  print >> f, row
f.close()
'''

import pandas as pd

conn = sqlite3.connect("macri2810.db", isolation_level=None,detect_types=sqlite3.PARSE_COLNAMES)
db_df = pd.read_sql_query("SELECT * FROM sentimiento", conn)
db_df.to_csv('messi.csv', index=False)


df = db_df
print(df)
df.to_csv('macri2810.csv', index=False)