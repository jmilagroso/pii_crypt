from setuptools import setup
setup(
    name='pii_crypt',
    packages=['pii_crypt'],
    version='1.0.1',
    license='MIT',
    description='Secures Personally Identifiable Information using AES (128/256 bit) key encryption.',
    author='Jay Milagroso',
    author_email='j.milagroso@gmail.com',
    url='https://github.com/jmilagroso/pii_crypt',
    download_url='https://github.com/jmilagroso/pii_crypt/releases',
    keywords=[
        'PII',
        'AES',
        'Security'],
    install_requires=['pycryptodome'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
