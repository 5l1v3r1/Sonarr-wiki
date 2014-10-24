from setuptools import setup, find_packages


setup(
    name='sonarr',
    version="1.0",
    description='Documentation for sonarr',
    #long_description=readme,
    author_email='hello@sonarr.tv',
    url='http://wiki.sonarr.tv',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)