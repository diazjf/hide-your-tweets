#!/bin/bash

# Install Packages for Development
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y apache2 git curl vim python-pip
sudo apt-get install -y python2.7 python2.7-dev python3.4 python3.4-dev python-tox
sudo apt-get install -y libssl-dev libffi-dev

# Install other required pip packages
sudo pip install --upgrade pip
sudo pip install -r /home/ubuntu/requirements.txt

sleep 10

# Set up Devstack
git clone https://github.com/openstack-dev/devstack.git /home/ubuntu/devstack
cd /home/ubuntu/devstack
cat <<EOF > local.conf
[[local|localrc]]
disable_all_services
enable_plugin barbican https://git.openstack.org/openstack/barbican
enable_service rabbit mysql key
HOST_IP=127.0.0.1
KEYSTONE_TOKEN_FORMAT=UUID
DATABASE_PASSWORD=secretdatabase
RABBIT_PASSWORD=secretrabbit
ADMIN_PASSWORD=secretadmin
SERVICE_PASSWORD=secretservice
SERVICE_TOKEN=111222333444
LOGFILE=/opt/stack/logs/stack.sh.log
EOF
sudo chown -R ubuntu:ubuntu /opt/stack/

sleep 10

# Start Stacking
cd devstack
./stack.sh
