#!/usr/bin/env python
# ┌─┐┬ ┬┬─┐┌─┐┬─┐┌─┐  ┌─┐┬─┐┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─
# ├─┤│ │├┬┘│ │├┬┘├─┤  ├┤ ├┬┘├─┤│││├┤ ││││ │├┬┘├┴┐
# ┴ ┴└─┘┴└─└─┘┴└─┴ ┴  └  ┴└─┴ ┴┴ ┴└─┘└┴┘└─┘┴└─┴ ┴
# A Powerful General Purpose Framework
# More information in: https://aurora-fw.github.io/
#
# Copyright (C) 2013 David Herberth
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Copyright (C) 2017 Aurora Framework
#
# This file is part of the Aurora Framework. This framework is free
# software; you can redistribute it and/or modify it under the terms of
# the GNU Lesser General Public License version 3 as published by the
# Free Software Foundation and appearing in the file LICENSE included in
# the packaging of this file. Please review the following information to
# ensure the GNU Lesser General Public License version 3 requirements
# will be met: https://www.gnu.org/licenses/lgpl-3.0.html.

"""
Aurora Framework GL Loader
----

aufw-glloader uses the official Khronos-XML specs to generate a
GL/GLES/EGL/GLX/WGL Loader made for your needs.

Checkout the GitHub repository: https://github.com/Dav1dde/glad
"""

from setuptools import setup, find_packages
import ast
import re


# Thanks flask: https://github.com/mitsuhiko/flask/blob/master/setup.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('glloader/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))


if __name__ == '__main__':
	setup(
		name='aufw-glloader',
		version=version,
		description='Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs.',
		long_description=__doc__,
		packages=find_packages(),
		install_requires=[],
		entry_points={
			'console_scripts': [
				'aufw-glloader = glloader.__main__:main'
			]
		},
		classifiers=[
			'Development Status :: 5 - Production/Stable',
			'Environment :: Console',
			'Intended Audience :: Developers',
			'Intended Audience :: Education',
			'Intended Audience :: Science/Research',
			'License :: OSI Approved :: MIT License',
			'Natural Language :: English',
			'Operating System :: OS Independent',
			'Programming Language :: Python :: 2',
			'Programming Language :: Python :: 2.7',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.4',
			'Topic :: Games/Entertainment',
			'Topic :: Multimedia :: Graphics',
			'Topic :: Multimedia :: Graphics :: 3D Rendering',
			'Topic :: Software Development',
			'Topic :: Software Development :: Build Tools',
			'Topic :: Utilities'
		],
		keywords='opengl glad generator gl wgl egl gles glx aurora framework aurorafw afw',
		author='Aurora Framework',
		author_email='auroraframework@gmail.com',
		url='https://github.com/aurora-fw/module_gengine_opengl-loader/',
		license='LGPL-3.0',
		platforms='any'
	)
