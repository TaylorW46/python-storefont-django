# python-storefont-django
Creates a simple HTML webpage using Python, VSCode, and Django

*SETTING UP ENVIRONMENT*
Open your terminal (CMD for Windows).
First download the latest version of python from the website and verify that its downloaded 
successfully using python --version (python3 --version on Mac). 


Then install pipenv (Open the terminal in VSCode and type pip3 install pipenv (CMD, zsh, or Powershell is fine))
![image](https://user-images.githubusercontent.com/40469463/229387847-fff387bd-a9e8-44fe-9088-51719531d84a.png)


Change directory to whichever folder you want to store your project in (I did it in the Desktop). 
Then install django. (pipenv install django)
![image](https://user-images.githubusercontent.com/40469463/229388495-62e638be-2260-4394-b0bf-e5459323c778.png)


If done correctly, you should have two files in your directory (Pipfile and Pipfile.lock)
![image](https://user-images.githubusercontent.com/40469463/229389319-44d7352f-d0b6-4198-9cb7-0ceb6782f180.png)


Next we want to activate the virtual environment, so well use the python interpreter inside this virtual environment.
Not the one installed globally. Run this command
![image](https://user-images.githubusercontent.com/40469463/229389455-7a68594e-1491-4966-bf73-f73a02a52ed9.png)


Then use the Django-admin startproject <projectname>.
![image](https://user-images.githubusercontent.com/40469463/229389677-87ebfe23-33a5-47db-8dbb-c1f9834d1565.png)


Now in the project folder you should have these files.
![image](https://user-images.githubusercontent.com/40469463/229389664-e33fcb8d-b183-4b02-b90d-ac5ef0f07c89.png)

*RUNNING A WEBSERVER*
Now we want to run a web server. Another command that django provides is runserver.
When we run python manage.py, we see the same commands django-admin provides.
![image](https://user-images.githubusercontent.com/40469463/229390247-2755a826-af19-4535-b6de-36528038c86c.png)

Run python manage.py runserver <portnumber>
![image](https://user-images.githubusercontent.com/40469463/229390411-8fd53bf8-6296-45b7-9eab-a6216f6fe9bd.png)


 Copy the http link and voila! You have your first Django server up and running


![image](https://user-images.githubusercontent.com/40469463/229390393-da377972-c712-467b-8c75-0a4c1303943c.png)




