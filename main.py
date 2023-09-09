import json

with open('./data/math/hard/2.json') as f:
    data = json.load(f)
    print(data['question'])
    e = input('Input your answer: ')
    if e == data['answer']:
        print('Correct answer!\n\nExplanation: ')
        print(data['explanation'])

    else:
        print('Incorrect')
        print('Correct answer is: ' + data['answer'])
        print(data['explanation'])