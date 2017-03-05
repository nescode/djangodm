## Multi-Vendor Digital Marketplace Platform(Early stage development)

This project is an attempt to develop a Multi-vendor digital marketplace platform on top of Django Framework and offer sellers to register, upload and sell their digital images. Development is still is early stages and not recommended for production use. Pull request with fixes and enhancements are most welcome, though.

## Features
* Products
* Curated Products
* My product
* Products rating
* Image Thumbnail
* Sellers
* Seller dashboard
* Seller side option for product management
* Admin dashboard
* Basic analytics
* Tags

## Installation

Post setting up virtualenv Run the following commands. In case you would like know how to setup virtualenv, browse through [Configure virtualenv and virtualenvwrapper](http://www.sunilsrikumar.com/2016/03/django-multi-site-setup/)

```
git clone https://github.com/nescode/djangodm.git
cd djangodm
pip install -r requirement.txt
python manage.py migrate
python manage.py runserver
```
The Multi-vendor Marketplace will be now accessible at http://127.0.0.1:8000/ and the admin interface
at http://127.0.0.1:8000/admin/ . To login into admin panel create a superuser:

```
python manage.py createsuperuser
```
Give your username, email id and password to complete the user creation process.

## Paid development

We love Python and Django because of its flexibility and clean code. We offer customized application development using Django. Just say hello at info@nescode.com to start a discussion.

## Django development company

We are passionate technologists. We offer full stack development and consulting for organizations
with Python, Django framework, Wagtail and PostgreSQL. Drop us a line at info@nescode.com to shape your idea.
