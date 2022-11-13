from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="HelloWorld_aline",
    version="0.0.1",
    author="Aline Gorisch",
    author_email="aline.gorisch@outlook.com",
    description="Exercício de criação de pacotes",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlineGorischF/Data-Science-Projects/tree/main/desafios_projeto_DIO/boot_geracao_tech_unimed_DS/package-helloworld-aline"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)