from argparser import ArgParser

class Core:
    def start(self):
        """
        Starts and configures arguement parser.
        """
        self._create_arg()

    def _create_arg(self):
        self.arg_parser = ArgParser()
        self.arg_parser.add_argument("filename")
    