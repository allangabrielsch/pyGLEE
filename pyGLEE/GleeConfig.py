from header import *
from optimisers import *
from esource import *
from light_profiles import *

class GleeConfig:
    """
    A class to represent the Glee configuration.

    Attributes
    ----------
    header : Header
        The header parameters.
    optimiser : Optimizers
        The optimiser parameters.
    e_source : ESource
        An extended source
    light_profiles : list of LightProfile
        The list of LightProfile parameters.
    """
    def __init__(self, header, optimiser, e_source):
        if not isinstance(header, Header):
            raise TypeError("header must be an instance of Header")
        if not isinstance(optimiser, Optimisers):
            raise TypeError("optimiser must be an instance of Optimizers")
        if not isinstance(e_source, ESource):
            raise TypeError("e_source must be an instance of ESource")
        if not all(isinstance(lp, LightProfile) for lp in e_source.light_profiles):
            raise TypeError("light_profiles must be a list of LightProfile instances")

        self.header = header
        self.optimiser = optimiser
        self.e_source = e_source

    def as_string(self):
        """
        Returns a string representation of the GleeConfig object.

        Returns
        -------
        str
            A string representation of the GleeConfig object.
        """
        values = []
        values.append(self.header.as_string())
        values.append("")  # Add a break
        values.append(self.optimiser.as_string())
        values.append("") 
        values.append(self.e_source.as_string())
        return "\n".join(values)
    