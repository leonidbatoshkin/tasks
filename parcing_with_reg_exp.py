import requests, re
from itertools import groupby
url = "http://pastebin.com/raw/7543p0ns"
res_of_url = requests.get(url)
text = res_of_url.text
s = ''
with open('C:\\Users\\Leonid\\Desktop\\sites in alphabet.html', 'r') as f:
    for line in f:
        line = line.strip()
        s += line + '\n'
#print(s)

#url = input().strip()
res_of_url = requests.get(url)
match = re.findall(r'<a .*href=[\'"](\w+://)*(\w[\w.\-]+).+', s)
sorted_match = sorted(match)
group_match = [el for el, _ in groupby(sorted_match)]
sorted_sites = sorted(group_match, key=lambda x: x[0])
for x in sorted_sites:
    print(x, end='\n')