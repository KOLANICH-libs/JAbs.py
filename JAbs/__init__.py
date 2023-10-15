__all__ = ("SelectedJVMInitializer", "ClassPathT", "ClassesImportSpecT")
import sys
from importlib import import_module
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KAbs/JAbs.py , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

from .utils.pathListTools import ClassesImportSpecT, ClassPathT

implPkgNameMapping = {"cpython": "JPype", "graalpython": "GraalVM"}

implPkgName = implPkgNameMapping[sys.implementation.name]
pkg = import_module(".impls." + implPkgName, __package__)
SelectedJVMInitializer = pkg.SelectedJVMInitializer
