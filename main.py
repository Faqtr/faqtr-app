
from multiprocessing import Pool

import speech_recognition

from ai.neuralnet import modelStatistics
from ai.nlp.custom_parser import process_text
from ai.neuralnet import wrapper_phase_2_CNN as ptc
from ai.nlp import ballpark
from ai.nlp.numtext_interconversion import wrapper_normalizer as wn
import re
# from ai.nlp import convert_to_question

from search import bing_api
from transcribe import transcribe_audio


def process(recognizer, audio, modelCNN, wordlistCNN):
    # Get text chunk from audio
    transcribed_text_chunk = transcribe_audio.run(recognizer, audio)
    valid, invalid, figure_bP, scores = 0, 0, 0, []

    # Convert the statement into question form and also get the main number metric for future use
    # transcribed_text_chunk, cardinal_number = convert_to_question.convert_statement(transcribed_text_chunk)

    statement_array = []

    if len(transcribed_text_chunk) > 0:
        model, word_list = modelStatistics.createModel()

        if modelStatistics.predict(model, word_list, transcribed_text_chunk):
            # getting relevant content from BING API
            # modelCNN.load('ai/neuralnet/phase2CNN.model')
            transcribed_text_chunk = process_text(wn(transcribed_text_chunk), False)
            numbers = [str(s) for s in re.findall(r'\b\d+\b', transcribed_text_chunk)]
            search_term = ''.join(i for i in transcribed_text_chunk if i not in numbers and i != '.')
            phrase_hits = bing_api.search('how much many ' + search_term)

            # replace words like '9 out of 10' with actual numerical values
            
            for hit in phrase_hits:
                transcribed_text_chunk = process_text(transcribed_text_chunk)
                hit = process_text(wn(hit))
                figure_bP += ballpark.get_most_relevant_data(transcribed_text_chunk, hit)
                scores.append(ptc.predict(modelCNN, word_list_phase_2, transcribed_text_chunk, hit))



            """
            NOT CALCULATING COSINE DISTANCES
            """
            # calculating cosine distance of retrieved content with actual query
            # for hit in phrase_hits:
            #     hit = process_text(hit)
            #     distance = get_cosine_distance(transcribed_text_chunk, hit)
            #     print transcribed_text_chunk, hit, distance
            #     statement_array.append([hit, distance])
            #
            # statement_array = sorted(statement_array, key=lambda tup: tup[1], reverse=True)

            # AB KYA KARNA HAI
            # CNN ADD KARO
            # Cardinal Difference Module Add karo
            # Combine Results for each, precedence ke hisaab se; something like:
            # score = 0
            # priority = len(phrase_hits) #top priority for first one
            # for hit in phrase_hits:
            #   res1 = CNN(hit, query)
            #   res2 = CardinalDifference(hit, query)
            #   score = priority * someFunc(res1, res2)
            #   priority -= 1
            priority = len(scores)
            
            for score in scores:
                valid += score[0]*priority
                invalid += score[1]*priority
                priority -= 1

    return statement_array, valid, invalid, figure_bP/max(1, len(scores))


# MAIN

# Init Multithreading stuff
# pool = Pool(processes=1)

# Init Speech Recog
recognizer = speech_recognition.Recognizer()

# Build ML Model
# model, word_list = modelStatistics.createModel()

modelCNN, word_list_phase_2 = ptc.create_network()

# Driver to receive input
with speech_recognition.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)

    while True:
        print "Speak:"

        # timeout if the time it waits before audio starts
        # phrase_time_limit is to cut it off at those many seconds
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        # Asynchronously process batches of transcribed data

        # result = pool.apply_async(process, [recognizer, audio, modelCNN, word_list_phase_2])
        r, v, iv, ball = process(recognizer, audio, modelCNN, word_list_phase_2)
        total = v + iv
        try:
            v, iv = v/total, iv/total
            print "Neural Net says claim in {}% valid and {}% invalid".format(v*100, iv*100)
            print "Ballpark figures match {}% of the time".format(ball*100)
        except:
            print "Sentence was not classified as a statistical sentence."
