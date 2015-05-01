#Centre for Organic Electronics Website

##Requirements

* Python version >= 2.7.6
* pip >= 1.5.4

##Installation

Using pip install virtualenv and virtualenvwrapper. These allow for easy use of a local virtualenvironmet to do all of the development. This ensures when the app is deployed it won't break.

```bash
pip install virtualenv
pip install virtualenvwrapper
```

Then call the shell script virtualenvwrapper.sh

```bash
source virtualenvwrapper.sh
```

Now create the virtual environment and the use 'workon' to change into the virtualenv:

```bash
mkvirtual env coe_website
workon coe_website
```
Once in the local environment the dependencies of the app need to be installed. This is easily done using pip and the 'requirements.txt' file located in the project's top directory.

```bash
pip install -r requirements.txt

```
