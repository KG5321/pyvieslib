import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = 'pyvieslib',
    packages = ['pyvieslib'],
    version = '0.8.0',
    license='MIT',
    description = 'Library for VIES number validation',
    author = 'KG5321',
    author_email = 'konradgebler1@gmail.com',
    url = 'https://github.com/KG5321/pyvieslib',   
    download_url = 'https://github.com/KG5321/pyvieslib/archive/0.5.tar.gz',
    keywords = ['vies', 'nip', 'validation', 'eu', 'vat', 'number'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',      
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
    ]
)