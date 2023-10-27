#Code to download the PDF's of CA DMV Reports 

import requests
from bs4 import BeautifulSoup
import os

# CA DMVs URL
url = "https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-collision-reports/"
 
# request URL and get response object
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
 
#deciding years to download, if you want more - append to the list
years = [2023]

#get current path and make a new folder with the name of the year
current_path = str(os.getcwd())

#make new folder for each year
for year in years:
    try:
        folder_name = 'Reports_from_' + str(year)
        os.mkdir(folder_name)
    except FileExistsError:
        print("Folder with name: " + folder_name + " already exists.")
        ans = input("Would you like to delete the existing folder? (y or n)")
        if ans.upper() == "Y":
            if os.path.isfile(folder_name):
                os.rmdir(folder_name)




# From all links check for year-pdf in link and if present download file

for year in years:
    
    pdf_id = str(year) + '-pdf'
    file_path = current_path + '/Reports_from_' + str(year) +'/'

    for link in links:

        if (pdf_id in link.get('href', [])):

            complete_link = link.get('href', [])
            file_name = complete_link.split("file/")[1]
            file_name = file_name[0:len(file_name)-5]
            print("Downloading file: ", file_name)
    
            # Get response object for link
            response = requests.get('https://www.dmv.ca.gov/'+ link.get('href'))
    
            # Write content in pdf file in a new file in the year folder
            pdf = open(file_path+str(file_name)+".pdf", 'wb')
            pdf.write(response.content)
            pdf.close()
            print("File " + file_name + " downloaded")

    
    print("All PDF from year " + str(year) + " files downloaded!")
 
