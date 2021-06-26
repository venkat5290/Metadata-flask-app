# Metadata-flask-app

# Create a script file say flask-script.sh:
#!/bin/bash -xe  
  
#Install or update Needed Software
apt update  
apt install -yq git python3 python3-pip  

#account to own server process  
useradd -m -d /home/pythonapp pythonapp
  
#cloning directory and creating a service  
git clone https://github.com/venkat5290/Metadata-flask-app.git  /opt/app  
cd /opt/app/     
cp  flask.service /etc/systemd/system/flask.service  
python3 -m pip install -r requirements.txt  
  
#Set ownership to newly created account
chown -R pythonapp:pythonapp /opt/app
  
# start and enable the service
systemctl start flask
systemctl enable flask


Change file permisiions and run the file  
chmod +x flask-script.sh
./flask-script.sh
