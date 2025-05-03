from setuptools import setup, find_packages

setup(
    name="django-delegating-manager-and-queryset",
    version="1.0.0",
    packages=find_packages(),
    description="Provides typed subclasses of Django's Manager and QuerySet to improve type checking and autocomplete, without altering runtime behavior.",
    author="Louis Thompson",
    author_email="104149942+L-Pson@users.noreply.github.com",
    python_requires=">=3.8",
)