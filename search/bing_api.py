import requests
import re
from ml.nlp import numtext_interconversion

BASE_URL = "https://api.cognitive.microsoft.com/bing/v7.0/search"
headers = {'Ocp-Apim-Subscription-Key': 'cd18b9463d45418fa44af0837b59cb51'}


def search(text):
    response = requests.get(BASE_URL, params={'q': text}, headers=headers).json()
    result_list = response['webPages']['value']
    relevant_sentence_list = []

    # Fetch various opinions and results from the search
    for res in result_list:
        # Eliminate noise from sentence
        noiseless_snip = re.sub('[^A-Za-z0-9 ]+', '', res['snippet']).lower()

        # Break into words to find int and do int2word
        words = noiseless_snip.split(" ")
        for i in range(0, len(words)):
            try:
                num = int(words[i])
                words[i] = numtext_interconversion.int2text(num)
            except:
                pass

        j = 0
        while j < len(words):
            if numtext_interconversion.is_str_int_rep(words[j]):
                rep = ""
                while j < len(words) and numtext_interconversion.is_str_int_rep(words[j]):
                    rep += words[j]
                    words[j] = ''
                    j += 1
                words[j - 1] = rep
            j += 1

        # Remake sentence
        " ".join(words)

        # Append first 150 chars (ML Model limitation)
        relevant_sentence_list.append(noiseless_snip[:150].encode('utf-8'))

    return relevant_sentence_list
