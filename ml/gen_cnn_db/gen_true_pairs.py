from search import bing_api

file = open("../Statistical.txt", "r")

sentences = []

for line in file:
    sentences.append(line)

for sen in sentences:
    results = bing_api.search(sen)

