#Exercises 9.1 and 9.2
def main():
    
    #Exercise 9.1, inputs grades
    with open('grades.txt', mode='w') as grades:
        grade = 0
        
        while grade != 'STOP':
            grade = input("Input grade, or STOP to end input: ")
            if grade != 'STOP':
                grades.write('{}\n'.format(grade))

    #Exercise 9.2, reads grades
    with open('grades.txt', mode='r') as grades:
        total = 0
        count = 0
        average = 0

        for grade in grades:
            total += int(grade)
            count += 1
            print(grade)

        average = total / count

        print('Total =', total, 'Count =', count, 'Average =', average)

main()
