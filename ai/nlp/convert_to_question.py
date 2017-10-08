import nltk


def convert_statement(text):
    tokenized_text = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokenized_text)

    # Find digit and convert to question for better results
    cardinal_digit_location = [i for i, w in enumerate(tagged) if w[1] == 'CD']
    cardinal_digit = None

    if cardinal_digit_location:
        cardinal_digit = int(tagged[cardinal_digit_location[0]][0])
        tagged.pop(cardinal_digit_location[0])
        tagged.insert(0, ('How Many Much', 'CD'))

    new_ques = ' '.join([t[0] for t in tagged])

    # Return the quest + cardinal digit
    return new_ques, cardinal_digit
