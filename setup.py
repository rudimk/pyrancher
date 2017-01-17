from setuptools import setup

setup(name='pyrancher',    
    version='0.1',
    description="A Python wrapper around Rancher's API.",
    url='https://github.com/rudimk/pyrancher',
    author='Rudraksh MK',
    author_email='rudraksh.mk@gmail.com',
    license='MIT',
    packages=['pyrancher'],
    install_requires=[
        'requests',
    ],
    zip_safe=False)