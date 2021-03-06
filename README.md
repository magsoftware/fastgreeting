# Deployment of example FastAPI application

## Assumptions
1. Operating system:   CentOS 7.9
1. Firmware user name: firmware
1. Application name:   fastgreeting

## Installation instructions

### Install python and git
```bash
sudo -i
yum update -y
yum install -y python3 git
python3 -V
```

### Create user for the application runtime
```bash
useradd firmware
```

### Clone Git repo, create virtual environment and install dependencies
```bash
su - firmware
git clone https://github.com/magsoftware/fastgreeting.git
cd fastgreeting
python3 -m venv venv
source venv/bin/activate
./venv/bin/python -m pip install --upgrade pip
pip install -r requirements.txt
deactivate
```

### Install, start and enable systemd service unit file (as root user)
```bash
exit
cp /home/firmware/fastgreeting/scripts/fastgreeting.service /etc/systemd/system/
chmod 644 /etc/systemd/system/fastgreeting.service
systemctl daemon-reload
systemctl start fastgreeting
systemctl status fastgreeting
systemctl enable fastgreeting
```

# Resources
- https://www.uvicorn.org/deployment/#using-a-process-manager
- https://fastapi.tiangolo.com/deployment/server-workers/
- https://docs.gunicorn.org/en/stable/configure.html
