import requests
import io

encoding = 'utf-8' ##To support emojis

def updateParams(alist, key, value):
    return [(k,v) if (k != key) else (key, value) for (k, v) in alist]

headers = {
    'Host': 'api-v2.soundcloud.com',
    'User-Agent': 'Mozilla/5.0 Gecko/20100101 Firefox/54.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Authorization': '##insert oauth token here##', ###this comment is here to grab attention
    'Referer': 'https://soundcloud.com/',
    'Origin': 'https://soundcloud.com',
    'Connection': 'keep-alive',
}

params = (
    ('offset', '0'),
    ('q', '#Dubstep'),
    ('facet', 'genre'),
    ('limit', '100'),
    ('app_version', '1501060039'),
)

offset = 0

for i in range(100):
	
	response = requests.get('https://api-v2.soundcloud.com/search/tracks', headers=headers, params=params)
	
	data = response.json()
	
	with io.open('dubstepArtists.txt', 'a', encoding=encoding) as f:
		for j in range(100):
			f.write(data["collection"][j]["user"]["username"] + '\n')
	
	offset += 100
	
	params = updateParams(params, 'offset', offset)