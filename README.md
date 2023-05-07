# TranslatorApi


# Installation Guide #


1. DOCKER:

1.1 Pull from Docker-Hub 

$docker pull imwish/translator_api

$docker run -p 5000:5000 -it --name Translator-Api imwish/translator_api

or

1.2 Build

clone this repository then switch to it.

$docker build -t translator_api:v2 .

$docker run -p 5000:5000 -it --name Translator-Api translator_api:v2

OR 

2. SYSTEM:
clone this repository then switch to it.

$pip install -r requirements.txt

$python app.py

2.1 Virtual ENViroment 

Its good practice to use seprate vm for your project,

$python3 -m venv translator_venv

then,

$source translator_venv/bin/activate

$pip install -r requirements.txt

$python app.py

make sure you are in project directory.


THEN

~Usage:


http://127.0.0.1:5000/translate?language= #language_to_translate &filename= #path/to/file/inputfile.txt


127.0.0.1:5000

here 127.0.0.1 is the loopback IP address, also known as localhost,
URL used to access a web application running on the local machine at port 5000.
you can modify/change it accordingly.

Example :
if you have created Docker container from Docker file 

http://172.17.0.2:5000/translate?language=french&filename=/app/myfile.txt

else 

http://127.0.0.1:5000/translate?language=french&filename=/home/wish/Documents/Do-Translator-API/myfile.txt

http://localhost:5000/translate?language=french&filename=/home/wish/Documents/Do-Translator-API/myfile.txt

here language=french we specified language
  
here filename=/home/wish/Documents/Do-Translator-API/myfile.txt it is the file path we spacified.

