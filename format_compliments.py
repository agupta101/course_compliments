import csv

def format_csv():
    '''Opens csv of compliments and exports formatted  file'''
    outfile = open('formatted.doc', 'w')
    outfile.write(r'<html><head></head><body>')
    with open('course_compliments.csv', 'rU', encoding='latin-1') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            outfile.write(f'<b>{row[2]}</b><br>{row[3]}')
            if row[4] != '':
                outfile.write(f' ({row[4]})')
            outfile.write('<br><br>')
    outfile.write('</body>')
    outfile.close()

format_csv()