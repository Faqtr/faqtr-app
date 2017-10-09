import requests
import re
from ai.nlp import numtext_interconversion

from appconfig import BING_API_KEY

BASE_URL = "https://api.cognitive.microsoft.com/bing/v7.0/search"
headers = {'Ocp-Apim-Subscription-Key': BING_API_KEY}


def search(text):
    response = requests.get(BASE_URL, params={'q': text}, headers=headers).json()
    result_list = response['webPages']['value']
    relevant_sentence_list = []
    relevant_URL_list = []

    # Fetch various opinions and results from the search
    for res in result_list:
        # Eliminate noise from sentence
        noiseless_snip = re.sub('[^A-Za-z0-9 ]+', '', res['snippet']).lower()

        # Normalizing the string to replace number expressed in words
        norm_snip = numtext_interconversion.wrapper_normalizer(noiseless_snip)

        # Append first 150 chars (ML Model limitation)
        relevant_sentence_list.append(norm_snip[:150].encode('utf-8'))

    for res in result_list:
        # Eliminate noise from sentence
        urls = res['displayUrl'].lower()

        # Normalizing the string to replace number expressed in words
        # norm_snip = numtext_interconversion.wrapper_normalizer(noiseless_snip)

        # Append first 150 chars (ML Model limitation)
        relevant_URL_list.append(urls.encode('utf-8'))

    print "Top 5 top hits:"
    for i in range(5):
        print 'Hit #{}:'.format(i+1)
        print relevant_sentence_list[i]
        print "URL:{}".format(relevant_URL_list[i])
        print ""
        print ""

    return relevant_sentence_list
