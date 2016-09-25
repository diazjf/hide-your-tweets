#!/bin/bash

# Install Packages for Development
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y apache2 git curl vim python-pip
sudo apt-get install -y python2.7-dev python3.4 python3.4-dev python-tox
sudo apt-get install -y libssl-dev libffi-dev ebtables

# Install other required pip packages
sudo pip install Flask==0.10.1
sudo pip install Flask-WTF==0.12
sudo pip install WTForms==2.1

sleep 10

# Setup Devstack
git clone -b stable/mitaka https://github.com/openstack/barbican.git /opt/stack/barbican
# Copy Over Patch
sudo rm -rf /opt/stack/barbican/barbican/plugin/crypto/simple_crypto.py
sudo cp /home/vagrant/simple_crypto.py /opt/stack/barbican/barbican/plugin/crypto/simple_crypto.py
sudo rm -rf /home/vagrant/simple_crypto.py
git clone https://github.com/openstack-dev/devstack.git /home/vagrant/devstack
cd /home/vagrant/devstack
cat <<EOF > local.conf
[[local|localrc]]
disable_all_services
enable_plugin barbican https://git.openstack.org/openstack/barbican
enable_service rabbit mysql key
KEYSTONE_TOKEN_FORMAT=UUID
DATABASE_PASSWORD=secretdatabase
RABBIT_PASSWORD=secretrabbit
ADMIN_PASSWORD=secretadmin
SERVICE_PASSWORD=secretservice
SERVICE_TOKEN=111222333444
LOGFILE=/opt/stack/logs/stack.sh.log
EOF
sudo chown -R vagrant:vagrant /opt/stack/

sleep 10

# Start Stacking
cd devstack
./stack.sh
