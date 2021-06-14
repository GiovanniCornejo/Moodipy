from setuptools import setup
#general idea for setup
setup(
    name="Moodipy",
    version="0.1",
    packages=["Moodipy", "GUI"],
    url="https://github.com/dianas11xx/Moodify/",
    author="Noteworthy",
    description="use sentiment analysis to create a playlist that matches someone's mood and also predict songs to rise in popularity.",
    install_requires=["python3.8", "Ubuntu", "PyQt5"],
    entry_points={"console_scripts": ["start_Moodipy=Moodipy:main"]}
)
