# erase lines between the opening <rss> bracket and the first <item> from source wp xml export:
# i.e channel, description, pubDate, language, and any beginning with "wp:", 

# import feedparser
import xml.etree.ElementTree as Xet
import pandas as pd

# data = feedparser.parse('/content/surgicaleducationlearnsurgery.WordPress.2024-07-10.xml')
cols = ["title", "link"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('/content/surged7-12.xml')
root = xmlparse.getroot()

for item in root:
  title = item.find("title").text
  link = item.find("link").text
  rows.append({ "title": title, "link": link })

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output.csv')
