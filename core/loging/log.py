class Log:
    def __init__(self):
        pass

    def info(
            self,
            text: str
    ):
        """Prints the text with info formatting.

        Args:
            text (str): _description_
        """
        print("ⓘ - " + text)