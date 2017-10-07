from search import bing_api
from ml.nlp import cosine_distance
from ml.nlp import convert_to_question
from tqdm import tqdm
import re

main_arr = []

file = open("../Statistical.txt", "r")

sentences = []

for line in file:
    sentences.append(line)

with open('csvfile.csv', 'wb') as file:
    for sen in tqdm(sentences):

        try:
            sen, num = convert_to_question.convert_statement(sen)
        except Exception:
            pass

        statement_array = []

        results = bing_api.search(sen)

        str_to_insert = ""

        for hit in results:
            hit = re.sub('[^A-Za-z0-9 ]+', '', hit)
            statement_array.append([sen, hit])

        # statement_array = sorted(statement_array, key=lambda tup: tup[1], reverse=True)
        for i in range(0, 5):
            str_to_insert = statement_array[i][0] + '\t' + statement_array[i][1] + '\t' + str(1) + '\n'
            file.write(str_to_insert)
