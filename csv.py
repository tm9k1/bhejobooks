import csv
# ans =[]
q = {}
i=1
with open('ss.csv') as csv_file:
    csv_reader= csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        q['index'] = i
        q['question'] = row[0]
        q['answers'] = [row[1],row[2],row[3]]
        q['correct_answer'] = row[1]
        if "\'" not in q['question']:
            i+=1
            print('{')
            print('{}: {},'.format('index',q['index']))
            print('{}: \'{}\','.format('question',q['question']))
            print('{}: {},'.format('answers',q['answers']))
            print('{}: \'{}\','.format('correct_answer',q['correct_answer']))
            print('},')