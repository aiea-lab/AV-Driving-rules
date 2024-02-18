import csv
import os
from PyPDF2 import PdfReader
import pandas
import fitz




def extract_location(file_path):
    doc = fitz.open(file_path)
    # Extract text from the first page only
    first_page = doc[0]
    text = first_page.get_text()
    values = text.split("\n")[-20:]

    doc.close()
    i = 0

    # going through the list and finding the index of where the zip code is located
    for x in range(len(values)):
        value = values[x]
        if value.isdigit() and len(value) == 5:
            # print(value)
            i = x
    # returns the zip code and the 5 values before it
    return values[i-4:i+1]



def add_to_csv(data, root_folder_path, filename="data.csv"):

    path_to_csv = os.path.join(root_folder_path, filename)

    with open(path_to_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
    
        # Write the data
        for row in data:
            writer.writerow(row)
            print(f"Added new entry for {row[0]} succesfully!")



def extract_data_from_pdf(pdf_path, pdf):
    pdf_data = []

    reader = PdfReader(pdf_path)
    fields = reader.get_fields()
    # fieldList = ["MANufACTuRERS NAME", "BuSINESS NAME", "VEhICLE YEAR", "MANufACTuRERS NAME", "MANufACTuRERS NAME","MANufACTuRERS NAME",
    #              "MANufACTuRERS NAME","MANufACTuRERS NAME", "Moving","Stopped in Traffic", "Moving", "Stopped in Traffic"]

    location_information = extract_location(pdf_path)
    location_label = ["ADDRESS/LOCATION OF ACCIDENT", "CITY", "COUNTY", "STATE", "ZIP CODE"]


    pdf_data.append(str(pdf))
    pdf_data.append(str(fields["MANufACTuRERS NAME"]['/V'])) if '/V' in fields["MANufACTuRERS NAME"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["BuSINESS NAME"]['/V'])) if '/V' in fields["BuSINESS NAME"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["VEhICLE YEAR"]['/V'])) if '/V' in fields["VEhICLE YEAR"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["MAkE"]['/V'])) if '/V' in fields["MAkE"].keys() else pdf_data.append("N/A") 
    pdf_data.append(str(fields["MODEL"]['/V'])) if '/V' in fields["MODEL"].keys() else pdf_data.append("N/A")
    
    # adding the location, city county, state zipcode
    for value in location_information:
        pdf_data.append(value)

    pdf_data.append(str(fields["Moving"]['/V'])) if '/V' in fields["Moving"].keys() else pdf_data.append("N/A") 
    pdf_data.append(str(fields["Stopped in Traffic"]['/V'])) if '/V' in fields["Stopped in Traffic"].keys() else pdf_data.append("N/A") 
    pdf_data.append(str(fields["Pedestrian"]['/V'])) if '/V' in fields["Pedestrian"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Bicyclist"]['/V'])) if '/V' in fields["Bicyclist"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Other"]['/V'])) if '/V' in fields["Other"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["NuMBER Of VEhICLES INVOLVED"]['/V'])) if '/V' in fields["NuMBER Of VEhICLES INVOLVED"].keys()  else pdf_data.append("N/A")
    pdf_data.append(str(fields["MANufACTuRERS NAME"]['/V'])) if '/V' in fields["MANufACTuRERS NAME"].keys()  else pdf_data.append("N/A")   #Vehicle_damage
    pdf_data.append(str(fields["Rear Bumper"]['/V'])) if '/V' in fields["Rear Bumper"].keys()  else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Rear 1"]['/V'])) if '/V' in fields["Left Rear 1"].keys()  else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Rear 2"]['/V'])) if '/V' in fields["Left Rear 2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Rear 3"]['/V'])) if '/V' in fields["Left Rear 3"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Rear 1"]['/V'])) if '/V' in fields["Right Rear 1"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Rear 2"]['/V'])) if '/V' in fields["Right Rear 2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Rear 3"]['/V'])) if '/V' in fields["Right Rear 3"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Rear Passenger 1"]['/V'])) if '/V' in fields["Left Rear Passenger 1"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Rear Passenger 2"]['/V'])) if '/V' in fields["Left Rear Passenger 2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Rear Passenger 3"]['/V'])) if '/V' in fields["Left Rear Passenger 3"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Rear Passenger 4"]['/V'])) if '/V' in fields["Left Rear Passenger 4"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Rear Passenger 1"]['/V'])) if '/V' in fields["Right Rear Passenger 1"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Rear Passenger 2"]['/V'])) if '/V' in fields["Right Rear Passenger 2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Rear Passenger 3"]['/V'])) if '/V' in fields["Right Rear Passenger 3"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Rear Passenger 4"]['/V'])) if '/V' in fields["Right Rear Passenger 4"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Driver Side 1"]['/V'])) if '/V' in fields["Front Driver Side 1"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Driver Side 2"]['/V'])) if '/V' in fields["Front Driver Side 2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Driver Side 3"]['/V'])) if '/V' in fields["Front Driver Side 3"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Driver Side 4"]['/V'])) if '/V' in fields["Front Driver Side 4"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Passenger Side 1"]['/V'])) if '/V' in fields["Front Passenger Side 1"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Passenger Side 2"]['/V'])) if '/V' in fields["Front Passenger Side 2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Passenger Side 3"]['/V'])) if '/V' in fields["Front Passenger Side 3"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Passenger Side 4"]['/V'])) if '/V' in fields["Front Passenger Side 4"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Front Corner 1"]['/V'])) if '/V' in fields["Left Front Corner 1"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Front Corner 2"]['/V'])) if '/V' in fields["Left Front Corner 2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Left Front Corner 3"]['/V'])) if '/V' in fields["Left Front Corner 3"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Front Corner 1"]['/V'])) if '/V' in fields["Right Front Corner 1"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Front Corner 2"]['/V'])) if '/V' in fields["Right Front Corner 2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Right Front Corner 3"]['/V'])) if '/V' in fields["Right Front Corner 3"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Front Bumper"]['/V'])) if '/V' in fields["Front Bumper"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["MODEL_2"]['/V'])) if '/V' in fields["MODEL_2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["VEhICLE YEAR_2"]['/V'])) if '/V' in fields["VEhICLE YEAR_2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Moving_2"]['/V'])) if '/V' in fields["Moving_2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Stopped in Traffic_2"]['/V'])) if '/V' in fields["Stopped in Traffic_2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Pedestrian_2"]['/V'])) if '/V' in fields["Pedestrian_2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Bicyclist_2"]['/V'])) if '/V' in fields["Bicyclist_2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["Other_2"]['/V'])) if '/V' in fields["Other_2"].keys() else pdf_data.append("N/A")
    pdf_data.append(str(fields["NuMBER Of VEhICLES INVOLVED_2"]['/V'])) if '/V' in fields["NuMBER Of VEhICLES INVOLVED_2"].keys() else pdf_data.append("N/A")
    if '/V' in fields["Autonomous Mode"].keys():
        pdf_data.append("Autonomous Mode")
    else:
        pdf_data.append("Conventional Mode")

    if '/V' in fields["WEATHER A 1"].keys():
        pdf_data.append("Clear")
    elif '/V' in fields["WEATHER B 1"].keys():
        pdf_data.append("Cloudy")
    elif '/V' in fields["WEATHER C 1"].keys():
        pdf_data.append("Raining")
    elif '/V' in fields["WEATHER D 1"].keys():
        pdf_data.append("Snowing")
    elif '/V' in fields["WEATHER E 1"].keys():
        pdf_data.append("Fog/Visibility")
    elif '/V' in fields["WEATHER F 1"].keys():
        pdf_data.append("Other")
    else: pdf_data.append("Wind")

    if '/V' in fields["WEATHER A 2"].keys():
        pdf_data.append("Clear")
    elif '/V' in fields["WEATHER B 2"].keys():
        pdf_data.append("Cloudy")
    elif '/V' in fields["WEATHER C 2"].keys():
        pdf_data.append("Raining")
    elif '/V' in fields["WEATHER D 2"].keys():
        pdf_data.append("Snowing")
    elif '/V' in fields["WEATHER E 2"].keys():
        pdf_data.append("Fog/Visibility")
    elif '/V' in fields["WEATHER F 2"].keys():
        pdf_data.append("Other")
    else: pdf_data.append("Wind")

    if '/V' in fields["LIGHTING A 1"].keys():
        pdf_data.append("Daylight")
    elif '/V' in fields["LIGHTING B 1"].keys():
        pdf_data.append("Dusk/Dawn")
    elif '/V' in fields["LIGHTING C 1"].keys():
        pdf_data.append("Dark w Street-lights")
    elif '/V' in fields["LIGHTING D 1"].keys():
        pdf_data.append("Dark w/o Street-lights")
    else: pdf_data.append("Dark w Non-functioning Street-lights")

    if '/V' in fields["LIGHTING A 2"].keys():
        pdf_data.append("Daylight")
    elif '/V' in fields["LIGHTING B 2"].keys():
        pdf_data.append("Dusk/Dawn")
    elif '/V' in fields["LIGHTING C 2"].keys():
        pdf_data.append("Dark w Street-lights")
    elif '/V' in fields["LIGHTING D 2"].keys():
        pdf_data.append("Dark w/o Street-lights")
    else: pdf_data.append("Dark w Non-functioning Street-lights")

    if '/V' in fields["ROADWAY A 1"].keys():
        pdf_data.append("Dark")
    elif '/V' in fields["ROADWAY B 1"].keys():
        pdf_data.append("Wet")
    elif '/V' in fields["ROADWAY C 1"].keys():
        pdf_data.append("Snowy/Icy")
    else: pdf_data.append("Slippery")

    if '/V' in fields["ROADWAY A 2"].keys():
        pdf_data.append("Dark")
    elif '/V' in fields["ROADWAY B 2"].keys():
        pdf_data.append("Wet")
    elif '/V' in fields["ROADWAY C 2"].keys():
        pdf_data.append("Snowy/Icy")
    else: pdf_data.append("Slippery")

    if '/V' in fields["ROAD CONDITIONS A 1"].keys():
        pdf_data.append("Holes,Deep Rut")
    elif '/V' in fields["ROAD CONDITIONS B 1"].keys():
        pdf_data.append("Loose Material on Roadway")
    elif '/V' in fields["ROAD CONDITIONS C 1"].keys():
        pdf_data.append("Construction on Roadway")
    elif '/V' in fields["ROAD CONDITIONS D 1"].keys():
        pdf_data.append("Construction - Repair Zone")
    elif '/V' in fields["ROAD CONDITIONS E 1"].keys():
        pdf_data.append("Reduced Roadway Width")
    elif '/V' in fields["ROAD CONDITIONS F 1"].keys():
        pdf_data.append("Flooded")
    elif '/V' in fields["ROAD CONDITIONS G 1"].keys():
        pdf_data.append("Other")
    else: pdf_data.append("No unusual conditions")

    if '/V' in fields["ROAD CONDITIONS A 2"].keys():
        pdf_data.append("Holes,Deep Rut")
    elif '/V' in fields["ROAD CONDITIONS B 2"].keys():
        pdf_data.append("Loose Material on Roadway")
    elif '/V' in fields["ROAD CONDITIONS C 2"].keys():
        pdf_data.append("Construction on Roadway")
    elif '/V' in fields["ROAD CONDITIONS D 2"].keys():
        pdf_data.append("Construction - Repair Zone")
    elif '/V' in fields["ROAD CONDITIONS E 2"].keys():
        pdf_data.append("Reduced Roadway Width")
    elif '/V' in fields["ROAD CONDITIONS F 2"].keys():
        pdf_data.append("Flooded")
    elif '/V' in fields["ROAD CONDITIONS G 2"].keys():
        pdf_data.append("Other")
    else: pdf_data.append("No unusual conditions")

    if '/V' in fields["MOVEMENT A 1"].keys():
        pdf_data.append("Stopped")
    elif '/V' in fields["MOVEMENT  B 1"].keys():
        pdf_data.append("Proceeding Straight")
    elif '/V' in fields["MOVEMENT C 1"].keys():
        pdf_data.append("Ran off Road")
    elif '/V' in fields["MOVEMENT  D 1"].keys():
        pdf_data.append("Making Right Turn")
    elif '/V' in fields["MOVEMENT  E 1"].keys():
        pdf_data.append("Making Left Turn")
    elif '/V' in fields["MOVEMENT  F 1"].keys():
        pdf_data.append("Making U turn")
    elif '/V' in fields["MOVEMENT  G 1"].keys():
        pdf_data.append("Backing")
    elif '/V' in fields["MOVEMENT  H 1"].keys():
        pdf_data.append("Slowing/Stopping")
    elif '/V' in fields["MOVEMENT  I 1"].keys():
        pdf_data.append("Passing other Vehicle")
    elif '/V' in fields["MOVEMENT J 1"].keys():
        pdf_data.append("Changing Lanes")
    elif '/V' in fields["MOVEMENT  K 1"].keys():
        pdf_data.append("Parking Manuever")
    elif '/V' in fields["MOVEMENT  L 1"].keys():
        pdf_data.append("Entrering Traffic")
    elif '/V' in fields["MOVEMENT  M 1"].keys():
        pdf_data.append("Other Unsafe Turning")
    elif '/V' in fields["MOVEMENT  N 1"].keys():
        pdf_data.append("Xing into opposing lane")
    elif '/V' in fields["MOVEMENT  O 1"].keys():
        pdf_data.append("Parking")
    elif '/V' in fields["MOVEMENT  P 1"].keys():
        pdf_data.append("Merging")
    elif '/V' in fields["MOVEMENT  Q 1"].keys():
        pdf_data.append("Travelling Wrong Way")
    else: pdf_data.append("Other")

    if '/V' in fields["MOVEMENT A 2"].keys():
        pdf_data.append("Stopped")
    elif '/V' in fields["MOVEMENT  B 2"].keys():
        pdf_data.append("Proceeding Straight")
    elif '/V' in fields["MOVEMENT C 2"].keys():
        pdf_data.append("Ran off Road")
    elif '/V' in fields["MOVEMENT  D 2"].keys():
        pdf_data.append("Making Right Turn")
    elif '/V' in fields["MOVEMENT  E 2"].keys():
        pdf_data.append("Making Left Turn")
    elif '/V' in fields["MOVEMENT  F 2"].keys():
        pdf_data.append("Making U turn")
    elif '/V' in fields["MOVEMENT  G 2"].keys():
        pdf_data.append("Backing")
    elif '/V' in fields["MOVEMENT  H 2"].keys():
        pdf_data.append("Slowing/Stopping")
    elif '/V' in fields["MOVEMENT  I 2"].keys():
        pdf_data.append("Passing other Vehicle")
    elif '/V' in fields["MOVEMENT J 2"].keys():
        pdf_data.append("Changing Lanes")
    elif '/V' in fields["MOVEMENT  K 2"].keys():
        pdf_data.append("Parking Manuever")
    elif '/V' in fields["MOVEMENT  L 2"].keys():
        pdf_data.append("Entrering Traffic")
    elif '/V' in fields["MOVEMENT  M 2"].keys():
        pdf_data.append("Other Unsafe Turning")
    elif '/V' in fields["MOVEMENT  N 2"].keys():
        pdf_data.append("Xing into opposing lane")
    elif '/V' in fields["MOVEMENT  O 2"].keys():
        pdf_data.append("Parking")
    elif '/V' in fields["MOVEMENT  P 2"].keys():
        pdf_data.append("Merging")
    elif '/V' in fields["MOVEMENT  Q 2"].keys():
        pdf_data.append("Travelling Wrong Way")
    else: pdf_data.append("Other")

    if '/V' in fields["TYPE A 1"].keys():
        pdf_data.append("Head-On")
    elif '/V' in fields["TYPE B 1"].keys():
        pdf_data.append("Side Swipe")
    elif '/V' in fields["TYPE C 1"].keys():
        pdf_data.append("Rear End")
    elif '/V' in fields["TYPE D 1"].keys():
        pdf_data.append("Broadside")
    elif '/V' in fields["TYPE E 1"].keys():
        pdf_data.append("Hit Object")
    elif '/V' in fields["TYPE F 1"].keys():
        pdf_data.append("Overturned")
    elif '/V' in fields["TYPE G 1"].keys():
        pdf_data.append("Vehicle/Pedestrian")
    else: pdf_data.append("Other")

    if '/V' in fields["TYPE A 2"].keys():
        pdf_data.append("Head-On")
    elif '/V' in fields["TYPE B 2"].keys():
        pdf_data.append("Side Swipe")
    elif '/V' in fields["TYPE C 2"].keys():
        pdf_data.append("Rear End")
    elif '/V' in fields["TYPE D 2"].keys():
        pdf_data.append("Broadside")
    elif '/V' in fields["TYPE E 2"].keys():
        pdf_data.append("Hit Object")
    elif '/V' in fields["TYPE F 2"].keys():
        pdf_data.append("Overturned")
    elif '/V' in fields["TYPE G 2"].keys():
        pdf_data.append("Vehicle/Pedestrian")
    else: pdf_data.append("Other")

    if '/V' in fields["OTHER A YES"].keys():
        pdf_data.append("CVC Sections Violated")
    elif '/V' in fields["OTHER A NO"].keys():
        pdf_data.append("CVC Sections Not Violated")
    elif '/V' in fields["OTHER B"].keys():
        pdf_data.append("Vision Obscured")
    elif '/V' in fields["OTHER C"].keys():
        pdf_data.append("Inattention")
    elif '/V' in fields["OTHER D"].keys():
        pdf_data.append("Stop and Go Traffic")
    elif '/V' in fields["OTHER E"].keys():
        pdf_data.append("Entering/Leaving Traffic")
    elif '/V' in fields["OTHER F"].keys():
        pdf_data.append("Previous Collision")
    elif '/V' in fields["OTHER G"].keys():
        pdf_data.append("Unfamiliar w Road")
    elif '/V' in fields["OTHER H YES"].keys():
        pdf_data.append("Defective with Equipment")
    elif '/V' in fields["OTHER H NO"].keys():
        pdf_data.append("Not Defective with Equipment")
    elif '/V' in fields["OTHER I"].keys():
        pdf_data.append("Uninvolved Vehicle")
    elif '/V' in fields["OTHER J"].keys():
        pdf_data.append("Other")
    elif '/V' in fields["OTHER K"].keys():
        pdf_data.append("None Apparent")
    elif '/V' in fields["OTHER L"].keys():
        pdf_data.append("Runaway Vehicle")
    else: pdf_data.append("N/A")


    return pdf_data

root_folder_path = os.getcwd()
print("The current directory is: " + str(root_folder_path))

downloaded_folder_name =  "CA_accident_reports" #Download this folder in the root
folder_with_reports_path = os.path.join(root_folder_path, downloaded_folder_name)
print("The path for reports directory is: " + str(folder_with_reports_path))

data = [["File ID", "Vehicle 1 Manufacturer", "Vehicle 1 Business Name", "Vehicle 1 Year of Manufacturing", 
    "Vehicle 1 Make", "Vehicle 1 Model", "Location of Accident", "City of Accident", "County of Accident", 
    "State of Accident", "ZIPCODE of Accident", "Vehicle 1 was Moving", "Vehicle 1 was Stopped in Traffic", 
    "Pedestrian Involved in Accident (w V1)", "Bicyclist involved in Accident (w V1)", "Any other involved entity (w V1)", 
    "Number of Vehicles involved in Accident (w V1)", "Vehicle Damage" ,"RB" ,"LR1", "LR2", "LR3", "RR1", "RR2","RR3", 
    "LRP1", "LRP2", "LRP3", "LRP4", "RRP1", "RRP2", "RRP3", "RRP4", "FDS1", "FDS2", "FDS3", "FDS4", "FPS1", "FPS2", 
    "FPS3", "FPS4", "LFC1", "LFC2", "LFC3", "RFC1", "RFC2", "RFC3", "FB", "Vehicle 2 Model", "Vehicle 2 Year of Manufacturing", 
    "Vehicle 2 was Moving", "Vehicle 2 was Stopped in Traffic", "Pedestrian Involved in Accident (w V2)", 
    "Bicyclist involved in Accident (w V2)", "Any other involved entity (w V2)", "Number of Vehicles involved in Accident (w V2)", 
    "Car Mode", "Weather Vehicle 1", "Weather Vehicle 2", "Lighting Vehicle 1", "Lighting Vehicle 2", "Roadway Surface Vehicle 1", 
    "Roadway Surface Vehicle 2", "Roadway Conditions Vehicle 1", "Roadway Conditions Vehicle 2", "Movement Preceding Collision Vehicle 1", 
    "Movement Preceding Collision Vehicle 2", "Type of Collison Vehicle 1","Type of Collison Vehicle 2", "Other Factors"]]
print("The length of the data is: " + str(len(data[0])))

# Iterate through files in the folder
for folder_year in os.listdir(folder_with_reports_path):
    folder_year_path = os.path.join(folder_with_reports_path, folder_year)
    print("The path to the folder year is " + str(folder_year_path))
    if "Reports_from" in str(folder_year_path):
        for pdf in os.listdir(folder_year_path):
            if pdf != ".DS_Store":
                print("We are looking at : " + str(pdf))
                pdf_path = os.path.join(folder_year_path, pdf)
                print("Path to pdf is " + str(pdf_path))
                new_row = extract_data_from_pdf(pdf_path, pdf)
                print("We are extracting new row")
                data.append(new_row)
                print("We appended new row!")
   
# print("We have data as: ")
# print(data)
                
add_to_csv(data, root_folder_path)

