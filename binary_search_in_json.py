import json

#js = json.loads(input())
#js = json.loads('[{"name": "kvrwxkmqfy", "parents": ["zemrehxvuo", "qzntzflodp", "pjvisgmdrw"]}, {"name": "ogqoyccgkn", "parents": ["ppcmlxqgmn", "titthqeskb"]}, {"name": "uhfdrfrhzx", "parents": ["ogqoyccgkn", "ppcmlxqgmn", "wubwjzolrx", "pjvisgmdrw", "titthqeskb"]}, {"name": "zemrehxvuo", "parents": ["uhfdrfrhzx", "wubwjzolrx", "pjvisgmdrw", "titthqeskb"]}, {"name": "ppcmlxqgmn", "parents": ["pjvisgmdrw", "thceozowkb"]}, {"name": "qzntzflodp", "parents": ["wubwjzolrx", "titthqeskb", "thceozowkb"]}, {"name": "wubwjzolrx", "parents": []}, {"name": "pjvisgmdrw", "parents": []}, {"name": "titthqeskb", "parents": ["wubwjzolrx", "pjvisgmdrw"]}, {"name": "thceozowkb", "parents": ["pjvisgmdrw", "titthqeskb"]}]')
#js = json.loads('[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]')
js = json.loads('[{"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]')

json_dict, top_dict, mas = {}, [], []
for y in js:
    top_dict.append(y['name'])

for x in js:
    for top in x.get('parents'):
        if len(top) > 1:
            if top in json_dict:
                json_dict[top].append(x.get('name'))
            else:
                json_dict[top] = [x.get('name')]
        elif top in json_dict:
            json_dict[top].add(x.get('name'))
        else:
            json_dict[top] = set(x.get('name'))

for top in top_dict:
    if top not in json_dict.keys():
        json_dict[top] = []
# print(json_dict)
# print()
#^^^^^^^^^^^^^^^^^^^^ Ввод данных ^^^^^^^^^^^^^^^^^^^^^^


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in set(graph[start]) - visited:
        dfs(graph, next, visited)
    return visited


#vvvvvvvvvvvvvvvvvvvv Сортировка и вывод vvvvvvvvvvvvvvvvvvvvvvv
rez_dict = {}
for top in json_dict.keys():
#   mas.append(re.sub(r'\'(\w)\'', r'\1', ('%r : %s' % (top, len(dfs(json_dict, top))))))
    rez_dict[top] = len(dfs(json_dict, top))
sorted_x = dict(sorted(rez_dict.items(), key=lambda x: x[0]))
for key, val in sorted_x.items():
    print(str(key) + " : " + str(val))


# '[{"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]'
