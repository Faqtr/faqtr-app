import speech_recognition


def run(recognizer, audio):
    print("Processing...")

    try:
        transcribe_result = recognizer.recognize_google(audio)
        print("You said " + transcribe_result)
        return transcribe_result

    except speech_recognition.UnknownValueError:
        print("Could not understand audio")

    except speech_recognition.RequestError as e:
        print("Could not request results; {0}".format(e))

    return ""
