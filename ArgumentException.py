class ArgumentException(Exception):
    """Invalid Argument(s)."""

    def __init__(self, arguments, message="Argument was invalid."):
        self.arguments = arguments
        if len(arguments) > 0:
            plural = len(arguments) > 1
            self.message = f"Argument{'s' if plural else '' } {arguments} {'are' if plural else 'is' } invalid."
        else:
            self.message = message
        super().__init__(self.message)
