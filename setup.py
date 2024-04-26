from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='NetHyTech-TTS',
    version='0.2',
    author='Anubhav Chaturvedi',
    author_email='chaturvedianubhav520@example.com',
    description='Text To Speech In British Brian Voice',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Anubhavchaturvedi/NetHyTech-TTS',
    project_urls={
        'Source Code': 'https://github.com/AnubhavChaturvedi-GitHub/',
        'Demo Video': 'https://www.youtube.com/channel/UC7YDMgu0dMRZotLMuB3oEcQ'
    },
    packages=find_packages(),
    install_requires=[
        'selenium',
        'webdriver_manager',
    ],
    entry_points={
        'console_scripts': [
            'NetHyTech-TTS = my_package.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
