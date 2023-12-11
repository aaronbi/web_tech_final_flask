# About
This is the source code for a website for organizing outdoor climbing trips. This project
uses Flask for most of its serverside operations, HTML/CSS for page structure, JS for dynamic elements
of pages, and is deployed using AWS(EC2, gunicorn, nginx, Elastic IPs, Route 53)/Cloudflare.

An EC2 ubuntu instance is running the server using gunicorn and nginx. Elastic Ips and Route 53 are used to redirect the
default public IP over to Cloudflare. Cloudflare acts as a proxy between the AWS IP and the actual domain for the website.
# Link
https://aaronbi.xyz
# Usage
If you want to run this locally, you will need to have some package manager (like pip3) and a python installation.

intall requirements
```pip3 install -r requirements.txt```

run the flask server using python
```python3 flaskServer.py```

# Documentation
## .py files
Most of the server logic and page routing/rendering is handled in ```flaskServer.py```. Each page has its own function
that will request or pass data as needed.

```handleFiles.py``` handles the fetching of data from the .json files in the /files folder. There is also a short __main__ for testing
some of the functionality of the functions.

```initData.py``` was used to create the test data currently stored in /files. The server doesn't actively use any of the functions there. You can
run this file to reset the .json files in case they get corrupted somehow. ```python3 initData.py```
## HTML/CSS/JS
All of the HTML is stored in the /templates folder. Each page has its own .html file. Some of these files also have some JS to dynamically populated
the page based on the saved data it is passed.

All CSS is stored in the /static folder. Each page has its own .css file for styling. There is also a general.css and nav.css file for the overall styling/color
of the website and the navigation bar.

# /files/
Data is stored in the files folder. Each 'trip' will have its own .json file containing all the data about that trip. For more information about the structure of
the json files you can look at ```initData.py``` since that is what was used to generate them.
