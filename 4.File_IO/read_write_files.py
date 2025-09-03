import csv


file = open('diaries.txt','w')
file.write('PERSONAL LOG 1.0 - PoseidoNet V1.7\n')
file.write('He who hath witness this document hath been blessed by good luck. =]\n')
file.write('Dated - 20.08.2025\n')

liked_songs = {
    'Bad Habits' : 'Ed Sheeran',
    'I am just be Ken' : 'Ryan Gosling',
    'Mastermind' : 'Taylor Swift',
    'Uptown Funk' : 'Mark Ronson ft. Bruno Mars',
    'Ghost' : 'Justin Bieber'
}

output_file = open('music_output.txt','w')

def write_to_file(liked_songs, file_name):
    file_name.write('Liked Songs: ' + '\n')
    for k,v in liked_songs.items():
        file_name.write(k + ' by ' + v + '\n')
    
write_to_file(liked_songs,output_file)

file.close()
output_file.close()


file_text = open('sent_message.txt','w')
file_text.write('Hey there! This is a secret message.')
with open('sent_message.txt','r+') as file_text:
    original_message = file_text.read()
    file_text.seek(0)
    unsent_message = 'This message has been now unsent.'
    file_text.truncate(len(unsent_message))
    file_text.write(unsent_message)
    print(original_message)
    print(unsent_message)
    

with open('Bestseller - Sheet1.csv','r',newline='',encoding='utf-8') as csv_file:
    csv_reader=csv.reader(csv_file)
    
    header = next(csv_reader)
    
    max_sales = 0
    best_selling_box = []
    
    for row in csv_reader:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_box = row

with open('best_seller.csv','w',newline='',encoding='utf-8') as bestseller_file:
    csv_writer = csv.writer(bestseller_file)
    csv_writer.writerow(header)
    csv_writer.writerow(best_selling_box)
    print('The bestseller.csv has been created.')