from distutils.core import setup

setup(
    name='django-mongorunner',
    version='0.1',
    description='Django testrunner for mongoengine',
    author='Marcus Carlsson',
    author_email='carlsson.marcus@gmail.com',
    url='https://github.com/xintron/django-mongorunner',
    packages=[
        'mongorunner',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
