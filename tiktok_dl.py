from bs4 import BeautifulSoup
import requests
import os


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}

def createdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

file = input('Enter file name for tiktok page html: ')
username = input('Enter the username: ')
soup = BeautifulSoup(open(file, 'rb'), 'lxml')
videos = [x['href'] for x in soup.find_all('a', {'class': 'jsx-1792501825 video-feed-item-wrapper'})]
print('Found {} videos!'.format(len(videos)))

createdir(username)

for y, x in enumerate(videos):
    print('Downloading {} of {}...'.format(y, len(videos)))
    if not os.path.isfile(username + '/{}{}.mp4'.format(username, y)):
        r = requests.get(x, headers=headers)
        link = BeautifulSoup(r.content, 'html5lib').find('video', {'class': 'jsx-3382097194 video-player'})
        if link is None:
            link = BeautifulSoup(r.content, 'html5lib').find('video', {'class': 'jsx-3382097194 horizontal video-player'})
        open(username + '/{}{}.mp4'.format(username, y), 'wb').write(requests.get(link['src']).content)


