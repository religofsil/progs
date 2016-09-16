from apiclient.discovery import build

service = build("customsearch", "v1",
                developerKey="AIzaSyCVuQB4cvNRYJgmE7nHLwYxFE25fDLL5p4")

res = service.cse().list(
    q='face',
    cx='http://imgur.com',
    searchType='image',
    num=3,
    imgType='photo',
    fileType='png'
).execute()

if not 'items' in res:
    print('No result !!\nres is: {}'.format(res))
else:
    for item in res['items']:
        print('{}:\n\t{}'.format(item['title'], item['link']))
