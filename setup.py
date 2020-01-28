from setuptools import setup

setup(
    name='VolcaFMVel',
    version='0.1',
    packages=['VolcaFMVel'],
    url='https://github.com/Olly000/VolcaFMVel',
    license='',
    author='Olly000',
    author_email='',
    description='Provides note on velocity to Volca FM from external MIDI keyboard',
    install_requires=[
        'mido',
        'pygame'
    ]
)
