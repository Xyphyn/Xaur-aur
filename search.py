import requests, json, ANSI

class search:
    def __init__(self, package):
        r = requests.get(f'https://aur.archlinux.org/rpc/?type=search&sb=p&SO=a&by=name-desc&arg={package}').text
        dict = json.loads(r)
        for i in range(len(dict['results'])):
            print(ANSI.ANSI.color_text(35) + 'aur/' + ANSI.ANSI.style_text(36) + ANSI.ANSI.style_text(1) + dict['results'][i]['Name'])
            print(ANSI.ANSI.style_text(0) + ANSI.ANSI.color_text(30) + dict['results'][i]['Description'])
            print()
