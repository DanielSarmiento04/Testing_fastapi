# Testing The FastApi framework

with the past day, I read in forums that FastApi is poweful and fast framework for create apis and some basic websites

With this context, this repository contains the a example of a api  for manage a small store, actually, it  would be neccesary to implement a secure token system

## Init
1. Create virtual enviaroments:

    Win
 <pre>python -m venv .venv</pre>
 linux/MacOs
 <pre>python3 -m virtualenv .venv</pre>
Or using anaconda 
 <pre>conda create --name .venv python=3.10 --yes</pre>

2. Activate the virtual environment

    Win
 <pre>.venv/Scripts/activate</pre>
 linux/MacOs
 <pre>source .venv/bin/activate</pre>
Or using anaconda 
 <pre>conda ativate .venv</pre>

3. Download the requirements  from requirements.txt


    Win/Conda
 <pre>python -m pip install -r requirements.txt</pre>
 linux/MacOs
 <pre>python3 -m pip install -r requirements.txt</pre>



## References
1. [Pydantic](https://pydantic-docs.helpmanual.io/usage/models/)
2. [FastAPI](https://fastapi.tiangolo.com/features/)