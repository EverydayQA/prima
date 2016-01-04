from pkgutil import extend_path
__path__ = extend_path(__path__,__name__)
__all__ = ['mqueue_test']
from lib.mqueue import MQueue

