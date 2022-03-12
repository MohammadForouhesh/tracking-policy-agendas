import sys
import distutils.util
from pathlib import Path
from setuptools import setup, find_packages

PACKAGES = find_packages()
COMPILE_OPTIONS = {
    "msvc": ["/Ox", "/EHsc"],
    "other": ["-O3", "-Wno-strict-prototypes", "-Wno-unused-function"],
}
COMPILER_DIRECTIVES = {
    "language_level": -3,
    "embedsignature": True,
    "annotation_typing": False,
}
LINK_OPTIONS = {"msvc": [], "other": []}


def is_new_osx():
    """Check whether we're on OSX >= 10.10"""
    name = distutils.util.get_platform()
    if sys.platform != "darwin": return False
    elif name.startswith("macosx-10"):
        minor_version = int(name.split("-")[1].split(".")[1])
        if minor_version >= 7:  return True
        else:                   return False
    else:                       return False


if is_new_osx():
    COMPILE_OPTIONS["other"].append("-stdlib=libc++")
    LINK_OPTIONS["other"].append("-lc++")
    LINK_OPTIONS["other"].append("-nodefaultlibs")


def clean(path):
    for path in path.glob("**/*"):
        if path.is_file() and path.suffix in (".so", ".cpp"):
            print(f"Deleting {path.name}")
            path.unlink()


def setup_package():
    root = Path(__file__).parent

    setup(
        name='tracking_policy_agendas',
        packages=PACKAGES,
        version='1.0.0',
        url='https://github.com/MohammadForouhesh/tracking-policy-agendas',
        license='MIT',
        author='MohammadForouhesh',
        author_email='Mohammadh.Forouhesh@gmail.com',
        description='A Persian Twitter policy agenda tracking framework',
        package_data={"": ["*.pyx", "*.pxd", "*.pxi", "*.cu"]},
    )


if __name__ == '__main__':
    setup_package()
