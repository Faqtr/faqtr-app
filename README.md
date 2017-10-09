# Faqtr

Faqtr aim to perform statistical claim validation with the aid of Voice Transcribing, Deep Learning and Natural Language Processing.

### Installing

* Create a virtualenv and activate it

    `pip install virtualenv && virtualenv env && source env/bin/activate`

* Install the additional libraries required to support packages being used

  ```
  sudo apt-get install libasound2-dev libgstreamer-plugins-good1.0-0:i386 libportaudiocpp0 libtag1v5:i386 mint-backgrounds-serena python3-xlib uuid-dev libssl-dev python-dev portaudio19-dev
  ```

* Install Requirements:

	`sudo pip install -r requirements.txt`

* Create the *appconfig.py* file

    `cp appconfig.sample.py appconfig.py`

* Add the API keys and secrets as given

### Running

`python main.py`

You will be prompted to speak a sentence. On detecting a statistical claim sentence, you receive the response validating your claim.

Examples of statistical sentences factr will detect and work on:

\> *70 percent of earth is covered in water*

\> *3 out of 10 people on the planet do not have access to clean drinking water*

\> *15 million people suffer from metal disorders*

and so on.