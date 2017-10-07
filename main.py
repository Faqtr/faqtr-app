import speech_recognition
from multiprocessing import Pool
from transcribe import transcribe_audio


def process(recognizer, audio):
    # Get text chunk from audio
    transcribed_text_chunk = transcribe_audio.run(recognizer, audio)

    if len(transcribed_text_chunk) > 0:
        # Call ML function which returns true or false
        # if true, call search api
        pass


# Main

pool = Pool(processes=1)
recognizer = speech_recognition.Recognizer()

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
