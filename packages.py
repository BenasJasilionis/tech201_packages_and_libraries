# pip and packages

# pip is pythons package manager, allows us to install and manage additional packages
# pip install <package name> in terminal
# if package is still red, click red lightbulb and install through pycharm

import requests

# Can use request.get to get data from a url
request_bbc = requests.get("https://www.google.co.uk")

# status_code -> check if its working 200 = everything is fine
print(request_bbc.status_code)

# .content gets all the content on that specific webpage
print(request_bbc.content)

# Packages are a way of structuring programs so they can be used by other programs