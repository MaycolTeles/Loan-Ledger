# Ampla Engineering Take-home Exercise

## Loan Ledger
This repository contains the implementation of the Ampla Engineering challenge proposal.

To have a better understand about the proposal, check [this file here](project_description.md)

*********************

## Summary

* [Requirements](#requirements)
* [Setup and Installation](#setup-installation)
* [How to Use](#how-to-use)
* [Final Considerations](#final-considerations)

*********************
## Requirements <a name="requirements"></a>

* [Python 3.6+](https://www.python.org/)
* Pip 20.0+ (comes with Python 3)

*********************
## Setup and Installation <a name="setup-installation"></a>

### Cloning this repository
First off, in order to get a copy of the project to run it/test it, clone the repository into a folder in your machine:

```
git clone git@github.com:MaycolTeles/Loan-Ledger.git
```

### Creating the Virtual Environment and Installing Dependencies

It is recommended to install the dependencies inside a [virtualenv](https://docs.python.org/3/tutorial/venv.html). Usually, you'd need to create a virtual environment, then activate it, and finally install all the dependencies. But in this case, there's a `Makefile` to help you with all of that.

So, to set up the environment and install everything, first make sure that you are in the same directory of the `Makefile` file (i.e.: cd path/to/project/Loan-Ledger)

Now, just type the following command in the terminal of your preference, and the whole environment will be set up.

```
make
```

This command will:
* Create a new virtual environment;
* Activate it;
* Install all the dependencies from "requirements.txt";
* Execute all the tests directly.

If, by any chance, this command doesn't work, you'll need to create a virtual environment all by yourself.

<b>But no worries!</b> Just follow [this guide](set_up_virtual_environment.md) and you'll be fine!

*********************

## How To Use <a name="how-to-use"></a>

If you want to run a specific test or just play with the app, simple run:

```
python cli.py
```

This command will display some options for you, which you can check what they do and their expected behavior following this [project description file](project_description.md)


### Note
In case this command doesn't work, make sure that you are running it with your virtual environment activated!

*********************

## Final Considerations <a name="final-considerations"></a>

If you want to contribute or have a better understand about the code, please make sure to check the documentation [here](https://maycolteles.github.io/Loan-Ledger/docs/src/index.html)