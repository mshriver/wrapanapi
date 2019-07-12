from __future__ import absolute_import
from setuptools import setup

setup(
    setup_requires=['pbr'],
    pbr=True,
    packages='wrapanapi',
    python_requires='>=2.7, !=3.4.*, !=3.5.*, !=3.6.*, <4.0',
    extras_require={
        'testing': [
            'azure-cosmosdb-table',
            'coveralls',
            'mock',
            'pytest',
            'pytest-cov',
            'pytest-mock',
            'pytest-variables',
        ]
    },
    install_requires=[
        'azure>=3.0.0',
        'azure-storage-common>=1.0',
        'boto3==1.6.6',
        'botocore==1.9.6',
        'boto',
        'cached_property',
        'dateparser',
        'enum34; python_version == "2.7"',
        'fauxfactory>=2.0.7',
        'google-api-python-client',
        'google-compute-engine',
        'inflection',
        'miq-version>=0.1.6',
        'oauth2client',
        'ovirt-engine-sdk-python~=4.3',
        'openshift==0.3.4',
        'packaging',
        'pyvmomi>=6.5.0.2017.5.post1',
        'python-cinderclient',
        'python-swiftclient',
        'python-glanceclient',
        'python-ironicclient',
        'python-keystoneclient',
        'python-neutronclient==6.12.0',
        'python-novaclient==7.1.2',
        'python-heatclient',
        'pyvcloud==19.1.2',
        'py3winrm==0.0.1',
        'redfish-client==0.1.0',
        'requests',
        'six',
        'tzlocal',
        'vspk==5.3.2',
        'wait_for',
        'websocket_client',
        # suds jurko supports python3, suds is only used on python2
        'suds-jurko; python_version > "3.0"',
        'suds; python_version == "2.7"',
        # lxml super SGML parser, needs libxml2-devel and libxslt-devel
        'lxml',
    ]
)
