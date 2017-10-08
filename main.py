from multiprocessing import Pool

import speech_recognition

from ai.neuralnet import modelStatistics
from ai.nlp.custom_parser import process_text
from ai.nlp import convert_to_question

from search import bing_api
from transcribe import transcribe_audio


def process(recognizer, audio):
    # Get text chunk from audio
    transcribed_text_chunk = transcribe_audio.run(recognizer, audio)

    # Convert the statement into question form and also get the main number metric for future use
    transcribed_text_chunk, cardinal_number = convert_to_question.convert_statement(transcribed_text_chunk)

    statement_array = []

    if len(transcribed_text_chunk) > 0:
        model, word_list = modelStatistics.createModel()

        if modelStatistics.predict(model, word_list, transcribed_text_chunk):
            # getting relevant content from BING API
            model, word_list_phase_2 = ptc.create_network()
            model.load('ml/neuralnet/phase2CNN.model')
            phrase_hits = bing_api.search(transcribed_text_chunk)

            # replace words like '9 out of 10' with actual numerical values
            transcribed_text_chunk = process_text(transcribed_text_chunk)
            scores = []
            for hit in phrase_hits:
                scores.append(cnn.predict(model, word_list_phase_2, transcribed_text_chunk, hit))

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

            for hit in phrase_hits:
                hit = process_text(hit)
                statement_array.append(hit)

    return statement_array


# MAIN

# Init Multithreading stuff
pool = Pool(processes=1)

# Init Speech Recog
recognizer = speech_recognition.Recognizer()

# Build ML Model
# model, word_list = modelStatistics.createModel()

# Driver to receive input
with speech_recognition.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)

    while True:
        print("Speak:")

        # timeout if the time it waits before audio starts
        # phrase_time_limit is to cut it off at those many seconds
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        # Asynchronously process batches of transcribed data
        result = pool.apply_async(process, [recognizer, audio])
