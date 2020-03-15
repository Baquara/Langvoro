import PySimpleGUI as sg
from gtts import gTTS
from googletrans import Translator
from playsound import playsound
import unidecode
import re, string, timeit
from google_images_download import google_images_download   #importing the library
import sys,os
from PIL import Image
from transliterate import translit, get_available_language_codes
import pykakasi
from hangul_romanize import Transliter
from hangul_romanize.rule import academic
import flickrapi
import urllib.request
import speech_recognition as sr
import pyaudio


#sg.theme('DarkAmber')   # Add a touch of color

my_dict = {'ab': 'Abkhazian', 'aa': 'Afar', 'af': 'Afrikaans', 'ak': 'Akan', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'an': 'Aragonese', 'hy': 'Armenian', 'as': 'Assamese', 'av': 'Avaric', 'ae': 'Avestan', 'ay': 'Aymara','az': 'Azerbaijani','bm': 'Bambara','ba': 'Bashkir','eu': 'Basque','be': 'Belarusian','bn': 'Bengali (Bangla)','bh': 'Bihari','bi': 'Bislama','bs': 'Bosnian','br': 'Breton','bg': 'Bulgarian','my': 'Burmese','ca': 'Catalan','ch': 'Chamorro','ce': 'Chechen','ny': 'Chichewa, Chewa, Nyanja','zh': 'Chinese','zh-cn': 'Chinese (Simplified)','zh-tw': 'Chinese (Traditional)','cv': 'Chuvash','kw': 'Cornish','co': 'Corsican','cr': 'Cree','hr': 'Croatian','cs': 'Czech','da': 'Danish','dv': 'Divehi, Dhivehi, Maldivian','nl': 'Dutch','dz': 'Dzongkha','en': 'English','eo': 'Esperanto','et': 'Estonian','ee': 'Ewe','fo': 'Faroese','fj': 'Fijian','fi': 'Finnish','fr': 'French','ff': 'Fula, Fulah, Pulaar, Pular','gl': 'Galician','gd': 'Gaelic (Scottish)','gv': 'Gaelic (Manx), Manx','ka': 'Georgian','de': 'German','el': 'Greek','kl': 'Kalaallisut, Greenlandic','gn': 'Guarani','gu': 'Gujarati','ht': 'Haitian Creole','ha': 'Hausa','he': 'Hebrew','hz': 'Herero','hi': 'Hindi','ho': 'Hiri motu','hu': 'Hungarian','is': 'Icelandic','io': 'Ido','ig': 'Igbo','id': 'Indonesian','in': 'Indonesian','ia': 'Interlingua','ie': 'Interlingue','iu': 'Inuktitut','ik': 'Inupiak','ga': 'Irish','it': 'Italian','ja': 'Japanese','jv': 'Javanese','kn': 'Kannada','kr': 'Kanuri','ks': 'Kashmiri','kk': 'Kazakh','km': 'Khmer','ki': 'Kikuyu','rw': 'Kinyarwanda (Rwanda)','rn': 'Kirundi','ky': 'Kyrgyz','kv': 'Komi','kg': 'Kongo','ko': 'Korean','ku': 'Kurdish','kj': 'Kwanyama','lo': 'Lao','la': 'Latin','lv': 'Latvian (Lettish)','li': 'Limburgish ( Limburger)','ln': 'Lingala','lt': 'Lithuanian','lu': 'Luga-Katanga','lg': 'Luganda, Ganda','lb': 'Luxembourgish','mk': 'Macedonian','mg': 'Malagasy','ms': 'Malay','ml': 'Malayalam','mt': 'Maltese','mi': 'Maori','mr': 'Marathi','mh': 'Marshallese','mo': 'Moldavian','mn': 'Mongolian','na': 'Nauru','nv': 'Navajo','ng': 'Ndonga','nd': 'Northern Ndebele','ne': 'Nepali','no': 'Norwegian','nb': 'Norwegian bokmål','nn': 'Norwegian nynorsk','ii': 'Nuosu, Sichuan Yi','oc': 'Occitan','oj': 'Ojibwe','cu': 'Old Church Slavonic, Old Bulgarian','or': 'Oriya','om': 'Oromo (Afaan Oromo)','os': 'Ossetian','pi': 'Pāli','ps': 'Pashto, Pushto','fa': 'Persian (Farsi)','pl': 'Polish','pt': 'Portuguese','pa': 'Punjabi (Eastern)','qu': 'Quechua','rm': 'Romansh','ro': 'Romanian','ru': 'Russian','se': 'Sami','sm': 'Samoan','sg': 'Sango','sa': 'Sanskrit','sr': 'Serbian','sh': 'Serbo-Croatian','st': 'Sesotho','tn': 'Setswana','sn': 'Shona','sd': 'Sindhi','si': 'Sinhalese','ss': 'Siswati, Swati','sk': 'Slovak','sl': 'Slovenian','so': 'Somali','nr': 'Southern Ndebele','es': 'Spanish','su': 'Sundanese','sw': 'Swahili (Kiswahili)','sv': 'Swedish','tl': 'Tagalog','ty': 'Tahitian','tg': 'Tajik','ta': 'Tamil','tt': 'Tatar','te': 'Telugu','th': 'Thai','bo': 'Tibetan','ti': 'Tigrinya','to': 'Tonga','ts': 'Tsonga','tr': 'Turkish','tk': 'Turkmen','tw': 'Twi','ug': 'Uyghur','uk': 'Ukrainian','ur': 'Urdu','uz': 'Uzbek','ve': 'Venda','vi': 'Vietnamese','vo': 'Volapük','wa': 'Wallon','cy': 'Welsh','wo': 'Wolof','fy': 'Western Frisian','xh': 'Xhosa','yi': 'Yiddish','ji': 'Yiddish','yo': 'Yoruba','za': 'Zhuang, Chuang','zu': 'Zulu'}

my_inverted_dict = dict(map(reversed, my_dict.items()))

google_sp_dict ={

'af' : 'af-ZA',
'am' : 'am-ET',
'by' :'by-AM',
'az': 'az-AZ',
'id':'id-ID',
'ms':'ms-MY',
'bn':'bn-BD',
'ca':'ca-ES',
'cs':'cs-CZ',
'da':'da-DK',
'de':'de-DE',
'en':'en-US',
'es':'es-ES',
'eu' : 'eu-ES',
'fil':'fil-PH', 
'fr': 'fr-FR',
'gl':'gl-ES', 
'ka':'ka-GE',
'gu':'gu-IN', 
'hr':'hr-HR', 
'zu':'zu-ZA', 
'is':'is-IS', 
'it':'it-IT', 
'jv':'jv-ID',
'kn':'kn-IN ',
'km':'km-KH',
'b':'b-LA', 
'Iv':'Iv-LV', 
'It':'It-LT', 
'hu':'hu-HU',
'ml':'ml-IN',
'mr':'mr-IN',
'nl':'nl-NL',
'ne':'ne-NP',
'nb':'nb-NO',
'pl':'pl-PL',
'pt':'pt-BR' ,
'ro':'ro-RO', 
'si':'si-LK' ,
'sk':'sk-SK' ,
'sl':'sl-SI' ,
'su':'su-ID' ,
'sw':'sw-TZ' ,
'fi':'fi-FI' ,
'sv':'sv-SE' ,
'ta':'ta-IN' ,
'te':'te-IN' ,
'vi':'vi-VN' ,
'tr':'tr-TR' ,
'ur':'ur-IN' ,
'el':'el-GR' ,
'bg':'bg-BG' ,
'ru':'ru-RU' ,
'sr':'sr-RS' ,
'uk':'uk-UA' ,
'he':'he-IL' ,
'ar':'ar-EG' ,
'fa':'fa-IR' ,
'hi':'hi-IN' ,
'th':'th-TH' ,
'ko':'ko-KR' ,
'zh':'zh-TW' ,
'yue':'yue-Hant-HK',
'ja':'ja-JP' ,
'zh':'zh'
}



terminate=False



def showtranslated(otext,lang):
    translator = Translator()
    needs_translit = False
    translit = ''
    translations = translator.translate(otext, dest=lang)
    if (lang!='ru' or lang!='ja' or lang!='ko'):
         layout = [  
            [sg.InputText(translations.text)],
            [sg.Button('Cancel')] ]
    else:
        translit = transliter(translations.text,lang)
        layout = [  
            [sg.InputText(translations.text)],
            [sg.InputText(translit)],
            [sg.Button('Cancel')] ]
        needs_translit=True
        elemento= simplify(otext)
    global window
    window = sg.Window('Results', layout)
    while True:
        event, values = window.Read()
        if event in (None, 'Cancel'):
            window.close()
            break

def showspeechresults(text):
    layout = [  
            [sg.InputText(text)],
            [sg.Button('Ok')]]
    global window
    window = sg.Window('Speech results', layout)
    while True:
        event, values = window.Read()
        if event in (None, 'Ok'):   # if user presses ok
            window.close()
            break





def custominput(selected):

    layout = [  
            [sg.Text('Enter input'), sg.InputText()],
            [sg.Button('Ok'),sg.Button('Repeat'), sg.Button('Cancel')],
            [sg.Button('Speech to text'),sg.Text('Say something right after clicking')]]
    translator = Translator()
    lang=my_inverted_dict[selected]
    glang=google_sp_dict[lang]
    print("O idioma para stt é "+glang)
    print(lang)
    global window
    window = sg.Window('Custom translation', layout)
    while True:
        event, values = window.Read()
        if event in (None, 'Cancel'):
            window.close()
            break
        if event in (None, 'Repeat'):   # if user presses repeat
            translations = translator.translate(values[0], dest=lang)
            tts = gTTS(translations.text, lang=lang)
            tts.save('audio.mp3')
            playsound('audio.mp3')
        if event in (None, 'Ok'):   # if user presses ok
            showtranslated(values[0],lang)
        if event in (None, 'Speech to text'):
            with sr.Microphone( sample_rate=48000) as source:
                r=sr.Recognizer()
                r.adjust_for_ambient_noise(source)
                print("Say Something!")
                audio=r.listen(source)
                try:
                    text = r.recognize_google(audio,language=glang)
                    showspeechresults(text) 
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}").format(e)



def transliter(text,code):
    if code=='ja':
        textt = text
        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
        kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
        kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
        kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
        kakasi.setMode("s", True) # add space, default: no separator
        kakasi.setMode("C", True) # capitalize, default: no capitalize
        conv = kakasi.getConverter()
        result = conv.do(textt)
        return (result)
    elif code=='ko':
        transliter = Transliter(academic)
        return transliter.translit(text)
    else:
        return translit(text, code, reversed=True)


def simplify(istring):
    unaccented_string = unidecode.unidecode(istring)
    nopont = unaccented_string.translate(str.maketrans('', '', string.punctuation))
    return nopont.lower()

def card(meaning,phrase,image,windowname,lan):
    needs_translit = False
    translit = ''
    glang=google_sp_dict[lan]
    if (lan=='ru' or lan=='ja' or lan=='ko'):
        translit = transliter(phrase,lan)
        print(translit)
        needs_translit=True
    if needs_translit==True:    
        layout = [  
                [sg.Text(meaning)],
                [sg.Text(phrase)],
                [sg.Text(translit)],
                [sg.Image(image)],
                [sg.Text('Repeat sentence'), sg.InputText()],
                [sg.Button('Ok'),sg.Button('Repeat'), sg.Button('Skip'), sg.Button('Cancel')],
                [sg.Button('Speech to text'),sg.Text('Say something right after clicking')] ]
    else:
        layout = [  
                [sg.Text(meaning)],
                [sg.Text(phrase)],
                [sg.Image(image)],
                [sg.Text('Repeat sentence'), sg.InputText()],
                [sg.Button('Ok'),sg.Button('Repeat'), sg.Button('Skip'), sg.Button('Cancel')],
                [sg.Button('Speech to text'),sg.Text('Say something right after clicking')]]
    global window
    window = sg.Window(windowname, layout)
    tts = gTTS(phrase, lang=lan)
    tts.save('audio.mp3')
    playsound('audio.mp3')
    while True:
        event, values = window.Read()
        if event in (None, 'Skip'):   # if user presses cancel
            break
        if event in (None, 'Cancel'):   # if user presses cancel
            global terminate
            terminate=True
            break
        if event in (None, 'Repeat'):   # if user presses repeat
            playsound('audio.mp3')
        if event in (None, 'Ok'):   # if user presses ok
           values[1]= simplify(values[1])
           print(phrase)
           if values[1]==simplify(phrase) or  (values[1]==simplify(translit) and needs_translit==True):
            window.close()
            verifycard(meaning,phrase,image,windowname,lan)
            break
        if event in (None, 'Speech to text'):
            with sr.Microphone( sample_rate=48000) as source:
                r=sr.Recognizer()
                r.adjust_for_ambient_noise(source)
                print("Say Something!")
                audio=r.listen(source)
                try:
                    text = r.recognize_google(audio,language=glang)
                    showspeechresults(text) 
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}").format(e)
    window.close()


def verifycard(meaning,phrase,image,windowname,lan):
    needs_translit = False
    translit = ''
    if (lan=='ru' or lan=='ja'):
        translit = transliter(phrase,lan)
        print(translit)
        needs_translit=True
    layout = [  
            [sg.Text(meaning)],
            [sg.Image(image)],
            [sg.Text('Repeat sentence'), sg.InputText()],
            [sg.Button('Ok'),sg.Button('Repeat'), sg.Button('Skip')] ]
    global window
    window = sg.Window(windowname, layout)
    playsound('audio.mp3')
    while True:
        event, values = window.Read()
        if event in (None, 'Skip'):   # if user presses cancel
            break
        if event in (None, 'Repeat'):   # if user presses repeat
            playsound('audio.mp3')
        if event in (None, 'Ok'):   # if user presses ok
           values[1]= simplify(values[1])
           print(phrase)
           if values[1]==simplify(phrase) or  (values[1]==simplify(translit) and needs_translit==True):
            window.close()
            break
    window.close()
    
def lvl(selected,lvl):
    translator = Translator()
    selevel = 0
    title=selected + ' course - '+str(lvl[0])
    translations=''
    iteration=0
    if str(lvl[0])=='Level 1':
        print("Level 1 was chosen")
        selevel = 1
    if str(lvl[0])=='Level 2':
        print("Level 2 was chosen")
        selevel = 2
    if str(lvl[0])=='Level 3':
        print("Level 3 was chosen")
        selevel = 3
    lang=my_inverted_dict[selected]
    print(lang)
    if selevel ==1:
        translations = translator.translate(['Ball', 'Chair', 'Dog', 'House', 'Child','Girl','Boy','Man','Woman','Water','Cat'], dest=lang)
    if selevel ==2:
        translations = translator.translate(['Hello!', 'Thank you!', 'Sorry!', 'Good morning.', 'Excuse me.'], dest=lang)
    if selevel ==3:
        translations = translator.translate(['Hi! My name is Adam', 'Nice to meet you!', 'How old are you?', 'Where is the bathroom?', 'I need to go now. Bye bye!'], dest=lang)
    for translation in translations:
        global terminate
        if terminate==True :
            terminate=False
            break

#Procurar imagens
        iteration=iteration+1
        """orig_stdout = sys.stdout
        f = open('URLS.txt', 'w')
        sys.stdout = f
        response = google_images_download.googleimagesdownload()   #class instantiation
        arguments = {"keywords":translation.origin,"limit":1,"print_urls":True,"format":"png"}   #creating list of arguments
        paths = response.download(arguments)   #passing the arguments to the function
        print(paths)   #printing absolute paths of the downloaded images
        sys.stdout = orig_stdout
        f.close()

        with open('URLS.txt') as f:
            content = f.readlines()
        f.close()

        urls = []
        for j in range(len(content)):
            if content[j][:9] == 'Completed':
                urls.append(content[j][22:-1])   

        basewidth = 300
        img = Image.open('./' + 'downloads' + '/' + translation.origin +'/' + str(urls[0]))
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save('./' + 'downloads' + '/' + translation.origin +'/' + 'resize' + str(urls[0])) """
#Flickr
        flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)


        keyword = translation.origin

        photos = flickr.walk(text=keyword,
                            tag_mode='all',
                            tags=keyword,
                            extras='url_c',
                            per_page=100,           # may be you can try different numbers..
                            sort='relevance')

        urls = []
        for i, photo in enumerate(photos):
            #print (i)
            
            url = photo.get('url_c')
            urls.append(url)
            
            # get 50 urls
            if i > 2:
                break

        print (urls)

        # Download image from the url and save it to '00001.jpg'
        linki = str(iteration) + '.png'
        try:
            urllib.request.urlretrieve(urls[1], linki)
        except: 
            linki= 'notloaded.png'
            pass

        # Resize the image and overwrite it
        basewidth = 300
        image = Image.open(linki) 
        wpercent = (basewidth/float(image.size[0]))
        hsize = int((float(image.size[1])*float(wpercent)))
        image = image.resize((basewidth,hsize), Image.ANTIALIAS)
        image.save(linki)
        #try: 
        #    os.remove('00001.jpg')
        #except: pass
        print(translation.origin)
        print(translation.text)
        print(title)
        print(lang)
        card(translation.origin,translation.text,linki,title,lang)



def Course(selected):
    layout = [  
            [sg.Text('Select the level:')],
            [sg.Listbox(values=['Level 1', 'Level 2', 'Level 3'], size=(30, 6))],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Custom input')] ]
    global window
    window = sg.Window(selected + ' course', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'): 
            window.close()
            break
        if event in (None, 'Ok'):  
            print(values)
            window.close()
            lvl(selected,values[0])
            Course(selected)
        if event in (None, 'Custom input'):
            custominput(selected)


def main():
    # All the stuff inside your window.
    layout = [  
                [sg.Text('Welcome to Langvoro! Select the language you want to learn:')],
                [sg.Combo(['Abkhaz','Afar','Afrikaans','Akan ','Albanian ','Amharic ','Arabic ','Aragonese ','Armenian ','Assamese ','Avaric','Avestan','Aymara','Azerbaijani','Bambara','Bashkir','Basque','Belarusian','Bengali','Bangla ','Bihari','Bislama','Bosnian ','Breton ','Bulgarian ','Burmese ','Catalan','Valencian','Chamorro ','Chechen','Chichewa','Chewa','Nyanja','Chinese (Simplified)','Chinese (Traditional)' ,'Chuvash','Cornish','Corsican','Cree','Croatian','Czech','Danish','Divehi','Dhivehi','Maldivian','Dutch','Dzongkha','English','Esperanto','Estonian','Ewe','Faroese','Fijian','Finnish','French','Fula','Fulah','Pulaar','Pular','Galician','Ganda','Georgian','German','Greek','Guaraní','Gujarati','Haitian','Haitian Creole','Hausa','Hebrew','Herero','Hindi','Hiri Motu','Hungarian','Icelandic','Ido','Igbo','Indonesian','Interlingua','Interlingue','Inuktitut','Inupiaq','Irish','Italian','Japanese','Javanese','Kalaallisut','Greenlandic','Kannada','Kanuri','Kashmiri','Kazakh','Khmer','Kikuyu','Gikuyu','Kinyarwanda','Kirundi','Komi ','Kongo','Korean','Kurdish','Kwanyama','Kuanyama','Kyrgyz','Lao','Latin','Latvian','Limburgish','Limburgan','Limburger','Lingala','Lithuanian','Luba-Katanga','Luxembourgish','Letzeburgesch','Macedonian','Malagasy','Malay','Malayalam','Maltese','Manx','Marathi','Marshallese','Mongolian','Maori','Nauru','Navajo','Navaho','Ndonga','Nepali','Northern Ndebele','Northern Sami','Norwegian','Norwegian Bokmål','Norwegian Nynorsk','Nuosu','Occitan','Ojibwe','Ojibwa','Old Church Slavonic','Church Slavonic','Old Bulgarian','Oriya','Oromo','Ossetian','Ossetic','Panjabi','Punjabi','Pashto','Pushto','Persian','Polish','Portuguese','Pali','Quechua','Romanian','Romansh','Russian','Samoan','Sango','Sanskrit','Sardinian','Scottish Gaelic','Gaelic','Serbian','Shona','Sindhi','Sinhala','Sinhalese','Slovak','Slovene','Somali','Southern Ndebele','Southern Sotho','Spanish','Castilian','Sundanese','Swahili','Swati','Swedish','Tagalog','Tahitian','Tajik','Tamil','Tatar','Telugu','Thai','Tibetan Standard','Tibetan','Central','Tigrinya','Tonga','Tsonga','Tswana','Turkish','Turkmen','Twi tw','Ukrainian','Urdu','Uyghur','Uighur','Uzbek','Venda','Vietnamese','Volapük','Walloon','Welsh','Western Frisian','Wolof','Xhosa','Yiddish','Yoruba','Zhuang','Chuang','Zulu'])],
                #[sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Langvoro', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'): 
            window.close()
            break
        if event in (None, 'Ok'):  
            Course(values[0])


if __name__ == '__main__':
    main()
