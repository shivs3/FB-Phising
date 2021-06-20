# FB-Phising
#Project: PHISING (Facebook Phising)
#Introduction
Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message. The recipient is then tricked into clicking a malicious link, which can lead to the installation of malware, the freezing of the system as part of a ransomware attack or the revealing of sensitive information.


#Project Structure
In this project, I created a facebook login page to get user credentials.
Following Steps were involved:
	Facebook login page was created using HTML and CSS
	Backend created using python Django framework.
	For database PostgreSQL was used
	After the user login to this page, the data is saved to database where I can get the information.

#REQUIREMENTS:
Frontend: HTML, CSS
Backend: Python, Django
Database: PostgreSQL
Server: http://127.0.00.1:8000


#How to Use the system:
1)	Clone the repository using following command
git clone https://github.com/shivs3/FB-Phising.git
2)	Create virtual environment using following command
python –m venv venv
3)	Activate venv
4)	Install all the requirements using following command
pip install –r requirements.txt
5)	Run the following commands to make migration for databse
Python manage.py makemigration
Python manage.py migrate

NOTE: Before making migration install pgadmin and create a new databse with name ‘phising’ and use  5432 port.
6)	Run the following command to run the server
Python manage.py runserver
7)	Go to the link : http://127.0.00.1:8000 , the login page will appear. The credentials will be saved every time a user login the page.
