import setuptools


with open("README.md","r",encoding="utf-8", errors="ignore") as fh:
	long_description = fh.read()

with open("requirements.txt","r",encoding="utf-8") as requirements:
	required = requirements.read().splitlines()

setuptools.setup(
	name="pytwitterscraper",
	version="1.3.3-6",
	author="M-307",
	author_email="contact@m-307.tk",
	description="Twitter Scraper using Python",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/mrwan200/pytwitterscraper",
	keywords = ['pytwitterscraper', 'twitterscraper', 'webscraper','apiscraper'],
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	install_requires=required,
	python_requires=">=3.6",
	data_files=[('lib/site-packages/pytwitterscraper', ['pytwitterscraper/user_agent.json'])]
)
