from setuptools import setup

setup(
    name="discli",
    version='0.1.dev1',
    description="A ",
    author="Tim Penhey",
    author_email="tim@canonical.com",
    scripts=["discli"],
    license='MIT',
    python_requires=">= 3.4",
    install_requires=[
      "requests>=2.22",
      "PyYAML>=5.1",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
    ]
)
