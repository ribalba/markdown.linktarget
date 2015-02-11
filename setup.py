from distutils.core import setup

setup(
    name='MarkdownLinkTaget',
    version='0.1.0',
    packages=['MarkdownLinkTaget',],
    license='Apache License 2.0',
    long_description=open('README.txt').read(),
    url='https://github.com/ribalba/markdown.linktarget',
    description='Adds a taget="_blank" attribute to HTML links in Markdown',
    author='Didi Hoffmann',
    author_email='didi@ribalba.de',
    install_requires=[
        "Markdown >= 2.3.1",
    ],
)