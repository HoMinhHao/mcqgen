from setuptools import setup, find_packages

setup(
    name="mcrganerator",
    version="0.0.1",
    author="Hao Ho-Minh",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv","PyPDF2", "langchain_community", "huggingface_hub"],
    packages=find_packages()
)