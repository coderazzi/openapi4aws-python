from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='openapi4aws',
    py_modules=['openapi4aws'],
    version='1.2.1',
    description='utility to enrich an openapi specification with information '
                'specific for the AWS API Gateway',
    author='coderazzi (LuisM Pena)',
    author_email='coderazzi@gmail.com',
    url='https://coderazzi.net/python/openapi4aws',
    long_description=readme(),
    keywords=['openapi', 'aws', 'api-gateway'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=['pyyaml'],
    python_requires='>=3.7',
    project_urls={
        'Website': 'https://coderazzi.net/python/openapi4aws/index.html',
        'Source': 'https://github.com/coderazzi/openapi4aws-python',
        'Tracker': 'https://github.com/coderazzi/openapi4aws-python/issues',
    },
)
