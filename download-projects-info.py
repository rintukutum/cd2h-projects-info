#---------
# Author: Rintu Kutum, Study Coordinator, @ TavLab, ML/AI in Healthcare, IIIT-Delhi
# Date: 02-April-2021
#---------
# CODE TO GET THE PROJECTS FROM 
# N3C Data Enclave Projects
# https://covid.cd2h.org/projects
# https://ncats.nih.gov/news/releases/2020/access-to-N3C-COVID-19-data-analytics-platform-now-open?utm_source=Twitter&utm_medium=Social&utm_campaign=n3c_data_enclave_release

# python 3
#---------
# ESSENTIAL MODULES
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#---------
# FOR LOADING THE COMPLETE DATASET (js code)
#

time.sleep(20) 

url = "https://covid.cd2h.org/projects"

#---------
# CHANGE DRIVER ACCORDINGLY

driver = webdriver.Safari()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', {'id' : 'table'})

project_para = all_divs.find_all('td')

proj_all = []
for i in range(0,len(project_para)):
	tst = project_para[i]
	x2 = tst.find_all('h3')
	proj_title = x2[0].text
	proj_detail = x2[0].next_sibling.strip().replace("\n","")
	proj_lead = tst.find_all('strong')[0].text
	proj_inst = tst.find_all('strong')[1].text
	proj_info = [proj_title, proj_lead, proj_inst, proj_detail]
	print(proj_info)
	proj_all.append(proj_info)

#----------
# write to a file

# open a file to write
outfile = open("data/cd2h-projects.csv", "w")
header = '"' + '","'.join(["proj_title","proj_lead","proj_inst","proj_detail"]) + '"\n'
outfile.write(header)
for i in range(0, len(proj_all)):
	out = '"' + '","'.join(proj_all[i]) + '"\n'
	outfile.write(out)

outfile.close()



