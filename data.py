import os
import requests
import json
from PIL import Image

file = 'data_request.json'

url = f"https://webhook.site/token/6aea8dca-92b8-4df6-be25-2873fb31dda0"

showcase = int(input('Do you wish the data to be:\n\n'
                     'Printed: press 1\n'
                     'Shown on an image: press 2\n'
                     'To be saved in a txt '
                     'fille: press 3\n'))
response = requests.get(url)
data = response.json()
if showcase == 1:
    print(data)
elif showcase == 2:
    outcome = int(input(('Images are about to be opened, wish to confirm?\n Press 1 to confirm\n Press 2 to exit\n')))
    if outcome == 2:
        exit()
    img = ['devtool.PNG', 'devtool_two.PNG', 'webhook.PNG']
    for i in(img):
        image = Image.open(i)
        image.show()
else:
    with open(file, 'w') as txt:
        json.dump(data,txt)
    print('File saved as: "data_request.json"')
    open_file = input('Do you wish to open the file?\nYes / No\n').lower()
    if open_file == 'yes':
        os.startfile(file)
    else:
        exit()