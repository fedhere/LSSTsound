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
    subprocess.call('rm ID{}_multi.png'.format(objectID), shell=True)
    npt.assert_equal(0, status)


def test_mklcvsgif():
    from rrhapsodies.rr_utils import readdata
    from rrhapsodies.rr_plotutils import singlePlotObject, multiPlotObject, makegiflcvs
    #import imageio.v2 as iio
    import subprocess
    from rrhapsodies.configs import passband, INSTRUMENTS
    images = []
    data, _ = readdata()
    objectID = 43018203
    gifname = 'test.gif'
    subprocess.call(gifname, shell=True)
    filenames = []
    for f in passband.keys():
        singlePlotObject(data, objectID, filter=f,
                         instrument=None, save=True, show=False)
        filenames.append('ID{}_filter_{}.png'.format(objectID, f))

    multiPlotObject(data, objectID,
                     instruments=INSTRUMENTS, save=True, show=False)
    filenames.append('ID{}_multi.png'.format(objectID))

    makegiflcvs(filenames, gifname)

    for f in passband.keys():
        status = subprocess.call('rm ID{}_filter_{}.png'.format(objectID, f), shell=True)
        npt.assert_equal(0, status)
    status = subprocess.call('rm ID{}_multi.png'.format(objectID), shell=True)
    npt.assert_equal(0, status)

    subprocess.call(giffile, shell=True)
    npt.assert_equal(0, status)
