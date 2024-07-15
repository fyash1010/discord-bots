import webbrowser

url = 'https://stackoverflow.com/questions/64910874/webbrowser-doesnt-open-new-tabs-in-edge-browser-after-having-it-registered'

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

for x in range(25):
    webbrowser.open(url)
    webbrowser.get('edge').open(url)