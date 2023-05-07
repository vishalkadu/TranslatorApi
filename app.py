from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/translate')
def translate():
    languages = {'Amharic': 'am',
                'Arabic': 'ar',
                'Basque': 'eu',
                'Bengali': 'bn',
                'EnglishUK': 'en-GB',
                'PortugueseBrazil': 'pt-BR',
                'Bulgarian': 'bg',
                'Catalan': 'ca',
                'Cherokee': 'chr',
                'Croatian': 'hr',
                'Czech': 'cs',
                'Danish': 'da',
                'Dutch': 'nl',
                'English': 'en',
                'Estonian': 'et',
                'Filipino': 'fil',
                'Finnish': 'fi',
                'French': 'fr',
                'German': 'de',
                'Greek': 'el',
                'Gujarati': 'gu',
                'Hebrew': 'iw',
                'Hindi': 'hi',
                'Hungarian': 'hu',
                'Icelandic': 'is',
                'Indonesian': 'id',
                'Italian': 'it',
                'Japanese': 'ja',
                'Kannada': 'kn',
                'Korean': 'ko',
                'Latvian': 'lv',
                'Lithuanian': 'lt',
                'Malay': 'ms',
                'Malayalam': 'ml',
                'Marathi': 'mr',
                'Norwegian': 'no',
                'Polish': 'pl',
                'Portuguese': 'pt-PT',
                'Romanian': 'ro',
                'Russian': 'ru',
                'Serbian': 'sr',
                'Chinese': 'zh-CN',
                'ChinesePRC': 'zh-CN',
                'Slovak': 'sk',
                'Slovenian': 'sl',
                'Spanish': 'es',
                'Swahili': 'sw',
                'Swedish': 'sv',
                'Tamil': 'ta',
                'Telugu': 'te',
                'Thai': 'th',
                'ChineseTaiwan': 'zh-TW',
                'Turkish': 'tr',
                'Urdu': 'ur',
                'Ukrainian': 'uk',
                'Vietnamese': 'vi',
                'Welsh': 'cy'}
    
    if 'language' not in request.args or 'filename' not in request.args:
        return 'Error: Please provide a language and a filename parameter'
    
    language = request.args['language'].title()
    filename = request.args['filename']
    
    try:
        if not os.path.exists(filename) or not filename.endswith('.txt'):
            return 'Error: File not found or not a .txt file'
        
        with open(filename, 'r') as f:
            text = f.read()

        if language not in languages:
            return 'Error: Language not supported'
        
        sentences = text.split('.')

        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        translated_sentences = []
        for sentence in sentences:
            code = languages[language]
            response = requests.get(
                f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={code}&dt=t&q={sentence}')
            response.raise_for_status()  
            
            translated_sentence = response.json()[0][0][0]
            translated_sentences.append(translated_sentence)
        

        translated_text = '. '.join(translated_sentences)
        
        return translated_text
    
    except requests.exceptions.RequestException as e:
        return f'Error: {str(e)}'
    
    except IOError as e:
        return f'Error: {str(e)}'
    
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run()
