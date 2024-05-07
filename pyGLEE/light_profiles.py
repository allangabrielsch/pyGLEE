from priors import *

class LightProfile:
    def __init__(self, x, y, amp):
        if not isinstance(x, Prior):
            raise TypeError("x must have a prior")
        if not isinstance(y, Prior):
            raise TypeError("y must have a prior")
        if not isinstance(amp, Prior):
            raise TypeError("amp must have a prior")
        if amp.mean < 0:
            raise ValueError("amp must be positive")
        self.x = x
        self.y = y
        self.amp = amp

class Sersic(LightProfile): 
    def __init__(self, x, y, amp, q, pa, r_eff, n_sersic):
        """
        Initialize a Sersic light profile.
        Parameters:
        x: The x-coordinate of the object.
        y: The y-coordinate of the object.
        amp: The amplitude of the object.
        q: The axis ratio of the object.
        pa: The position angle of the object.
        r_eff: The effective radius of the object.
        n_sersic: The Sersic index of the object.
        """
        super().__init__(x, y, amp)
        if not isinstance(q, Prior):
            raise TypeError("q must have a prior")
        if not isinstance(pa, Prior):
            raise TypeError("pa must have a prior")
        if not isinstance(r_eff, Prior):
            raise TypeError("r_eff must have a prior")
        if not isinstance(n_sersic, Prior):
            raise TypeError("n_sersic must have a prior")
        self.q = q
        self.pa = pa
        self.r_eff = r_eff
        self.n_sersic = n_sersic

    def as_string(self):
        """
        Returns a GLEE string of the light profile.

        The string includes the mean values and prior information for each attribute of the object.

        Returns:
            str: A string representation of the object.
        """   
        glee_string = f"""
        sersic
        {self.x.mean}  #x-coord   {self.x.prior_as_string()}
        {self.y.mean}  #y-coord   {self.y.prior_as_string()}
        {self.q.mean}  #q         {self.q.prior_as_string()}
        {self.pa.mean}  #PA        {self.pa.prior_as_string()}
        {self.amp.mean}  #amp       {self.amp.prior_as_string()}
        {self.r_eff.mean}  #r_eff     {self.r_eff.prior_as_string()}
        {self.n_sersic.mean}  #n_sersic  {self.n_sersic.prior_as_string()}
        """
        return glee_string
    
class PSF(LightProfile):
    """
    Initialize a PSF light profile.
    Parameters:
    x: The x-coordinate of the object.
    y: The y-coordinate of the object.
    amp: The amplitude of the object.
    """    
    def __init__(self, x, y, amp):
        super().__init__(x, y, amp)

class Gaussian(LightProfile):
    """
    Initialize a Gaussian light profile.
    Parameters:
    x: The x-coordinate of the object.
    y: The y-coordinate of the object.
    amp: The amplitude of the object.
    q: The axis ratio of the object.
    pa: The position angle of the object.
    sigma: The sigma of the object.
    """    
    def __init__(self, x, y, amp, q, pa, sigma):
        super().__init__(x, y, amp)
        if not isinstance(q, Prior):
            raise TypeError("q must have a prior")
        if not isinstance(pa, Prior):
            raise TypeError("pa must have a prior")
        if not isinstance(sigma, Prior):
            raise TypeError("sigma must have a prior")
        self.q=q
        self.pa=pa
        self.sigma = sigma
    def as_string(self):
        """
        Returns a GLEE string of the light profile.

        The string includes the mean values and prior information for each attribute of the object.

        Returns:
            str: A string representation of the object.
        """       
        glee_string = f"""
        gaussian
        {self.x.mean}  #x-coord   {self.x.prior_as_string()}
        {self.y.mean}  #y-coord    {self.y.prior_as_string()}
        {self.q.mean}  #q          {self.q.prior_as_string()}
        {self.pa.mean}  #PA        {self.pa.prior_as_string()}
        {self.amp.mean}  #amp       {self.amp.prior_as_string()}
        {self.sigma.mean}  #sigma      {self.sigma.prior_as_string()}
        """
        return glee_string
    
class Moffat(LightProfile):
    """
    Initialize a Moffat light profile.
    Parameters:
    x: The x-coordinate of the object.
    y: The y-coordinate of the object.
    amp: The amplitude of the object.
    q: The axis ratio of the object.
    pa: The position angle of the object.
    alpha: The alpha structural parameter.
    beta: The alpha structural parameter.
    """    
    def __init__(self, x, y, amp, q, pa, alpha, beta):
        super().__init__(x, y, amp)
        self.q=q
        self.pa=pa
        self.alpha = alpha
        self.beta = beta
    def as_string(self):
        """
        Returns a GLEE string of the light profile.

        The string includes the mean values and prior information for each attribute of the object.

        Returns:
            str: A string representation of the object.
        """        
        glee_string = f"""
        moffat
        {self.x.mean}  #x-coord   {self.x.prior_as_string()}
        {self.y.mean}  #y-coord    {self.y.prior_as_string()}
        {self.q.mean}  #q          {self.q.prior_as_string()}
        {self.pa.mean}  #PA        {self.pa.prior_as_string()}
        {self.amp.mean}  #amp       {self.amp.prior_as_string()}
        {self.alpha.mean}  #alpha      {self.alpha.prior_as_string()}
        {self.beta.mean}  #beta      {self.beta.prior_as_string()}
        """
        return glee_string

class piemd(LightProfile): 
    """
    Initialize a piemd light profile.
    Parameters:
    x: The x-coordinate of the object.
    y: The y-coordinate of the object.
    amp: The amplitude of the object.
    q: The axis ratio of the object.
    pa: The position angle of the object.
    w: Magical parameter (ask Sherry for more information)
    """       
    def __init__(self, x, y, amp, q, pa, w):
        super().__init__(x, y, amp)
        self.q=q
        self.pa=pa
        self.w = w
    def as_string(self):
        """
        Returns a GLEE string of the light profile.

        The string includes the mean values and prior information for each attribute of the object.

        Returns:
            str: A string representation of the object.
        """    
        glee_string = f"""
        piemd
        {self.x.mean}  #x-coord   {self.x.prior_as_string()}
        {self.y.mean}  #y-coord    {self.y.prior_as_string()}
        {self.q.mean}  #q          {self.q.prior_as_string()}
        {self.pa.mean}  #PA        {self.pa.prior_as_string()}
        {self.amp.mean}  #amp       {self.amp.prior_as_string()}
        {self.w.mean}  #w      {self.w.prior_as_string()}
        """
        return glee_string
