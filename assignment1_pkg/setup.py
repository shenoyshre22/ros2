from setuptools import find_packages, setup

package_name = 'assignment1_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arc',
    maintainer_email='arc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'pub_one = assignment1_pkg.publisher_one:main',
        'pub_two = assignment1_pkg.publisher_two:main',
        'listener = assignment1_pkg.listener:main',
        ],
    },
)
