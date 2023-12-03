import importlib
import os
import pkgutil
import sys

from types import ModuleType

ancestry_pack = None
supported_ancestries = None


def _import_submodules(module):
    pkgs = pkgutil.iter_modules(module.__path__)
    for loader, module_name, is_pkg in pkgs:
        yield importlib.import_module(f"{module.__name__}.{module_name}")


def load_ancestry_pack(module_name: str = "") -> ModuleType:
    if not module_name:
        module_name = os.getenv("NPC_ANCESTRY_PACK", "npc.ancestries")
    ancestry_pack = importlib.import_module(module_name)
    _import_submodules(ancestry_pack)
    supported_ancestries = dict(
        (module.__name__.split(".")[-1], module) for module in list(_import_submodules(sys.modules[module_name]))
    )
    return ancestry_pack, supported_ancestries
