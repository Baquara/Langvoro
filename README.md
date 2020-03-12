Langvoro is a project designed to ultimately provide a free of charge (and free of accounts) alternative to popular online language courses and applications.
It uses the Google Translate API to translate a basic vocabulary (in English by default as it is handled better by GT), as well as its TTS technology to provide voices. I also scrapes for image from Google or Flickr, so it's not necessary to provide an image for each new word or sentence added.
The courses will be structured in cards, where the user will have access to audiovisual content, and will need to write down the sentences in order to improve reading, writing and listening skills at the same time. A better way to define it, the goal is to become an "Anki on steroids".
It also provides transliteration to some text, such as Cyrillic, Japanese text (Kanji, Hiragana and Katakana), Chinese text and Korean text (Hangul).
It's still very WIP, and as of the last commit, all of it was done in a single day.

#### Requirements/dependencies

- Python 3
- PySimpleGUI
- gtts
- googletrans
- playsound
- unidecode
- google_images_download
- Image / PIL
- transliterate
- pykakasi
- hangul_romanize
- flickrapi
- urllib.request


#### Roadmap

- Actually provide a structure for the courses (how each section/step/phase will work in terms of learning and comprehension). For example, there could be a section where the user would be provided machine generated random sentences/situations where he/she would need to use the language skills he acquired in order to give a proper reply, and the machine would then decide it as accurate or not.
- Provide support for Speech to Text (using a suitable API) where the user would have to speak the sentences on top of listening and writing it
- Add some minor machine learning functions where it's needed or fit
- Add gamification (scores, give benefits to those who makes less mistakes)
- Add support for dictionary, where the user would be provided a definition for each word he/she clicks.
- Support to train/drawn alphabetic characters to non-latin alphabets
- Add every single basic words between languages to the database
- Add an option to download the entire course for offline usage
- Port it to Android, or even make a web interface
