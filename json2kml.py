import simplekml
import json

with open('initiatives_all.json', 'r') as file:
    initiatives_json = file.read()

dict_initiatives = json.loads(initiatives_json)

initiatives_kml = simplekml.Kml()

themes = set()
all_titles = set()
dict_title_coord = {}
dict_title_desc = {}
nb_init = 0
for region in range(len(dict_initiatives)):
    for id in dict_initiatives[region]:
        # print(dict_initiatives[region][id]['theme'])
        initiative = dict_initiatives[region][id]
        themes.add(initiative['theme'])
        if initiative['theme'] in ['Déchets', 'Energies renouvelables']:
            if 'méthan' in initiative['title'].lower():
                title = initiative['title']
                latitude = initiative['location']['latitude']
                longitude = initiative['location']['longitude']
                # print(initiative['body'])
                dict_title_coord[title] = (longitude, latitude)
                dict_title_desc[title] = initiative['body']
                # if title == "Méthanisation IAA Fromagerie Gaugry":
                #     print(latitude)
                #     print(longitude)
                #     print(initiative['body'])
                #     print(initiative['location'])
                if not title in all_titles:
                    all_titles.add(title)
                    nb_init += 1
                #long, lat
# Déchets, Energies renouvelables

for initiative in dict_title_coord:
    pnt = initiatives_kml.newpoint(name=initiative, description=dict_title_desc[initiative], coords=[dict_title_coord[initiative]])
    pnt.style.labelstyle.scale = 0.0001  # Text twice as big
    # pnt.style.labelstyle.color = simplekml.Color.blue


print(nb_init)

initiatives_kml.save('initiatives.kml')
print(themes)
