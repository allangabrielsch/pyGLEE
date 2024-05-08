from light_profiles import *

class ESource:
    def __init__(self, 
                 dds_ds, 
                 ngy, 
                 ngx, 
                 dx, 
                 data, 
                 err, 
                 arcmask, 
                 lensmask, 
                 mod_light, 
                 psf, 
                 sub_agn_psf, 
                 sub_agn_psf_factor, 
                 sub_esr_psf, 
                 sub_esr_psf_factor, 
                 regopt, reglampre, 
                 reglamnup, 
                 regtype, 
                 reglam, 
                 reglamlo, 
                 reglamhi, 
                 light_profiles):
        """
        ESource class represents a source in the E-source model.

        Attributes:
            dds_ds (float): Dds/Ds ratio.
            ngy (int): Number of source pixels (number of pixels in 2nd dimension).
            ngx (int): Number of image pixels (number of pixels in 2nd dimension).
            dx (float): Pixel size in image plane (pixel size in 2nd dimension).
            data (str): Path to the data image file (.fits format).
            err (str): Path to the sigma error image file (.fits format).
            arcmask (str): Path to the region used for reconstructing source file (.fits format).
            lensmask (str): Path to the lens mask file (.fits format).
            mod_light (str): Set to 'LensOnly' to not do source plane reconstruction.
            psf (str): Path to the PSF file used for lens light (.fits format).
            sub_agn_psf (str): Path to the subsampled PSF from modeling point image file (.fits format).
            sub_agn_psf_factor (int): Subsampling factor (number of times smaller on a side, needs to be odd).
            sub_esr_psf (str): Path to the subsampled PSF for extended source file (.fits format).
            sub_esr_psf_factor (int): Subsampling factor (number of times smaller on a side, needs to be odd).
            regopt (str): Regularization options (usually use 'SpecRegPrecSigFigOnce').
            reglampre (int): Number of significant digits in lambda (1 usually works, sometimes 2 or 3).
            reglamnup (int): Update lambda every N points.
            regtype (str): Type of regularization ('zeroth', 'grad', 'curv').
            reglam (int): Regularization lambda (regularization strength).
            reglamlo (float): Minimum for optimizing lambda.
            reglamhi (int): Maximum for optimizing lambda.
            light_profiles (list): list containing the light profiles.
        """    
    
        if not isinstance(dds_ds, (int, float)):
            raise TypeError("dds_ds must be int or float")
        if not isinstance(ngy, int):
            raise TypeError("ngy must be int")
        if not isinstance(ngx, int):
            raise TypeError("ngx must be int")
        if not isinstance(dx, (int, float)):
            raise TypeError("dx must be int or float")
        if not isinstance(data, str) or not data.endswith('.fits'):
            raise TypeError("data must be a .fits file path")
        if not isinstance(err, str) or not err.endswith('.fits'):
            raise TypeError("err must be a .fits file path")
        if not isinstance(arcmask, str) or not arcmask.endswith('.fits'):
            raise TypeError("arcmask must be a .fits file path")
        if not isinstance(lensmask, str) or not lensmask.endswith('.fits'):
            raise TypeError("lensmask must be a .fits file path")
        if not isinstance(mod_light, str):
            raise TypeError("mod_light must be string")
        if not isinstance(psf, str) or not psf.endswith('.fits'):
            raise TypeError("psf must be a .fits file path")
        if not isinstance(sub_agn_psf, str) or not sub_agn_psf.endswith('.fits'):
            raise TypeError("sub_agn_psf must be a .fits file path")
        if not isinstance(sub_agn_psf_factor, int) or sub_agn_psf_factor % 2 == 0:
            raise ValueError("sub_agn_psf_factor must be an odd int")
        if not isinstance(sub_esr_psf, str) or not sub_esr_psf.endswith('.fits'):
            raise TypeError("sub_esr_psf must be a .fits file path")
        if not isinstance(sub_esr_psf_factor, int) or sub_esr_psf_factor % 2 == 0:
            raise ValueError("sub_esr_psf_factor must be an odd int")
        if not isinstance(regopt, str):
            raise TypeError("regopt must be string")
        if not isinstance(reglampre, int):
            raise TypeError("reglampre must be int")
        if not isinstance(reglamnup, int):
            raise TypeError("reglamnup must be int")
        if not isinstance(regtype, str) or regtype not in ['zeroth', 'grad', 'curv']:
            raise ValueError("regtype must be a string and one of the following: 'zeroth', 'grad', 'curv'")
        if not isinstance(reglam, int):
            raise TypeError("reglam must be int")
        if not isinstance(reglamlo, (int, float)):
            raise TypeError("reglamlo must be int or float")
        if not isinstance(reglamhi, int):
            raise TypeError("reglamhi must be int")
        if not isinstance(light_profiles, list) or not all(isinstance(lp, LightProfile) for lp in light_profiles):
            raise TypeError("light_profiles must be a list of LightProfile instances")
        
        self.dds_ds = dds_ds
        self.ngy = ngy
        self.ngx = ngx
        self.dx = dx
        self.data = data
        self.err = err
        self.arcmask = arcmask
        self.lensmask = lensmask
        self.mod_light = mod_light
        self.psf = psf
        self.sub_agn_psf = sub_agn_psf
        self.sub_agn_psf_factor = sub_agn_psf_factor
        self.sub_esr_psf = sub_esr_psf
        self.sub_esr_psf_factor = sub_esr_psf_factor
        self.regopt = regopt
        self.reglampre = reglampre
        self.reglamnup = reglamnup
        self.regtype = regtype
        self.reglam = reglam
        self.reglamlo = reglamlo
        self.reglamhi = reglamhi
        self.light_profiles = light_profiles

    def as_string(self):
        values = []
        values.append("esources 1")
        values.append(f"Dds/Ds    {self.dds_ds}  exact:")
        values.append(f"ngy          {self.ngy}")
        values.append(f"ngx          {self.ngx}")
        values.append(f"dx           {self.dx}")
        values.append(f"data         {self.data}")
        values.append(f"err          {self.err}")
        values.append(f"arcmask      {self.arcmask}")
        values.append(f"lensmask     {self.lensmask}")
        values.append(f"mod_light    {self.mod_light}")
        values.append(f"psf          {self.psf}")
        values.append(f"sub_agn_psf  {self.sub_agn_psf}")
        values.append(f"sub_agn_psf_factor     {self.sub_agn_psf_factor}")
        values.append(f"sub_esr_psf  {self.sub_esr_psf}")
        values.append(f"sub_esr_psf_factor     {self.sub_esr_psf_factor}")
        values.append(f"regopt       {self.regopt}")
        values.append(f"reglampre    {self.reglampre}")
        values.append(f"reglamnup    {self.reglamnup}")
        values.append(f"regtype      {self.regtype}")
        values.append(f"reglam       {self.reglam}")
        values.append(f"reglamlo     {self.reglamlo}")
        values.append(f"reglamhi     {self.reglamhi}")
        values.append(f"esource_light  {len(self.light_profiles)}")
        for lp in self.light_profiles:
            values.append(lp.as_string())
        values.append("esource_end")
        return "\n".join(values)