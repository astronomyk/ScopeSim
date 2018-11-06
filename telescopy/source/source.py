"""
This module contains the Class descriptions of the sources

- BasicSource
- PointSource
    - SpectralSource
- ExtendedSource

"""

def source_source():
    """
    Random docstring test
    
    Examples
    --------
    
    Inline code - but should fail ``pytest --doctest-modules``::
    
        >>> print("It's over 9000")
        It's over 9000
        
    
    Blocked code    
    
    .. code::
    
        >>> print("Hello World")
        Hello World
    
    
    More inline code::
    
        >>> print("It's under 10000")
        It's under 10000
        
    
    """
    pass
    

class BasicSource(object):
    """
    A basic `Source` object
    
    Parameters
    ----------
    input : str
        How the things are input
    
    See Also
    --------
    Stuff
    
    """
    
    def __init__(self):
        pass
        
        
    def random_func(self, a):
        """
        This one needs a docstring
        
        Here's the longer description, though not much longer
        
        Parameters
        ----------
        a : int
            A number
            
        Returns
        -------
        a : int
            You get what you give
        
        Examples
        --------
        
        Lets plot a line
        
        .. plot::
        
            >>> import matplotlib.pyplot as plt
            >>> x,y = [0,1], [1,0]
            >>> plt.plot(x,y)           # doctest: +SKIP
            
        
        """
        
        return a


class PointSource(BasicSource):
    """

    """

    def __init__(self):
        pass



class ExtendedSource(BasicSource):
    """

    """

    def __init__(self):
        pass
