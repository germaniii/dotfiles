from textual.message import Message


class PackageInstalled(Message):
    def __init__(self, package, is_success):
        self.package = package
        self.is_success = is_success
        super().__init__()
