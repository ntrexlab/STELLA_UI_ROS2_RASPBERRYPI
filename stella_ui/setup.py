import os
from glob import glob
from setuptools import setup

package_name = 'stella_ui'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('lib', package_name), glob(package_name + '/rtmgr.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Gyuha Kang',
    maintainer_email='kgh@ntrex.co.kr',
    description='STELLA UI node',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stella_ui_node = stella_ui.stella_ui_dialog:main',
        ],
    },
)
