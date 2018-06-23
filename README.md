# Item Catalog
With this program is possible to create, read, update and delete an item.
All items are related with categories previously  registered.
In this first version isn't possible to create, update and delete a new category.
There are JSON endpoints for GET methods (read), for other operations just by navigating
through the web browser.
## Requirements
* Python 3.5.2
  [download here](https://www.python.org/downloads/)
* Vagrant 1.8.5
  [download here](https://www.vagrantup.com/downloads.html)
## How to run
* Install Python 3.5.2
* Install Vagrant 1.8.5
* Clone or Download the follow repository from Udacity:

  `https://github.com/udacity/fullstack-nanodegree-vm`

* In fullstack-nanodegree-vm execute these cmd commands:

  `cd vagrant`

  `vagrant up`

  `vagrant ssh`

* Clone this repository using these git commands:

  `git init`

  `git clone https://github.com/marcelo-almeida/Item_catalog.git`

* Create an account in google developers

    [https://console.developers.google.com/apis]

* Create a new OAuth client ID: when you creating, please define a name to client,
fill the field `Authorized Javacript origins` with `http://localhost:8080` and
the field `Authorized redirect URIs` with:

  `http://localhost:8080/login`

  `http://localhost:8080/connect`

  `http://localhost:8080/disconnect`

note: Don't forget is one per line
* Download you client secret by clicking in `DOWNLOAD JSON` in your google developers account.
* Rename the file to `client_secrets.json` and replace the same file in this project.
* Copy the project to vagrant directory
* init a new vagrant session `vagrant ssh` in a terminal
* From a vagrant terminal execute these command to create the database and fill
with categories:
  `python database_config.py`

  `python fill_database.py`

* Again from a vagrant terminal execute this command to init a server http:
  `python run.py`

* Access in a web browser `http://localhost:8080` to interact with the catalog
## Copyright
It was used the vagrant config from udacity repository

  [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)

For the OAuth2/google logic is based in udacity's material:
  [OAuth2](https://github.com/udacity/OAuth2.0)