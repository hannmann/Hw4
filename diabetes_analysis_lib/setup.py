from setuptools import setup, find_packages

setup(
    name='diabetes_analysis_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        # Add other dependencies if necessary
    ],
    description='A library for preprocessing, training, and evaluating models for diabetes analysis',
    author='Your Name',
    author_email='your.email@example.com'
)
