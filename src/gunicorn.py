import os
from pathlib import Path
from dotenv import load_dotenv

name = "Gunicorn config for FastAPI Firmware (c) Binect AG"

# Load environment.
load_dotenv()

# APPROOT must be set before this script is run.
approot = Path(os.getenv("APPROOT"))
logdir = approot / "logs"
os.makedirs(logdir.absolute(), exist_ok=True)
accesslog = str((Path(logdir) / "gunicorn-access.log").absolute())
errorlog = str((Path(logdir) / "gunicorn-error.log").absolute())

bind = "0.0.0.0:9000"

# The type of workers to use. As we use FastAPI - ASGI compatible uvicorn.
worker_class = "uvicorn.workers.UvicornWorker"
# The number of worker processes for handling requests.
workers = 2
# The maximum number of simultaneous clients.
worker_connections = 16
# The maximum number of pending connections.
backlog = 32
# The maximum number of requests a worker will process before restarting.
max_requests = 4096
# Workers silent for more than this many seconds are killed and restarted.
timeout = 120
# The number of seconds to wait for requests on a Keep-Alive connection.
keepalive = 2

debug = os.environ.get("DEBUG", "false") == "true"
reload = debug
preload_app = False
daemon = False
