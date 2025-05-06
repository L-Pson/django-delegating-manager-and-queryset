from setuptools import setup, find_packages

setup(
    name="django-delegating-manager-and-queryset",
    version="1.0.1",                    # bump version
    packages=find_packages(),
    include_package_data=True,          # <-- allow package_data
    package_data={
        "django_delegating_manager_and_queryset": ["py.typed"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Typing :: Typed",             # <-- PEP 561 marker for PyPI
    ],
    install_requires=["Django>=3.2"],
)