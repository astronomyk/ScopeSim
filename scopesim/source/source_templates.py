from os import path as pth

import numpy as np
from astropy import units as u
from astropy.table import Table

from synphot import SourceSpectrum, ConstFlux1D
from synphot.units import PHOTLAM

from scopesim.rc import __pkg_dir__
from .source import Source
from .. import rc


def empty_sky(flux=0):
    """
    Returns an empty source so that instrumental fluxes can be simulated

    Returns
    -------
    sky : Source

    """
    sky = Source(lam=[0.3, 3.0]*u.um, spectra=[flux, flux]*PHOTLAM,
                 x=[0], y=[0], ref=[0], weight=[1])
    return sky


def star_field(n, mmin, mmax, width, height=None, photometric_system="vega",
               use_grid=False):
    """
    Creates a super basic field of stars with random positions and brightnesses

    Parameters
    ----------
    n : int
        number of stars

    mmin, mmax : float
        [mag] minimum and maximum magnitudes of the population

    width : float
        [arcsec] width of region to put stars in

    height : float, optional
        [arcsec] if None, then height=width

    photometric_system : str, optional
        [vega, AB]

    use_grid : bool, optional
        Place stars randomly or on a grid

    Returns
    -------
    stars : scopesim.Source object
        A Source object with a field of stars that can be fed into the method:
        OpticalTrain.observe()

    See Also
    --------
    OpticalTrain.observe
    OpticalTrain.readout

    """
    if height is None:
        height = width

    if photometric_system.lower() == "ab":
        spec = ab_spectrum()
    else:
        spec = vega_spectrum()

    if rc.__config__["!SIM.random.seed"] is not None:
        np.random.seed(rc.__config__["!SIM.random.seed"])

    if use_grid:
        nw = np.ceil(n**0.5)
        nh = np.ceil(n / nw)
        x, y = np.mgrid[0:1:1/nw, 0:1:1/nh] - 0.5
        positions = x.flatten(), y.flatten()
    else:
        positions = np.random.random(size=(2, n)) - 0.5

    x = width * positions[0]
    y = height * positions[1]
    mags = np.linspace(mmin, mmax, n)
    w = 10**(-0.4 * mags)
    ref = np.zeros(n, dtype=int)

    tbl = Table(data=[x, y, w, ref, mags],
                names=["x", "y", "weight", "ref", "mag"])
    tbl.meta["photometric_system"] = photometric_system
    stars = Source(spectra=spec, table=tbl)

    return stars


def vega_spectrum(mag=0):
    vega = SourceSpectrum.from_file(pth.join(__pkg_dir__, "vega.fits"))
    vega = vega * 10 ** (-0.4 * mag)
    return vega


def st_spectrum(mag=0):
    return SourceSpectrum(ConstFlux1D, amplitude=mag*u.STmag)


def ab_spectrum(mag=0):
    return SourceSpectrum(ConstFlux1D, amplitude=mag*u.ABmag)
