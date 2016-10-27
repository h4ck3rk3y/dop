**** The server side code is hosted in www.pythonanywhere.com the current account expires in august 2016
To Re Install code in pythonanywhere follow these steps
1.Create an account in pythonanywhere.com
2.Upload mysite.zip present in project files to default user folder provided on pythonanywhere
3.Open bash console in the folder where mysite.zip is uploaded
4.Decompress the compressed folder by using following command in bash console
	~ $ unzip mysite.zip
5.Open web tab in pythonanywhere
6.Click on Add a new web app link
7.Use Manual Configuration when asked for python framework and click next
8.Select python version 2.7 and click next to finish creating webapp
9.Start a new bash console from consoles tab in pythonanywhere
9.Create virtual environment named medicalApp
	~ $ source virtualenvwrapper.sh
	~ $ mkvirtualenv medicalApp
10.Now in web tab in Virtualenv slot enter the path to the virtual environment created and replace <user> with appropriate path. 
	/home/<user>/.virtualenvs/medicalApp 
11.Press start console in virtualenvironment 
12.Install the bellow packages in virtual enviroment by entering below commands in opened bash console
	~ $ pip install aiml
	~ $ pip install numpy
	~ $ pip install nltk
	~ $ pip install django
13.Now download punkt package in nltk
	~ $ python
	>>> import nltk
	>>> nltk.download()
	Downloader> d punkt
14.In web tab of pythonanywhere open wsgi configuration file and replace the code with code provided in wsgi.txt provided in project files
15.Replace sturl in onCreate() method appropriately.
