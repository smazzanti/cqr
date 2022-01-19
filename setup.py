from setuptools import setup

setup(
    name='cqr',
    version='0.2.0',
    description='d',
    url='https://github.com/smazzanti/cqr',
    author='Samuele Mazzanti',
    author_email='mazzanti.sam@gmail.com',
    license='MIT',
    packages=['cqr'],
    install_requires=[
        'jinja2',
        'tqdm',
        'joblib',
        'pandas>=1.0.3',
        'numpy>=1.18.1',
        'sklearn',
        'category_encoders'
    ],
    zip_safe=False
)
