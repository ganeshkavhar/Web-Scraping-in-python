"""
Description: Prints project details of any kickstarter campaign.

Before executing:
    Please copy the URL of the project to project.txt (ONLY 1 URL at a time)
"""

import requests
from lxml import html
import os

def error_reason(issue):
    if issue == "empty file":
        print ("Please enter the correct URL of the kickstarter project in project.txt")
    else:
        print ("INVALID URL or NOT CONNECTED TO THE INTERNET.")

with open("project.txt","r") as project:
    file_size = os.stat("project.txt").st_size
    if file_size > 0:
        url = project.readline().rstrip()
    else:
        error_reason("empty file")
        exit()
    
try:
    project_page = requests.get(url)
except requests.exceptions.RequestException as e:
    error_reason(e)
    exit()

structure = html.fromstring(project_page.content)

creator = str(structure.xpath("/html/body/div[1]/div[1]/div[1]/div[1]/text()")[0]).strip()
title = str(structure.xpath("//span[contains(@class, 'txt-rotate')]/@data-rotate")).strip().replace("['[","").replace("]']","").replace('"','')
skills = str(structure.xpath("//div[contains(@class, 'skill')]//text()")).strip().replace('[','').replace(']','').replace('\'','')
education = []
education.append(str(structure.xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/ul/li[1]//text()")).replace(',','').replace('\\n','').replace('\'','').replace('[','').replace(']','').strip().replace('                              ',', '))
education.append(str(structure.xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/ul/li[2]//text()")).replace(',','').replace('\\n','').replace('\'','').replace('[','').replace(']','').strip().replace('                              ',', '))

print ("CREATOR: "+creator)
print ("TITLE: "+title)
print ("SKILLS: "+skills)
print ("EDUCATION: "+str(education).replace('[','').replace(']',''))