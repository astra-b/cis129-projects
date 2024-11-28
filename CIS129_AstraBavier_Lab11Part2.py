#Exercise 9.3
import csv

def main():

    with open('grades.csv', mode='w', newline='') as grades:
        first = ''
        last = ''
        grade1 = 0
        grade2 = 0
        grade3 = 0
        writer = csv.writer(grades)
        cont = 'Y'
        
        while cont == 'Y':
            first = input('Input student first name: ')
            last = input('Input student last name: ')
            grade1 = input('Input first exam grade: ')
            grade2 = input('Input second exam grade: ')
            grade3 = input('Input third exam grade: ')
            writer.writerow([first, last, grade1, grade2, grade3])
            cont = input('Input another student? Y/N ')

        
main()