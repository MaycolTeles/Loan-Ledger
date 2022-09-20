### Creating and Activating the Virtual Environment 
It is recommended to install the dependencies inside a [virtualenv](https://docs.python.org/3/tutorial/venv.html). So, inside the folder where you cloned the repository, create a new virtualenv:

```
python3 -m virtualenv venv
```

Then, activate the virtualenv (for Linux/MacOS):

```
source venv/bin/activate
```

or (for Windows):

```
venv\Scripts\activate
```

### Installing Dependencies
To install all the necessary project dependencies, run the following command in the terminal:

<b>Make sure that you're running it from your current activated virtual environment! </b>

```
pip install -r requirements.txt
```