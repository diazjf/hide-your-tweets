import os

from keystoneauth1 import identity
from keystoneauth1 import session
from oslo_context import context


def get_context():
    """Uses environmental variables to generate authentication
    credentials"""
    username = os.getenv('OS_USERNAME', None)
    password = os.getenv('OS_PASSWORD', None)
    auth_url = os.getenv('OS_AUTH_URL', None) + '/v' + os.getenv('OS_IDENTITY_API_VERSION', None)
    project_name = os.getenv('OS_PROJECT_NAME', None)

    auth = identity.V3Password(auth_url=auth_url,
                               username=username,
                               password=password,
                               project_name=project_name,
                               user_domain_name="default",
                               project_domain_name="default")
    sess = session.Session(auth=auth, verify=False)
    return context.RequestContext(auth_token=auth.get_token(sess),
                                  tenant=auth.get_project_id(sess))
