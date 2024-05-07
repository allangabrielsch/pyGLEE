        
class SimanParameters:
    """
    A class to represent the parameters for Simulated Annealing.

    Attributes
    ----------
    siman_iter : int
        The number of iterations of annealing. If iter>1, will repeat at Ti.
    siman_nT : int
        The number of steps searched for at a given temperature. Generally ~1e3 for extended source, ~1e4-1e5 for point source.
    siman_dS : float
        The initial global scaling of step size.
    siman_Sf : float
        The change in global scaling as temperature decreases. dS(j)=(dS)/(Sf)^j for the (j+1)^th temperature.
    siman_k : int
        The analogous of Boltzmann constant factor in e[-E/kT].
    siman_Ti : float
        The initial temperature.
    siman_Tf : float
        The temperature factor. T(j)= Ti/Tf^j for the (j+1)^th temperature.
    siman_Tmin : int
        The final temperature.
    """
    def __init__(self, 
                 siman_iter, 
                 siman_nT, 
                 siman_dS, 
                 siman_Sf, 
                 siman_k, 
                 siman_Ti, 
                 siman_Tf, 
                 siman_Tmin):
        if not isinstance(siman_iter, int):
            raise TypeError("siman_iter must be int")
        if not isinstance(siman_nT, int):
            raise TypeError("siman_nT must be int")
        if not isinstance(siman_dS, (int, float)):
            raise TypeError("siman_dS must be int or float")
        if not isinstance(siman_Sf, (int, float)):
            raise TypeError("siman_Sf must be int or float")
        if not isinstance(siman_k, int):
            raise TypeError("siman_k must be int")
        if not isinstance(siman_Ti, (int, float)):
            raise TypeError("siman_Ti must be int or float")
        if not isinstance(siman_Tf, (int, float)):
            raise TypeError("siman_Tf must be int or float")
        if not isinstance(siman_Tmin, int):
            raise TypeError("siman_Tmin must be int")

        self.siman_iter = siman_iter
        self.siman_nT = siman_nT
        self.siman_dS = siman_dS
        self.siman_Sf = siman_Sf
        self.siman_k = siman_k
        self.siman_Ti = siman_Ti
        self.siman_Tf = siman_Tf
        self.siman_Tmin = siman_Tmin
        
    def as_string(self):
        values = []
        values.append(f"siman_iter  {self.siman_iter}")
        values.append(f"siman_nT {self.siman_nT}")
        values.append(f"siman_dS {self.siman_dS}")
        values.append(f"siman_Sf {self.siman_Sf}")
        values.append(f"siman_k {self.siman_k}")
        values.append(f"siman_Ti {self.siman_Ti}")
        values.append(f"siman_Tf {self.siman_Tf}")
        values.append(f"siman_Tmin {self.siman_Tmin}")
        return "\n".join(values)

class McmcParameters:
    """
    A class to represent the parameters for Markov Chain Monte Carlo.

    Attributes
    ----------
    mcmc_n : int
        The number of steps per chain for Markov Chain Monte Carlo.
    mcmc_dS : float
        The global scaling of step size. Desired acceptance rate of ~25% (Dunkley+05).
    mcmc_dSini : int
        0 for the initial parameters, 1 for random step size.
    mcmc_k : int
        The analogous of Boltzmann constant factor in e[-E/kT].
    """
    
    def __init__(self, 
                 mcmc_n, 
                 mcmc_dS, 
                 mcmc_dSini, 
                 mcmc_k):
        
        if not isinstance(mcmc_n, int):
            raise TypeError("mcmc_n must be int")
        if not isinstance(mcmc_dS, (int, float)):
            raise TypeError("mcmc_dS must be int or float")
        if not isinstance(mcmc_dSini, int):
            raise TypeError("mcmc_dSini must be int")
        if not isinstance(mcmc_k, int):
            raise TypeError("mcmc_k must be int")

        self.mcmc_n = mcmc_n
        self.mcmc_dS = mcmc_dS
        self.mcmc_dSini = mcmc_dSini
        self.mcmc_k = mcmc_k

    def as_string(self):
        values = []
        values.append(f"mcmc_n {self.mcmc_n}")
        values.append(f"mcmc_dS {self.mcmc_dS}")
        values.append(f"mcmc_dSini {self.mcmc_dSini}")
        values.append(f"mcmc_k {self.mcmc_k}")
        return "\n".join(values)

class CovarianceMatrix:
    """
    A class to represent a covariance matrix.

    Attributessiman = SimanParameters(siman_iter=10, 
                        siman_nT=1000, 
                        siman_dS=0.1, 
                        siman_Sf=0.5, 
                        siman_k=1, 
                        siman_Ti=1.0, 
                        siman_Tf=0.5, 
                        siman_Tmin=1)
mcmc = McmcParameters(mcmc_n=1000, 
                      mcmc_dS=0.25, 
                      mcmc_dSini=1, 
                      mcmc_k=1)

cov = CovarianceMatrix(sampling_f='gaussian', 
                       sampling_cov='path/to/covariance/matrix.cov')

# these three have to be in an optimizers class

    ----------
    sampling_f : str
        The sampling function. Can be 'gaussian' or 'flat'.
    sampling_cov : str
        The path to the covariance matrix file. Has to be a .cov file.
    """
    def __init__(self, 
                 sampling_f, 
                 sampling_cov):
        
        if sampling_f not in ["gaussian", "flat"]:
            raise ValueError("sampling_f must be 'gaussian' or 'flat'")
        if not isinstance(sampling_cov, str):
            raise TypeError("sampling_cov must be a string")
        if not sampling_cov.endswith('.cov'):
            raise ValueError("sampling_cov must be a path to a .cov file")    
        self.sampling_f = sampling_f
        self.sampling_cov = sampling_cov

    def as_string(self):
        values = []
        values.append(f"sampling_f {self.sampling_f}")
        values.append(f"sampling_cov {self.sampling_cov}")
        return "\n".join(values)
    



class Optimizers:
    """
    A class to represent the optimizers which includes Simulated Annealing and Markov Chain Monte Carlo parameters.

    Attributes
    ----------
    siman_params : SimanParameters
        The parameters for Simulated Annealing.
    mcmc_params : McmcParameters
        The parameters for Markov Chain Monte Carlo.
    cov_matrix : CovarianceMatrix, optional
        The covariance matrix, if provided.
    """
    def __init__(self, siman_params, mcmc_params, cov_matrix=None):
        if not isinstance(siman_params, SimanParameters):
            raise TypeError("siman_params must be an instance of SimanParameters")
        if not isinstance(mcmc_params, McmcParameters):
            raise TypeError("mcmc_params must be an instance of McmcParameters")
        if cov_matrix is not None and not isinstance(cov_matrix, CovarianceMatrix):
            raise TypeError("cov_matrix must be an instance of CovarianceMatrix or None")

        self.siman = siman_params
        self.mcmc = mcmc_params
        self.cov = cov_matrix
    
    def as_string(self):
        values = []
        values.append(self.siman.as_string())
        values.append("")  # Add a break
        values.append(self.mcmc.as_string())
        if self.cov is not None:
            values.append("")  # Add a break
            values.append(self.cov.as_string())
        return "\n".join(values)    
