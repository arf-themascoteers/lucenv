import os
from io import StringIO
import re


def extract_id(filename):
    pattern = "[0-9]+"
    x = re.findall(pattern, filename)
    if len(x) == 0:
        return None
    return int(x[0])


source = "data/rr"

for f in os.listdir(source):
    file = os.path.join(source, f)
    the_id = extract_id(file)
    fhandle = open(file, "r", encoding="utf8")
    content = fhandle.read()
    search_text = "See files sources.txt and stations.txt for more info."
    index = content.find(search_text)
    start = index + len(search_text)
    csv_content = content[start:]
    csv_content = csv_content.strip()
    out_file = f"data/csvs/{the_id}.csv"
    out = open(out_file,"w")
    csv_content_io = out.write(csv_content)
    out.close()
    fhandle.close()


