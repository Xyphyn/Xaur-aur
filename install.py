import requests, json, tarfile, os

class install:
    def __init__(self, package):
        try:
            r = requests.get(f'https://aur.archlinux.org/rpc/?type=info&arg={package}').text
            data = json.loads(r)
            link_to_snapshot = 'https://aur.archlinux.org/' + data['results']['URLPath']
            print(f'Downloading {package}...')
            file_to_download = requests.get(link_to_snapshot)
            file_path = f'/tmp/{package}.tar.gz'
            print(f'Writing {package} to {file_path}...')
            open(file_path, 'wb').write(file_to_download.content)
            file = tarfile.open(file_path)
            print(f'Extracting files to /tmp/{package}...')
            file.extractall(f'/tmp')
            os.chdir(f'/tmp/{package}')
            print(f'Building {package}...')
            os.system('makepkg -si')
        except requests.HTTPError:
            print(f'{package} is not an AUR package!')
