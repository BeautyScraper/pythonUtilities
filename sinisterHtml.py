
import re
import os
import sys


def createSinisterHtml(path, html_file="sinister.htm"):
    with open("template.htm", "r") as temp:
        template = temp.read()
    with open(html_file, "w") as htmFile:
        for filename in os.listdir(path):
            templateAnchor = """<a href="instaLink" title="profileName">
  <img src="MainImage" alt="Forest">
  
</a>"""
            replaceTemplate = """<!--templateLink-->"""
            templateAnchor += replaceTemplate
            sinister_pattern = "(.*?)\((.*?)\)"
            if (re.search(sinister_pattern, filename)):
                profile_name = re.search(sinister_pattern, filename)[1]
                img_code = re.search(sinister_pattern, filename)[2]
                instaLink = "https://www.instagram.com/p/@@/".replace("@@", img_code)
                templateAnchor = templateAnchor.replace("instaLink", instaLink)
                templateAnchor = templateAnchor.replace("MainImage", "file:///" + path + "\\" + filename)
                templateAnchor = templateAnchor.replace("profileName", profile_name)

                template = template.replace(replaceTemplate, templateAnchor)
        htmFile.write(template)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        createSinisterHtml(r"C:\Heaven\Haven\NayaMaal")
        pass
    else:
        pass
