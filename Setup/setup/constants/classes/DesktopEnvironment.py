from .Package import Package
from setup.constants.enums import DE


class DesktopEnvironment:
    name: DE
    description: str
    packages: list[Package]

    def __init__(self, name: DE, description: str, packages: list[Package]):
        self.name = name
        self.description = description
        self.packages = packages
