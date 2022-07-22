import pytest
import numpy as np
import numpy.testing as npt
import matplotlib.pylab as plt


def test_singleplot():
    from rrhapsodies.rr_utils import readdata
    from rrhapsodies.rr_plotutils import singlePlotObject
    from rrhapsodies.configs import passband
    import subprocess
    data, _ = readdata()
    objectID = 43018203

    for f in passband.keys():
        subprocess.call('rm ID{}_filter_{}.png'.format(objectID, f), shell=True)

        singlePlotObject(data, objectID, filter=f,
                     instrument=None, save=True, show=True)
        status = subprocess.call("test -e 'ID{}_filter_{}.png'".format(objectID, f), shell=True)
        npt.assert_equal(0, status)
        subprocess.call('rm ID{}_filter_{}.png'.format(objectID, f), shell=True)
        npt.assert_equal(0, status)


def test_multiplot():
    from rrhapsodies.rr_utils import readdata
    from rrhapsodies.rr_plotutils import multiPlotObject
    import subprocess
    data, _ = readdata()
    objectID = 43018203

    subprocess.call('rm ID{}_multi.png'.format(objectID), shell=True)

    multiPlotObject(data, objectID,
                     instruments=None, save=True, show=True)

    status = subprocess.call("test -e 'ID{}_multi.png'".format(objectID), shell=True)
    npt.assert_equal(0, status)
    #subprocess.call('rm ID{}_multi.png'.format(objectID), shell=True)
    npt.assert_equal(0, status)
