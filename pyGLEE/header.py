class Header:
    """
    A class to represent the chi2 parameters.

    Attributes
    ----------
    chi2type : int
        The type of chi2. Can be one of the following:
        1: point source position
        2: point image position
        4: fluxes
        8: 
        16: extended images (chi2 of pixelated image)
        32: 
        64: 
        128: time delays
        To combine multiple chi2, add the types together. E.g., to combine image position (chi2type=2) with time delays (chi2type=128), use chi2type of 130 (=2+128). Note that chi2type=3 should not be used, since either the image position chi2 or source position chi2 is used, but not both.
    minimiser : str
        The minimiser to use. Can be 'siman' but no idea what else.
    seed : int
        The magical seed.
    """
    def __init__(self, chi2type, minimiser, seed):
        if not isinstance(chi2type, int):
            raise TypeError("chi2type must be an integer")        
        if chi2type not in [1, 2, 4, 8, 16, 32, 64, 128]:
            raise ValueError("chi2type must be one of [1, 2, 4, 8, 16, 32, 64, 128]")
        if minimiser not in ['siman', 'mcmc']:
            raise ValueError("minimiser must be 'siman' or 'mcmc'")
        if not isinstance(seed, int):
            raise TypeError("seed must be an integer")

        self.chi2type = chi2type
        self.minimiser = minimiser
        self.seed = seed

    def as_string(self):
        """
        Returns a string representation of the Header object.

        Returns
        -------
        str
            A string representation of the Header object.
        """
        values = []
        values.append(f"chi2type {self.chi2type}")
        values.append(f"minimiser {self.minimiser}")
        values.append(f"seed {self.seed}")
        return "\n".join(values)