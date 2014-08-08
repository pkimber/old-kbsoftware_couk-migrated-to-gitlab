import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='pkimber-kbsoftware-couk',
    packages=['settings', 'web', 'web.tests', 'dash', 'dash.tests', 'project', 'project.management', 'project.management.commands'],
    package_data={
        'dash': [
            'templates/*.*',
            'templates/dash/*.*',
        ],

        'web': [
            'templates/*.*',
            'templates/web/*.*',
        ],

        'project': [
            'static/*.*',
            'static/img/*.*',
            'static/img/project/*.*',
            'templates/*.*',
            'templates/project/*.*',
        ],
    },
    version='0.0.04',
    description='KB Software Ltd',
    author='Greg Bushell',
    author_email='greg@kbsoftware.co.uk',
    url='git@github.com:pkimber/kbsoftware_couk.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)