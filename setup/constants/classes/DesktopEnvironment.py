from constants.enums import DE


class DesktopEnvironment:
    name = DE.NONE
    description = ""
    packages = []

    def __init__(self, name, description, packages):
        self.name = name
        self.description = description
        self.packages = packages

    def __eq__(self, other):
        return self.name.value == other.name.value
