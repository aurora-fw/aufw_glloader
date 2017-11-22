import glloader.lang.c
import glloader.lang.d
import glloader.lang.nim
import glloader.lang.volt


def get_generator(name, spec):
	_langs = [
		glloader.lang.c,
		glloader.lang.d,
		glloader.lang.nim,
		glloader.lang.volt
	]

	for lang in _langs:
		gen, loader = lang.get_generator(name, spec)
		if gen is not None:
			return gen, loader
	return None, None
