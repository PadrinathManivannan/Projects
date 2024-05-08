import csv
import yaml
import os

def csv_to_yaml(ucd_instance, csv_file, yaml_file)
  data = []
print("Enter filename with extension")
filename = input(Type your .csv filename:")
if not filename.endswith('.csv'):
  print("You opened a wrong file extension.Please provide a .csv filename")
else:
  try:
    with open(filename, 'r', encoding='utf-8-sig') as csv_file:
      csv_reader = csv,reader(csv_file)
      data = []
      for row in csv_reader:
        print(row)
        data.append(row)
    
    with open("outputfile.yaml", 'w', encoding='utf-8-sig') as yaml_file:
      yaml.dump(data, yaml_file, allow_unicode=True)
      csv_to_yaml("ucd","filename","outputfile.yaml")
      print("File converted successfully")
  except FileNotFoundError:
    print("File was not found")
    
