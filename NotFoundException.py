class NotFoundException(Exception):
    """Resource was not found."""

    def __init__(self, id, message="Resource was not found."):
        self.id = id
        self.message = f"Resource was not found with the id: {id}." if id is not None else message
        super().__init__(self.message)
