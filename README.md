# Hide Your Tweets #

![alt tag](src/static/images/1.jpg)

Hide Your Tweets is a sample app, providing a text encryption use case for
OpenStack Barbican. This application allows you to encrypt a short message,
which can then be directly posted to twitter. It also allows for decryption of the tweet.

## Setting Up Your Environment ##

You can run the app locally if you already have access to Keystone and
Barbican.  You can also launch a Vagrant virtual machine that will
stand up DevStack with Keystone and Barbican.

### On Host Machine ###

1. Clone the repository && `cd hide-your-tweets`.
2. (Optional) Create a virtual environment.
  `virtualenv flask_app_venv`
  `source flask_app_venv/bin/activate`
2. Install requirements. `pip install -r requirements.txt`

### Vagrant ###

In order to install the development environment needed to run this application,
you will need to install [vagrant](https://www.vagrantup.com/docs/installation/).

Once you have vagrant installed to deploy simply perform the following
commands in order:

1. Clone the Repository.
2. `cd vagrant`
3. `vagrant up` # This will take a bit, since it install devstack
4. `vagrant ssh` # If asked, Password is `vagrant`

You are now in the virtual machine. 

## Running the App ##
We can configure and start up the flask
application by performing the following:

1. `source /home/vagrant/devstack/openrc admin admin` # Source Admin Credentials from openrc file
   `source ~/openrc`
2. `SECRET=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 32)` # Generate Random String
3. `openstack secret store --payload $SECRET ` # Create a Secret
4. `export OS_SECRET_UUID=<secret_uuid>` # Set secret uuid given the href obtained in step 3
5. `cd src`
6. `python server.py`

The application is now running on your vagrant VM.

## Using the Application ##

To use the application, simply point your browser to `127.0.0.1:8000`.

## Editing the Application

To edit the application, simply edit the files in the local `/vagrant/flask-app`
directory. You will need to restart the flask web-server after each edit.

## Disclaimer ##

This is intended just for testing purposes and is not to be used for a
production system. It is by no means secure. The name of the application
is based of off the famous Hide your Kids, Hide your Wife [youtube video](https://www.youtube.com/watch?v=EzNhaLUT520).
