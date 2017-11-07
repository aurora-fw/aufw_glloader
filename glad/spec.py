from glad.parse import Spec


class EGLSpec(Spec):
    API = 'https://raw.githubusercontent.com/KhronosGroup/EGL-Registry/master/api/'
    NAME = 'egl'


class GLSpec(Spec):
    API = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/'
    NAME = 'gl'


class GLXSpec(Spec):
    API = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/'
    NAME = 'glx'


class WGLSpec(Spec):
    API = 'https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/'
    NAME = 'wgl'


class VulkanSpec(Spec):
    API = 'https://raw.githubusercontent.com/KhronosGroup/Vulkan-Docs/1.0/src/spec/vk.xml'
    NAME = 'vk'


SPECIFICATIONS = dict()

# reflection to fill SPECIFICATIONS
import sys
import inspect
for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    if issubclass(cls, Spec):
        SPECIFICATIONS[cls.NAME] = cls
