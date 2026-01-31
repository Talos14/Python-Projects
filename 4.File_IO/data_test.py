import csv
data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
try:
    with open('packing_list.csv','r',newline='',encoding='utf-8') as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print('Packing list file not found. Creating a new one.')

with open('packing_list.csv','w',newline='',encoding='utf-8') as new_pack:
    csv_writer = csv.writer(new_pack)
    csv_writer.writerows(data)
    