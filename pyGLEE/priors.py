class Prior():
    """ 
    A class to represent a prior for a parameter in GLEE.
    """
    def __init__(self, mean, label="", type="", step=None, link=None, link_a=None, min=None):
        if not isinstance(mean, (int, float)):
            raise TypeError("mean must be a number")
        if not isinstance(label, str):
            raise TypeError("label must be a string")
        if not isinstance(type, str):
            raise TypeError("type must be a string")
        if step is not None and not isinstance(step, (int, float)):
            raise TypeError("step must be a number")
        if link is not None and not isinstance(link, str):
            raise TypeError("link must be a string")
        if link_a is not None:
            if not isinstance(link_a, list) or len(link_a) != 3 or not all(isinstance(i, (int, float)) for i in link_a):
                raise TypeError("link_a must be a list of three numbers")
        if min is not None and not isinstance(min, (int, float)):
            raise TypeError("min must be a number")
        self.mean = mean
        self.label = label
        self.type = type
        self.step= step
        self.link = link
        self.link_a = link_a
        self.min = min



class FlatPrior(Prior):
    def __init__(self, mean, lower, upper, label="", step=None, link=None, link_a=None, min=None):
        """
        Initialize a FlatPrior object.

        Args:
            mean (float): The mean value of the prior.
            lower (float): The lower bound of the prior.
            upper (float): The upper bound of the prior.
            label (str, optional): The label for the prior. Defaults to "".
            type (str, fixed): The type of the prior. Set to "flat".
            step (float, optional): The step size for the prior. Defaults to None.
            link (str, optional): The link for the prior. Defaults to None.
            link_a (arr, optional): The link parameter for the prior. For a linked value x, new value y=a+bx^c .Defaults to None.
            min (float, optional): The minimum value for the prior. Defaults to None.
        """
        super().__init__(mean, label=label, type="flat", step=step, link=link, link_a=link_a, min=min)

        if not isinstance(lower, (int, float)):
            raise TypeError("lower bound must be a number")
        if not isinstance(upper, (int, float)):
            raise TypeError("upper bound must be a number")
        if lower >= upper:
            raise ValueError("lower bound must be less than upper bound")
        

        self.lower = lower
        self.upper = upper

    def prior_as_string(self):
        """
        Convert the prior to a string representation for GLEE.

        Returns:
            str: The string representation of the prior.
        """
        glee_string = f"""{self.type}:{self.lower},{self.upper}  {f"label:{self.label}" if self.label else ""}    {f"min:{self.min}" if self.min is not None else ""}  {f"step:{self.step}" if self.step is not None else ""}   {f"link:{self.link}" if self.link is not None else ""} {f"a:{self.link_a[0]},{self.link_a[1]},{self.link_a[2]}" if self.link_a is not None else ""}"""
        return glee_string




class ExactPrior(Prior):
    """
    Initialize an ExactPrior object.
    Args:
        mean (float): The mean value of the prior.
        label (str, optional): The label for the prior. Defaults to "".
        type (str, fixed): The type of the prior. Set to "exact".
        step (float, optional): The step size for the prior. Defaults to None.
        link (str, optional): The link for the prior. Defaults to None.
        link_a (arr, optional): The link parameter for the prior. For a linked value x, new value y=a+bx^c .Defaults to None.
        min (float, optional): The minimum value for the prior. Defaults to None.
    """    
    def __init__(self, mean, label="", step=None, link=None, link_a=None, min=None):
        super().__init__(mean, label=label, type="exact", step=step, link=link, link_a=link_a, min=min)
    def prior_as_string(self):
        """
        Convert the prior to a string representation for GLEE.

        Returns:
            str: The string representation of the prior.
        """
        glee_string = f"""{self.type}:  {f"label:{self.label}" if self.label else ""}    {f"min:{self.min}" if self.min is not None else ""}  {f"step:{self.step}" if self.step is not None else ""}   {f"link:{self.link}" if self.link is not None else ""} {f"a:{self.link_a[0]},{self.link_a[1]},{self.link_a[2]}" if self.link_a is not None else ""}"""
        return glee_string

    


class NoPrior(Prior):
    """
    Initialize a NoPrior object.
    Args:
        mean (float): The mean value of the prior.
        label (str, optional): The label for the prior. Defaults to "".
        type (str, fixed): The type of the prior. Set to "noprior".
        step (float, optional): The step size for the prior. Defaults to None.
        link (str, optional): The link for the prior. Defaults to None.
        link_a (arr, optional): The link parameter for the prior. For a linked value x, new value y=a+bx^c .Defaults to None.
        min (float, optional): The minimum value for the prior. Defaults to None.
    """    
    def __init__(self, mean, label="", step=None, link=None, link_a=None, min=None):
        super().__init__(mean, label=label, type="noprior", step=step, link=link, link_a=link_a, min=min)
    def prior_as_string(self):
        """
        Convert the prior to a string representation for GLEE.

        Returns:
            str: The string representation of the prior.
        """
        glee_string = f"""{self.type}:  {f"label:{self.label}" if self.label else ""}    {f"min:{self.min}" if self.min is not None else ""}  {f"step:{self.step}" if self.step is not None else ""}   {f"link:{self.link}" if self.link is not None else ""} {f"a:{self.link_a[0]},{self.link_a[1]},{self.link_a[2]}" if self.link_a is not None else ""}"""
        return glee_string
    
class GaussianPrior(Prior): 
    """
    Initialize a NoPrior object.
    Args:
        mean (float): The mean value of the prior.
        sigma (float): The sigma value for the prior. 
        type (str, fixed): The type of the prior. Set to "gaussian".
        step (float, optional): The step size for the prior. Defaults to None.
        link (str, optional): The link for the prior. Defaults to None.
        link_a (arr, optional): The link parameter for the prior. For a linked value x, new value y=a+bx^c .Defaults to None.
        min (float, optional): The minimum value for the prior. Defaults to None.
    """    
    def __init__(self, mean, sigma, label="", step=None, link=None, link_a=None, min=None):
        super().__init__(mean, label=label, type="gaussian", step=step, link=link, link_a=link_a, min=min)
        if not isinstance(sigma, (int, float)):
            raise TypeError("sigma must be a number")
        self.sigma = sigma
    def prior_as_string(self):
        """
        Convert the prior to a string representation for GLEE.

        Returns:
            str: The string representation of the prior.
        """
        glee_string = f"""{self.type}:{self.mean},{self.sigma}  {f"label:{self.label}" if self.label else ""}    {f"min:{self.min}" if self.min is not None else ""}  {f"step:{self.step}" if self.step is not None else ""}   {f"link:{self.link}" if self.link is not None else ""} {f"a:{self.link_a[0]},{self.link_a[1]},{self.link_a[2]}" if self.link_a is not None else ""}"""        
        return glee_string
