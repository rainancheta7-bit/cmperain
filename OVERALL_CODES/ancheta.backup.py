
#ANSWER
charList = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9',  " ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
"-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"',
",", "<", ".", ">", "/", "?", "\\", "|", "`", "~"]

key = 45
inputMessage = "My Pin Number is 0123456789"
outputMessage = ""
indexCounter = 0

for letter in inputMessage:
    indexCounter = charList.index(letter)
    print(indexCounter)
    outputMessage = outputMessage + charList[(indexCounter + key) % len(charList)]
print(outputMessage)

inputMessage = ""

for letter in outputMessage:
    indexCounter = charList.index(letter)
    print(indexCounter)
    outputMessage = outputMessage + charList[(indexCounter - key) % len(charList)]
print(inputMessage)

letter = input("Please input the letter: ")
pos = charList.index(letter)
print(pos)
#pos1 = charList.index(pos + key)

#demo
import subFile

@@ -752,5 +788,356 @@
student = subFile.Students(name="mokong", grade=1.0, subject="Python")
student.print_student_info_method()

#DEMO22

import math

def get_capacitance_by_cv(charge, voltage):
    capacitance = charge / voltage
    print(f"Capacitance is{capacitance} farad")
    return capacitance

def get_capacitance_material(permittivity, relative_permittivity, area, distance):
    capacitance = (permittivity * relative_permittivity * area) / distance
    print(f"Capacitance is{capacitance} farad")
    return capacitance

def get_capacitive_reactance(frequency, capacitance):
    reactance = 1 / (2 * math.pi * frequency * capacitance)
    print(f"Capacitive reactance is{reactance} ohms")
    return reactance

if __name__ == "__main__":
    get_capacitance_by_cv(10,10)
######################################################3

import math

def get_inductance_material (permeability, relativep, turns, area, length):
    inductance = (permeability * relativep * turns * turns * area) / length
    print(f"Inductance is {inductance} henry")
    return inductance

def get_inductive_reactance(frequency, inductance):
    reactance = 2 * math.pi * frequency * inductance
    print(f"Reactance is {reactance} ohms")
    return reactance

if __name__ == "__main__":
    get_inductive_reactance(1, 2)
########################################################
import math

def get_inductance_material (permeability, relativep, turns, area, length):
    inductance = (permeability * relativep * turns * turns * area) / length
    print(f"Inductance is {inductance} henry")
    return inductance

def get_inductive_reactance(frequency, inductance):
    reactance = 2 * math.pi * frequency * inductance
    print(f"Reactance is {reactance} ohms")
    return reactance

if __name__ == "__main__":
    get_inductive_reactance(1, 2)
########################################################

def get_resistance_material(resistivity, length, area):
    resistance = (resistivity * length) / area
    print(f"Resistance is{resistance} ohms")
    return resistance

def get_resistance_by_iv(voltage, current):
    resistance = voltage / current
    print(f"Resistance is{resistance} ohms")
    return resistance

get_resistance_material(0.06, 10, 9)
get_resistance_by_iv(3.0, 3.0)

if __name__ == "__main__":
    get_resistance_material(6, 2, 3)
    get_resistance_by_iv(10.0, 5.0)

#MAINRUNNER

from zzMyPackage_09.RESISTOR import resistor
from CAPACITOR import capacitor
from zzMyPackage_09.INDUCTOR import inductor

print("Welcome to Electronics Calculator")

while True:

    selector = input("Please select a calculator: ")

    match selector.upper():
        case "RESISTANCE":
            voltage = float(input("Please enter the voltage value: "))
            current = float(input("Please enter the  current value: "))
            resistor.get_resistance_by_iv(voltage, current)

        case "CAPACITANCE":
            voltage = float(input("Please enter the charge value : "))
            charge = float(input("Please enter the  voltage value : "))
            capacitor.get_capacitance_by_cv(charge, voltage)

        case "INDUCTANCE":
            frequency = float(input("Please enter the frequency value : "))
            inductance = float(input("Please enter the inductance value : "))
            inductor.get_inductive_reactance(frequency, inductance)

        case _:
            print("SYNTAX ERROR")

student1_name = "ZILONG"
student1_grade = "1.75"
student1_subject = "FIGHTER"

student2_name = "JOY"
student2_grade = "2.5"
student2_subject = "ASSASSIN"

student3_name = "WANWAN"
student3_grade = "5"
student3_subject = "MARKSMAN"

def print_student_info_function(name, grade, subject):
    print(f"Student {name} - grade is {grade} - subject is {subject}")

if __name__ == "__main__":
    print_student_info_function(student1_name, student1_grade, student1_name)
    print_student_info_function(student2_name, student2_grade, student2_name)
    print_student_info_function(student3_name, student3_grade, student3_name)

#CLASS
class Student:
    default_subject = "Mobile Legends"
    year_and_section = "1-2"

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info_method(self):
        print(f"Name {self.name} - grade is {self.grade} - subject is {self.subject}")

    @classmethod
    def print_student_info_class_method(cls, name, grade):
        print(f"Student {name} - grade is {grade} - subject is {cls.default_subject}")
        return cls(name, grade, cls.default_subject)

    @classmethod
    def update_year_and_section(cls, year_section_update):
        cls.year_and_section = year_section_update

    @staticmethod
    def is_passing_grade(grade):
        if grade <= 3:
            print("passed, congrats")
        else:
            print("did not passed, nice try")


#--------------------------------------------------------------------------------------------------------------------------
print("#-------------------------------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    student1 = Student("ZILONG", 1.75, "FIGHTER")
    student2 = Student("JOY", 2.5, "ASSASSIN")
    student3 = Student("WANWAN", 5, "MARKSMAN")
    student4 = Student.print_student_info_class_method("FLORYN", "1.75")

    student1.print_student_info_method()
    student2.print_student_info_method()
    student3.print_student_info_method()

    Student.is_passing_grade(4.75)
    Student.is_passing_grade(student1.grade)
    Student.is_passing_grade(student2.grade)
    Student.is_passing_grade(student3.grade)

    print(student1.year_and_section)
    print(student2.year_and_section)
    print(student3.year_and_section)
    Student.update_year_and_section("2-4")
    print(student1.year_and_section)
    print(student2.year_and_section)
    print(student3.year_and_section)

#SUBCLASS

import CLASS

student1_name = "ZILONG"
student1_grade = "1.75"
student1_subject = "FIGHTER"

CLASS.print_student_info_function(student1_name, student1_grade, student1_subject)

student = CLASS.Student("WANWAN", 3, "MARKSMAN")
student.print_student_info_method()



#MAINPROGRAM


import serial
import time
import threading

serialInstance = serial.Serial("COM1", 9600, timeout=1)
time.sleep(2)

def send(message):
    serialInstance.write((message + '\n').encode("utf-8"))
    print(f"Napasok na mensahe: {message}")


def receive():
    if serialInstance.in_waiting > 0:
        data = serialInstance.readline().decode("utf-8")
        if data:
            print(f"received: {data}")
            return data
    return None

def receive_continuous():
    while True:
        received_data = receive()
        time.sleep(0.1)

received_thread_instance = threading.Thread(target=receive_continuous, daemon=True)
received_thread_instance.start()

try:
    while True:
        message = input("Enter mo na: ")
        if message:
            send(message)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    serialInstance.close()


#DEMO 24


#DETECTOR

import os
import time

##print(os.listdir(os.getcwd()))
#os.makedirs(os.getcwd() + "/" + "new folder 1"))
#os.makedirs(os.path.join(os.getcwd(), "new folder 3")))
#os.makedirs(os.path.join(os.path.join(os.path.join(os.getcwd(), "new folder 3")),"This  is a new folder inside a folder"))
#print(os.path.dirname(os.path.abspath(__file__)))
BASE_FILE = os.path.dirname(os.path.abspath(__file__))
BASE_FILE2 = os.path.dirname(BASE_FILE)

#for root, dirs, files in os.walk(os.getcwd()):
    #for file in files:
        #if file.endswith("CABRADILLA_JOHN_LENARD_UTS_ESSAY2_DEC13.docx"):
            #print(file)

#for root, dirs, files in os.walk(BASE_FILE):
    #for filename in files:
        #print(filename)
        #if filename == "justbingoplusmylocationsir.py":
            #print("==========================================================")
            #print("FILE DETECTED")
            #print("==========================================================")

with open(os.path.join(BASE_FILE2, "HUNTERHUNTER.txt"), "w", encoding="utf-8"):
    print("Virus Alert!!")
    time.sleep(10)

for root, dirs, files in os.walk(BASE_FILE2):
    for filename in files:
        print(filename)
        if filename == "HUNTERHUNTER.txt":
            print("==========================================================")
            print("VIRUS DETECTED, deleting it.....")
            file_loc = os.path.join(BASE_FILE2, filename)
            print(file_loc)
            time.sleep(2)
            os.remove(file_loc)
            time.sleep(2)
            print("==========================================================")

#COMBINATION

import csv
import time
import os

BASE_FILE = os.path.dirname(os.path.abspath(__file__))
BASE_FILE2 = os.path.dirname(BASE_FILE)

RESOURCE_FILE = os.path.join(BASE_FILE2, 'CSV_DIRECTORY')
CSV_PATH = os.path.join(RESOURCE_FILE, 'MYsecondCSV.csv')

csv_list_data = []

with open(CSV_PATH, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
        csv_list_data.append(row)

print(csv_list_data)
print(csv_list_data[3])

name_and_address = []

for row in csv_list_data:
    name_and_address.append([row[1], row[4]])

CSV_PATH = os.path.join(RESOURCE_FILE, 'MYsecondCSV.csv')

with open(CSV_PATH, mode = "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(name_and_address)


#PART 3 GSPREAD


import os
import time
import gspread
from googleapiclient.errors import HttpError
from gspread.utils import ValueInputOption
from oauth2client.service_account import ServiceAccountCredentials

BASE_FILE = os.path.dirname(os.path.abspath(__file__))
BASE_FILE2 = os.path.dirname(BASE_FILE)

RESOURCE_FILE = os.path.join(BASE_FILE2, 'CSV_DIRECTORY')
SERVICE_KEY_PATH = os.path.join(RESOURCE_FILE, 'cmpeedelgado-3d15e460cd6f.json')

sheet_url = "https://docs.google.com/spreadsheets/d/1FZArplLHvuFnwNct5ZnB6PVZmPVDSmHrHHQlPU1zlIw/edit?"

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_KEY_PATH, scopes=[
    'https://www.googleapis.com/auth/spreadsheets',  'https://www.googleapis.com/auth/drive'])
client = gspread.authorize(credentials)

gs_instance = client.open_by_url(sheet_url)

sheet_instance = gs_instance.get_worksheet(0)

google_sheet_data = sheet_instance.get_all_records()

print(google_sheet_data)


