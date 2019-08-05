# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import sys
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(here, 'kernel_gateway', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup_args = dict(
    name='dlhub_gateway',
    author='dlhub.app (Originally by Jupyter Development Team)',
    author_email='dlhub.app@gmail.com',
    url='https://github.com/dlhub-app/dlhub_gateway',
    download_url = 'https://github.com/dlhub-app/dlhub_gateway/archive/1.0.0.tar.gz',
    description='A web server for spawning and communicating with Jupyter kernels',
    long_description='''\
DLHub Gateway is just a copy of the official Jupyter Kernel Gateway with minor changes to make it
more easy-to-use for DLHub.app users. The majority of the files in this repository is exactly an
unchanged copy from jupyter/kernel_gateway repository. We have just changed few files to make it
more accessible, especially for our Windows users.
''',
    version=version_ns['__version__'],
    license='BSD',
    platforms="Linux, Mac OS X, Windows",
    keywords=['DLHub', 'Interactive', 'Interpreter', 'Kernel', 'Web', 'Cloud'],
    packages=[
        'kernel_gateway',
        'kernel_gateway.base',
        'kernel_gateway.jupyter_websocket',
        'kernel_gateway.notebook_http',
        'kernel_gateway.notebook_http.cell',
        'kernel_gateway.notebook_http.swagger',
        'kernel_gateway.services',
        'kernel_gateway.services.kernels',
        'kernel_gateway.services.kernelspecs',
        'kernel_gateway.services.sessions',
    ],
    scripts=[
        'scripts/dlhub-gateway'
    ],
    install_requires=[
        'jupyter_core>=4.4.0',
        'jupyter_client>=5.2.0',
        'notebook>=5.7.6,<6.0',
        'traitlets>=4.2.0',
        'tornado>=4.2.0',
        'requests>=2.7,<3.0',
        'numpy',
        'pandas',
        'sklearn',
        'tensorflow'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    include_package_data=True,
)

if 'setuptools' in sys.modules:
    # setupstools turns entrypoint scripts into executables on windows
    setup_args['entry_points'] = {
        'console_scripts': [
            'dlhub-gateway = kernel_gateway:launch_instance'
        ]
    }
    # Don't bother installing the .py scripts if if we're using entrypoints
    setup_args.pop('scripts', None)

if __name__ == '__main__':
    setup(**setup_args)
