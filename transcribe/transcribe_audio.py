import speech_recognition


def run(recognizer, audio):
    print("Processing...")

    result = ""

    try:
        transcribe_result = recognizer.recognize_google(audio)
        print("You said " + transcribe_result)
        result = transcribe_result

    except speech_recognition.UnknownValueError:
        print("Could not understand audio")

    except speech_recognition.RequestError as e:
        print("Could not request results; {0}".format(e))

    return result
