from setuptools import setup

setup(
    name="Moodipy",
    version="0.9.1",
    packages=['Moodipy',],
    url="https://github.com/dianas11xx/Moodify",
    author="Noteworthy",
    license = "GPL 3",
    python_requires = '==3.8',
    package_data = {"Moodipy":['imgs/awful.jpeg', 'imgs/arrow.png', 'emotions.txt']},
    description="use sentiment analysis to create a playlist that matches someone's mood and also predict songs to rise in popularity.",
    install_requires=["spotipy>=2.18", "nltk>=3.6.2", "pyqt5>=5.12","screeninfo>=0.6.5", "requests"],
    entry_points={"console_scripts": ["start_Moodipy=Moodipy.main:main"]},
    include_package_data=True
)
