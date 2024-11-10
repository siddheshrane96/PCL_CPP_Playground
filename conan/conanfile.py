from conan import ConanFile
from conan.tools.cmake import cmake_layout

class PCLPlayground(ConanFile):
    name = "PCLPlayground"
    version = "1.0.0"
    """
    values of the settings are specific to the profile. And you can check that with
    $cat ~/.conan/profiles/default
    """
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    # def build_requirements(self):
    #     if self.settings.arch == "x86_64":
    #         self.build_requires("example/example@a12345")
    
    def requirements(self):
        self.requires("pcl/1.13.1")
        self.requires("cmake/3.30.5")
        self.requires("eigen/3.4.0")

    def layout(self):
        cmake_layout(self)