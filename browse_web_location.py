import webbrowser

# Import a list of Urls from a file
# Show a list of the Urls
# Open the selected Url

with open('browser_bookmarks.txt','r') as urls:
    urls_contents = urls.read()

def run_browser_url():
    webbrowser.open('http://example.com')

def work_urls_login():
    pass

def import_bookmarks():
    pass

def add_bookmark():
    pass


if __name__ == "__main__":
    print(urls_contents)
