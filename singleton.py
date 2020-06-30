#单例模式
class Single:

	__instance = None

	def __new__(cls, *args, **kwargs):

		if cls.__instance is None:
			cls.__instance = object.__new__(cls, *args, *kwargs)
		return cls.__instance
	def __init__(self):
		pass

#函数装饰器实现单例
def single(cls):

	__instance = {}

	def inner():
		if cls not in __instance:
			__instance[cls] = cls()
		return __instance[cls]
	return inner
@single
class A:

	def __init__(self):
		pass
	
#类装饰器实现单例
class Singleton:

	def __init__(self, cls):

		self._cls = cls
		self._instance = {}

	def __call__(self):

		if self._cls not in self._instance:

			self._instance[self._cls] = self._cls()
		return self._instance[self._cls]

@Singleton
class B(object):
	"""docstring for B"""
	def __init__(self):
		pass