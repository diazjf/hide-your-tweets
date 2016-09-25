import os

from keystoneauth1.identity import v3
from keystoneauth1 import session
from barbicanclient import client


def get_auth():
    """Uses environmental variables to generate authentication
    credentials"""
    username = os.getenv('OS_USERNAME', None)
    password = os.getenv('OS_PASSWORD', None)
    auth = v3.Password(auth_url="http://10.0.2.15:5000/v3", username=username,
                       password=password, project_name="admin",
                       user_domain_id="default", project_domain_id="default")

    sess = session.Session(auth=auth)
    barbican = client.Client(session=sess)

    return barbican
