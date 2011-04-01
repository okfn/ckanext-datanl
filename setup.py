from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-datanl',
	version=version,
	description="Example themeb for customising CKAN",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Seb Bacon',
	author_email='seb.bacon@gmail.com',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.datanl'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	datanl=ckanext.datanl.plugin:DataNLPlugin

        [ckan.forms]
        example_form = ckanext.datanl.package_form:get_example_fieldset
	""",
)
