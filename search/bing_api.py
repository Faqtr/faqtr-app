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

        # Normalizing the string to replace number expressed in words
        norm_snip = numtext_interconversion.wrapper_normalizer(noiseless_snip)

        # Append first 150 chars (ML Model limitation)
        relevant_sentence_list.append(norm_snip[:150].encode('utf-8'))

    return relevant_sentence_list
