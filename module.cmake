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

set(AURORAFW_GLLOADER_OUT_DIR "${CMAKE_CURRENT_BINARY_DIR}")
find_package(PythonInterp REQUIRED)

set(AURORAFW_GLLOADER_PROFILE "" CACHE STRING "OpenGL profile")
set(AURORAFW_GLLOADER_API "3.3" CACHE STRING "API type/version pairs, like \"gl=3.2,gles=\", no version means latest")
set(AURORAFW_GLLOADER_GENERATOR "c" CACHE STRING "Language to generate the binding for")
set(AURORAFW_GLLOADER_EXTENSIONS "" CACHE STRING "Path to extensions file or comma separated list of extensions, if missing all extensions are included")
set(AURORAFW_GLLOADER_SPEC "gl" CACHE STRING "Name of the spec")
set(AURORAFW_GLLOADER_NO_LOADER OFF CACHE BOOL "No loader")
set(AURORAFW_GLLOADER_EXPORT ON CACHE BOOL "Set export variables for external project")
set(AURORAFW_GLLOADER_INSTALL OFF CACHE BOOL "Generate installation target")
