import pickle

dump = pickle.load(open('trainingpositive.p', 'r'))
statistical_data = open('../Statistical.txt', 'r').readlines()

sen_location = {}

# Store questions location
cnt = 0
for i in range(0, len(dump)):
    dump[i][0] = statistical_data[int(i / 5)]
    print dump[i]

pickle.dump(dump, open('newpositivetrainingsetwithstatement.p', 'w'))
