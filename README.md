# This is a ToDO website made with Django
This a web application where a user can login and create the tasks, this was built with the [Django](https://www.djangoproject.com/) web application framework

A running instance of it can be found at " 
[https://my--todo.herokuapp.com/](https://my--todo.herokuapp.com/) ".

## :heavy_check_mark: This a basic project for learning Django3
## Resources:
  * [Django (3.0) Crash Course Tutorials | Customer Management App](https://youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
  * [To Do App | Django 3.0](https://youtu.be/4RWFvXDUmjo)

# :book: How to use the repository?
## :gear: Setup

#### **First we have to create virtual environments**

### On Windows: 
```cmd
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```

### On macOS and Linux:
```bash
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```
### Leaving the virtual environment
```bash
deactivate
```
### After setting up virtual environment do this!
``` bash
git clone https://github.com/Saketh-Chandra/My_ToDO.git
cd My_ToDO
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# :whale: Using Docker Compose

In production, Django uses a WSGI server such as Gunicorn and a web server such as Nginx.

### Architecture:
 ![Request Flow](https://user-images.githubusercontent.com/46235445/129321910-9dbfa7d3-395d-41f7-8400-eba90c77605e.png)
<div align="center">
 <h3>Request Flow Diagram</h3>
</div>

### :gear: Setup .env file
   - #### Edit the .env file
```Shell
## .env file, Don't Share it with anyone!

SECRET_KEY='e^$9mt#)3niaz9b9pyxc1x(53&qq1^@iuy2)=5hhji1t+*o_0$'
DEBUG=False

## Super-User Credentials
SUPER_USER_NAME = 'root'
SUPER_USER_PASSWORD = 'root'
SUPER_USER_EMAIL = 'admin@email.com'
```


### Usage

``` Shell
git clone https://github.com/Saketh-Chandra/My_ToDO.git
cd My_ToDO
docker-compose up -d
```

Run services in the background:
`docker-compose up -d`

Run services in the foreground:
`docker-compose up --build`

Inspect volume:
`docker volume ls`
and
`docker volume inspect my_todo_static`

View networks:
`docker network ls`

Bring services down:
`docker-compose down`



# :octocat: How to contribute?

All contributions are welcome! Code, documentation, graphics or even design suggestions are welcome; use GitHub to its fullest. Submit pull requests, contribute tutorials or other wiki content -- whatever you have to offer, it would be appreciated!

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on contributing.



# :scroll: License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


See the full list of [contributors](https://github.com/Saketh-Chandra/flask_basic/graphs/contributors) who participated in this project and statistics.

# :heavy_exclamation_mark: Prerequisites aka requirements

Please read [Prerequisite](Prerequisite.md) file for details.

# :scroll: Changelog

Check the [changelog here](https://github.com/Saketh-Chandra/My_ToDO/commits/master).

# :scroll: I found some bugs or issues. Where do I report?

Report [here](https://github.com/Saketh-Chandra/My_ToDO/issues/new) in detail answering these questions:

* What steps did you take to make the bug appear?
* How can the bug be fixed? (In case you know)
* Which OS and which all packages / softwares / dependencies are you using?
* Have you tried any troubleshooting steps such as a reboot for example?
* Have you followed the prescribed prerequisites?

# :scroll: How do I contact the team?

Check [here](https://github.com/Saketh-Chandra/My_ToDO/graphs/contributors) for the list of contributors. Contact one of them through their profiles.
