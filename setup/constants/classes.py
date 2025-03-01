class DesktopEnvironment:
    name = ""
    description = ""
    packages = []

    def __init__(self, name, description, packages):
        self.name = name
        self.description = description
        self.packages = packages


class Package:
    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description
