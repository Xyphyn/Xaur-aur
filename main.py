import requests, sys, install, search

try:
    if str(sys.argv[1]) == 'install':
        pkginstall = install.install(str(sys.argv[2]))
    elif str(sys.argv[1]) == 'search':
        pkgsearch = search.search(str(sys.argv[2]))
except IndexError:
    print('Type [xaur install {packagename}] to install an AUR package, and type [xaur search {packagename}] to search for an AUR package.')
