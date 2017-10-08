import num2words

mult_dict = {'million': 1000000, 'thousand': 1000, 'hundred': 100, 'billion': 1000000000}


def mixed_to_int(full_line):
    tokens = full_line.split(" ")
    final_string_to_return = ""
    i = 0
    while i < len(tokens):
        try:
            if (float(tokens[i])):
                val = float(tokens[i])
                if(i + 1 < len(tokens) and tokens[i + 1]  in ["thousand", "million", "hundred"]):
                    multiplier = mult_dict[tokens[i + 1]]
                    val *= multiplier
                    i += 1
                final_string_to_return += str(val) + " "
                #return val
        except Exception, e:
            final_string_to_return += tokens[i] + " "
        i += 1
    return final_string_to_return

def text2int(textnum, numwords={}):
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def int2text(num):
    return num2words.num2words(num)


def is_str_int_rep(currstr):
    vals = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety", "hundred", "thousand", "million", "billion", "trillion"}
    if currstr in vals:
        return True
    return False

def wrapper_normalizer(source_string):
    source_string = mixed_to_int(source_string)
    final_string_toreturn = ""
    i = 0
    source_string = source_string.split(" ")
    while i < len(source_string):
        #print source_string[i]
        if(is_str_int_rep(source_string[i])):
            #print "inside"
            num_builder = ""
            while i < len(source_string) and (is_str_int_rep(source_string[i]) or ( source_string[i] == "and" and  is_str_int_rep(source_string[i + 1]) == True ) ):
                num_builder += (source_string[i] + " ")
                i += 1
            #print (num_builder)
            #print (text2int(num_builder))
            final_string_toreturn += str(text2int(num_builder)) + " "
        else:
            final_string_toreturn += source_string[i] + " "
            i += 1

    return final_string_toreturn

#print(wrapper_normalizer("two hundred fifty thousand people out of five hundred fifty and people are idiots"))