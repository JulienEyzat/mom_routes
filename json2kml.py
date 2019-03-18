import simplekml
import json

with open('initiatives_all.json', 'r') as file:
    initiatives_json = file.read()

dict_initiatives = json.loads(initiatives_json)
initiatives_kml = simplekml.Kml()


themes = set()
for region in range(len(dict_initiatives)):
    for id in dict_initiatives[region]:
        # print(dict_initiatives[region][id]['theme'])
        themes.add(dict_initiatives[region][id]['theme'])
        if dict_initiatives[region][id]['theme'] in ['Déchets', 'Energies renouvelables']:
            if 'méthan' in dict_initiatives[region][id]['title'].lower():
                title = dict_initiatives[region][id]['title']
                latitude = dict_initiatives[region][id]['location']['latitude']
                longitude = dict_initiatives[region][id]['location']['longitude']
                if title == "Méthanisation VIN Cave Coopérative La Courtoise":
                    print(latitude)
                    print(longitude)
                initiatives_kml.newpoint(name=title, coords=[(longitude,latitude)])
                #long, lat
# Déchets, Energies renouvelables



initiatives_kml.save('initiatives.kml')
print(themes)
