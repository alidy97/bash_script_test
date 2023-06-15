#!/usr/bin/env python3
import sys
import shutil

# Extract the port number
port = sys.argv[1]

# Extract the names of people
names = sys.argv[2:]

# Generate the HTML content
html_content = "<html><body>\n"
for name in names:
    html_content += f"<p>Hello, {name}!</p>\n"
html_content += '<img src="meme.jpg" alt="Meme">\n'
html_content += "</body></html>"

# Write the HTML content to index.html
with open("index.html", "w") as file:
    file.write(html_content)

# Copy the meme image to the same directory
shutil.copyfile("/home/ali/Downloads/meme.jpg", "meme.jpg")

print("index.html and meme.jpg generated successfully!")
