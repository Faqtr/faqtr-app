import pickle
from ai.nlp import convert_to_question

dump = pickle.load(open('trainingpositive.p', 'r'))
statistical_data = open('../Statistical.txt', 'r').readlines()

i = 0
tup_list = []
for stat in statistical_data:
    ques = stat
    try:
        ques, waste = convert_to_question.convert_statement(stat)
    except:
        pass
    tup_list.append((ques, i))
    i += 1

tup_list = sorted(tup_list, key=lambda tup: tup[0], reverse=True)

cnt = 0

for i in range(0, len(dump)):
    dump[i][0] = statistical_data[tup_list[int(i / 5)][1]]

pickle.dump(dump, open('newpositivetrainingsetwithstatement.p', 'w'))
