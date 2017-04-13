**Exploration**

- Protractor (tested docker image, had some issue with the chrome driver, I won't go into javascript for now)
- I have a Vagrant machine, next is docker? :)
- report - junit might be enough

- configure environment (develop some tricks)
- check to see if behave can have the configuration file overwritten based on location, if not implement something in the framework
- I can have a behave.ini at root, then override it in each app_name, or even at features sub-folders if I go that way

- tear up and down (clean up for the down at least)
- reading expected and actual data from external csv

- should I add a setup.py, could be usefully if I want on the ci to create a python env and pip the automation in it.
- using setup.py standard tools, instead of cloning the repository and running the setup commands?

- On the framework area still between:
- I am not entirely sure that the Pages classes should do any actions on elements, except returning them 
- feels more like a step responsibility to decide what to do with the elements returned by Pages

- create metaclass - autoregistry (google: python Meta class that lets load plugins. Zope is one framework, this is light: https://gist.github.com/will-hart/5899567)
- sa incarc datele de test din fisiere externe csv si sa fac convertere de behave in care sa fac maparea cu coloane din fisiere.
- I should package it separatly and publish on github, extend the behave configs
