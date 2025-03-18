import os
import importlib

__all__ = []

for module in os.listdir(os.path.dirname(__file__)):
    if module.endswith(".py") and module != "__init__.py":
        module_name = module[:-3]
        imported_module = importlib.import_module(f".{module_name}", package=__name__)
        globals()[module_name] = imported_module
        __all__.append(module_name)

