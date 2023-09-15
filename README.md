# mejuri_python
This is a dedicated site for testing - https://mejuri.com/world/en/  
Autotests for the product catalog page.  
The user is supposed to log in, then to find the product Honey Mini Signet in the catalog of rings and add it to favorites in the shopping cart.

Runnig:\
Create venv\
pip install -r requirements.txt\
Run tests from root directory by\
'pytest --maximize --browser firefox' or 'pytest --maximize --browser chrome' command\
After pytest runnig logs are available in /logs directory.

For allure:
allure generate allure-results -c
allure open .\allure-report\

[Demo video](https://youtu.be/ztAzrR3VXmE)
