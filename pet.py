class Pet():
    """Return pet's species, when input pet's name.

    Parameters
    ----------
    name : str
        The name for the Pets

    Attributes
    ----------
    name : str
        This is where we store pet's name
    dog : str
    cat : str
    """

    def __init__(
        self,
        name: str,
    ):
        if isinstance(name, str):
            raise TypeError('Please input string.')

        self.name = name.lower()
        self.dog = 'dog'
        self.cat = 'cat'

    def print_species(
        self,
    ) -> str:
        """Return pet's species.

        Parameters
        ----------
        None

        Returns
        -------
        species : str

        Examples
        --------
        pet.print_species -> 'dog'
        """
        if self.name == 'billy':
            return self.dog
        else:
            return self.cat
