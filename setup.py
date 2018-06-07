from setuptools import setup

setup(
    name='csfashionadvice',
    version='0.1.0',
    packages=['csfashionadvice'],
    include_package_data=True,
    install_requires=[
        'flask',
        'jinja2'
    ]
)
