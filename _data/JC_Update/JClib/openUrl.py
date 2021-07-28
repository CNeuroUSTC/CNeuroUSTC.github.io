import webbrowser

def openurl(url):
    try:
        webbrowser.get('chrome').open_new_tab(url)
    except Exception as e:
        webbrowser.open_new_tab(url)
