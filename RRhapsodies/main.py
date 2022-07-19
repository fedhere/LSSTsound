# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from rrhapsodies import rr_utils
from rrhapsodies import configs
<<<<<<< HEAD

if __name__ == '__main__':
    data, metadata = rr_utils.readdata()
    thisband = 'r'
    object = 43018203 # 615 #2677
=======
if __name__ == '__main__':
    data, metadata = rr_utils.readdata()
    thisband = 'r'
    object = 2677
>>>>>>> 6771a4e280041380882fab8a8b9e1699d633c906
    if False:
        for thisband in ['u', 'g', 'r', 'i', 'z', 'y']:
            print("object:", object, "band", thisband, configs.INSTRUMENTS[thisband],
                  "transpose:", configs.TRANSPOSITIONS[thisband], "thirds up")
            rr_utils.singleSonification(data, object, filter=thisband,
                                instrument=configs.INSTRUMENTS[thisband],
                                transposing=True, rescaled=True,
                                key=configs.KEY, save=True, plot=True)

    rr_utils.multiSonification(data, object, key=configs.KEY,
<<<<<<< HEAD
                               drone="gliss", drum='crash cymbal 1',
                               save=True, plot=True)
=======
                               drone="gliss", save=True, plot=True)

>>>>>>> 6771a4e280041380882fab8a8b9e1699d633c906
