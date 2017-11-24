from glloader.lang.common.loader import BaseLoader
from glloader.lang.c.loader import LOAD_OPENGL_DLL, LOAD_OPENGL_DLL_H, LOAD_OPENGL_GLAPI_H

_WGL_LOADER = \
	LOAD_OPENGL_DLL % {'pre':'static', 'init':'open_gl',
					   'proc':'get_proc', 'terminate':'close_gl'} + '''
int afwglLoadWGL(HDC hdc) {
	int status = 0;

	if(open_gl()) {
		status = afwglLoadWGLLoader((AFWGLloadproc)get_proc, hdc);
		close_gl();
	}

	return status;
}
'''

_WGL_HEADER_START = '''
#ifndef WINAPI
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN 1
#endif
#ifndef NOMINMAX
#define NOMINMAX 1
#endif
#include <windows.h>
#endif

'''

#include <AuroraFW/GEngine/GL/Loader.h>

_WGL_HEADER_MID = '''
#ifndef __afw_gl_wglext_h_

#ifdef __wglext_h_
#error WGL header already included, remove this include, aufw-glloader already provides it
#endif

#define __afw_gl_wglext_h_
#define __wglext_h_

#ifndef APIENTRY
#define APIENTRY
#endif
#ifndef APIENTRYP
#define APIENTRYP APIENTRY *
#endif

#ifdef __cplusplus
extern "C" {
#endif

typedef void* (* AFWGLloadproc)(const char *name);
''' + LOAD_OPENGL_GLAPI_H

_WGL_HEADER_LOADER = '''
GLAPI int afwglLoadWGL(HDC hdc);
''' + LOAD_OPENGL_DLL_H

_WGL_HEADER_END = '''
#ifdef __cplusplus
}
#endif

#endif
'''

_WGL_HAS_EXT = '''
static HDC AFWGLWGLhdc = (HDC)INVALID_HANDLE_VALUE;

static int get_exts(void) {
	return 1;
}

static void free_exts(void) {
	return;
}

static int has_ext(const char *ext) {
	const char *terminator;
	const char *loc;
	const char *extensions;

	if(wglGetExtensionsStringEXT == NULL && wglGetExtensionsStringARB == NULL)
		return 0;

	if(wglGetExtensionsStringARB == NULL || AFWGLWGLhdc == INVALID_HANDLE_VALUE)
		extensions = wglGetExtensionsStringEXT();
	else
		extensions = wglGetExtensionsStringARB(AFWGLWGLhdc);

	if(extensions == NULL || ext == NULL)
		return 0;

	while(1) {
		loc = strstr(extensions, ext);
		if(loc == NULL)
			break;

		terminator = loc + strlen(ext);
		if((loc == extensions || *(loc - 1) == ' ') &&
			(*terminator == ' ' || *terminator == '\\0'))
		{
			return 1;
		}
		extensions = terminator;
	}

	return 0;
}
'''

class WGLCLoader(BaseLoader):
	def write(self, fobj):
		if not self.disabled:
			fobj.write(_WGL_LOADER)

	def write_begin_load(self, fobj):
		fobj.write('\twglGetExtensionsStringARB = (PFNWGLGETEXTENSIONSSTRINGARBPROC)load("wglGetExtensionsStringARB");\n')
		fobj.write('\twglGetExtensionsStringEXT = (PFNWGLGETEXTENSIONSSTRINGEXTPROC)load("wglGetExtensionsStringEXT");\n')
		fobj.write('\tif(wglGetExtensionsStringARB == NULL && wglGetExtensionsStringEXT == NULL) return 0;\n')

	def write_end_load(self, fobj):
		fobj.write('\treturn 1;\n')

	def write_find_core(self, fobj):
		fobj.write('\tAFWGLWGLhdc = hdc;\n')

	def write_has_ext(self, fobj):
		fobj.write(_WGL_HAS_EXT)

	def write_header(self, fobj):
		fobj.write(_WGL_HEADER_START)
		if self.local_files:
			fobj.write('#include "GLLoader.h"\n')
		else:
			fobj.write('#include <AuroraFW/GEngine/GL/Loader.h>\n')
		fobj.write(_WGL_HEADER_MID)
		if not self.disabled:
			fobj.write(_WGL_HEADER_LOADER)

	def write_header_end(self, fobj):
		fobj.write(_WGL_HEADER_END)
