# prep xml file: erase lines between the opening <rss> bracket and the first <item> from source:
# i.e channel, description, pubDate, language, and any beginning with "wp:", 

import xml.etree.ElementTree as Xet
import pandas as pd

cols = ["title", "link"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('PATH_TO_XML_FILE')
root = xmlparse.getroot()

for item in root:
  title = item.find("title").text
  link = item.find("link").text
  rows.append({ "title": title, "link": link })

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output.csv')
