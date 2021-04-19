# Link-PHP-to-Backend

An app to connect Grade an Essay online using NLP and Machine Learning. This Script aims at linking PHP scripts to a strong Python backend. You can deply the Django application on cloud and generate and API. This Python API can be added to the PHP script and the data transfer can take place.

## Requirements
1) Python
2) PHP
3) Django
4) Xampp Server


## Usage
This is documentation for how to use this app.
```
STARTING THE PYTHON APP ON LOCALHOST
> cd into the folder 'Text_Analytics-master'
> pip install -r requirements.txt
> python manage.py runserver

PHP SCRIPT CONNECTING PYTHON API
> PUT the "calling.php" script to your Php server(htdocs for XAMPP).

IF YOU HAVE HOSTED THE PYTHON APPICATION AND HAVE A URL FOR THE APP
JUST REPLACE THE "127.0.0.1" STRING IN "calling.php" SCRIPT TO YOUR 
APP'S URL.

```

## Functionalities
1) The python app focuses on Grading an Essay using NLP and Machine Learning. To check that app out, you can check the "IELTS-Essay-Grader" repository.
2) The highlight is the "calling.php" script that links a python API to PHP smoothly and facilitates data exchanges between the two. So if your app is in PHP but you want strong Computations in python,you can use this script.

