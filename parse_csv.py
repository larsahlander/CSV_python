import csv

with open('names_sc.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    
    for line in csv_reader:
        print(line)

#    with open('new_names.csv', 'w') as new_file:
#        fieldnames = ['first_name', 'last_name', 'email']
#
#        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#
#        csv_writer.writeheader()
#
#        for line in csv_reader:
#            del line['email']
#            csv_writer.writerow(line)