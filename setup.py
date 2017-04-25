from setuptools import setup

setup(name='agent-for-sre',
	version='0.0.22',
	description='The agent for sre',
	url='http://no.website/',
	author='niht',
	author_email='5007088@qq.com',
	license='GPLv3',
	packages=['agent_for_sre'],
	package_data={'agent_for_sre': ['*.py','Conf/*.py','Collector/*.py','Monitor/*.py','sample/*.*']},
	install_requires=[
		'psutil'
	],
	zip_safe=False)
