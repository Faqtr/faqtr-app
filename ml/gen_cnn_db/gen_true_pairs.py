from search import bing_api
from ml.nlp import cosine_distance
import pickle
from tqdm import tqdm

main_arr = []

file = open("../Statistical.txt", "r")

sentences = []

for line in file:
    sentences.append(line)

for sen in tqdm(sentences):
    statement_array = []

    results = bing_api.search(sen)
    for hit in results:
        distance = cosine_distance.get_cosine_distance(sen, hit)
        statement_array.append([sen, hit, distance])

    statement_array = sorted(statement_array, key=lambda tup: tup[1], reverse=True)
    for i in range(0, 5):
        main_arr.append(statement_array[i])

pickle.dump(main_arr, open('main_arr.pkl', 'w'))
