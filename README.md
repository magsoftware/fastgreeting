# fastgreeting
Sample deployment of FastAPI application

https://www.uvicorn.org/deployment/#using-a-process-manager
https://fastapi.tiangolo.com/deployment/server-workers/
https://docs.gunicorn.org/en/stable/configure.html


adduser firmware
python3 -m venv venv
source venv/bin/activate
./venv/bin/python -m pip install --upgrade pip
pip install -r requirements.txt


export PYTHONPATH=`pwd`/src
uvicorn main:app --reload
