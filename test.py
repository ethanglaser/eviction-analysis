import pandas as pd
import requests
from pprint import pprint
import json
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

url = "https://api.opencagedata.com/geocode/v1/json?q=1403%20Franklin%20St,%20Lafayette,%20IN%2047905&key=6fb685ba1b0d49479b5629ecc1fd569b"
df = pd.read_csv('Book1.csv')

payload = {}
headers= {}

lat = []
lng = []

response = requests.request("GET", url, headers=headers, data = payload)
errors = 0
for address in df['Addresses']:
    print(address)
    if '#' in address:
        address = address.replace('#' + address.split('#')[1].split()[0], '')
    address = address.replace(' ', '%20').replace('IN', 'Indiana')
    print(address)

    url = "https://api.opencagedata.com/geocode/v1/json?q=" + address + "&key=6fb685ba1b0d49479b5629ecc1fd569b"
    response = requests.request("GET", url, headers=headers, data = payload)
    try:
        coords = json.loads(response.text)['results'][0]['geometry']
        pprint(coords)
        lat.append(coords['lat'])
        lng.append(coords['lng'])
    except:
        errors += 1
        lat.append(None)
        lng.append(None)
        print("ERROR")
print(errors)
df['latitude'] = lat
df['longitude'] = lng
print(df)
#plt.scatter(df['longitude'], df['latitude'])
plt.show()
plt.savefig('scat')

K_clusters = range(1,30)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = df[['latitude']]
X_axis = df[['longitude']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
# Visualize
plt.plot(K_clusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()
plt.savefig('elbow')


