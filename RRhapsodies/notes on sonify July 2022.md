# SONIFY:

Sonify works by converting strings of numbers to notes within a key and a range of octages. 

To play a scale, say c_major, we pass to sonify.convert_to_key

```
x = np.linspace(1,4,7, endpoint=True)
```

# generate seven notes, the lowest has value 1 the highest has value 2
```
y = np.linspace(1,2,7, endpoint=True)

data = list(zip(x, y))
```

# seven notes within one octave in c_major: do-re-mi-fa-sol-la-ti
converted_c_data = sonify.convert_to_key(data, 'c_major', number_of_octaves=1)

```
x, y_in_c = zip(*converted_c_data)
```

# now play them back
```
sonify.play_midi_from_data(list(zip(x, y_in_c)), track_type='single’)
```

NOTE: ```sonify.play_midi_from_data()``` also accepts keyword arguments key and number_of_octaves. If given, the data gets rescaled _again_ and reset to cover the key and number of octaves designated by the keywords!

```
key='c_major', number_of_octaves=1
```

Additional notes:

- While the range in x determines the time it take to play the piece, it does not matter how I set the limit of y: 
``` 
y = np.linspace(1,2,7, endpoint=True), y = np.linspace(0,2,7, endpoint=True),

y = np.linspace(123,200,7, endpoint=True)
```

Those are all equivalent because the data gets renormalized based on the scale that defines the allowable notes and the number of octaves that defines the range

- Only 7 notes are allowed within the scale, so if I try to play more notes _within_ the range, intermediate values, I get repeats of the same notes
```
y = np.linspace(1,2,14, endpoint=True) -> 
do-do-re-re-mi-mi-fa-fa-sol-sol-la-la-ti-ti
```
(i.e. we cannot modify keys to make them sharp or flat arbitrarily)

Next, what if I want to add the higher c to complete the scale: then I need to add a note to the previous set, and since the higher Do is the next semitone after the last key in the previous scale, Ti, then its number value is just the values of Ti + 1

```
sonify.play_midi_from_data(list(zip(np.linspace(1, 4, 8, endpoint=True),
                          np.concatenate([y_in_c, [y_in_c[-1] + 1]]))),
                          track_type='single')
```

So now, lets look at how we generate scores for our data.
If we take the approach we took above we prepare the data first then we pass it to sonify.play_midi_from_data
as:

```
normalized_x = sonify.core.scale_list_to_range(x_points, new_min=t_min, new_max=t_max)

quantized_x = normalized_x #this sets the x values to integers, which aids musicality

normalized_y = sonify.core.scale_list_to_range(y_points,
                                                  new_min=low_note,
                                                  new_max=high_note)
                                                  
sonify.play_midi_from_data([instrument] + normed_data, track_type='single')
```

Where ``instrument’’ is a string corresponding to an available instrument (e.g. ‘violin’)

However, this does not allows us to choose a key. 

```
normed_data = sonify.core.convert_to_key([instrument] + list(zip(quantized_x, y_points)),octave_start=1)
```

## consistent normalization for multitrack
But this is still not right cause we cannot control the relative range of the scores associated with each band: the range should be set by the band that has the largest flux difference, and the other bands should be played in a proportional range.

In order to ensure that all tracks (i.e. all filters) are normalized together, I introduced the “rescaling” function: this function calculates the set of notes available for a given key and number of octaves corresponding to the max flux range (max_flux - min_flux for the whole time series considering all six filters). This is achieved by creating the array corresponding to all available notes: e.g. Do Major, 1 octave, would be 

(36, 38, 40, 41, 43, 45, 47)

If we have 2 arrays, with minimum value 0 and max value 6, the max range is 6. Lets for simplicity assume that the highest and lowest value are in the sam array and that the second array misses the first and last element:

[0,1,2,3,4,5,6], [1,2,3,4,5]

Then the notes available for the second array are (see ```test_rescale_flux( )``` in test_utils.py)

(38, 40, 41, 43, 45)

To do this, I modified the sonify core function 

```
def convert_to_key(data, key, number_of_octaves=4,minmaxvalue=None)
```

To take the argument minmaxvalues which is a tuple of two indices that slice the notes_in_key array. This function is called by ```prep_sonification()``` function in rrhapsodies/rr_utils.py

```
normed_data = sonify.core.convert_to_key(data, key, number_of_octaves=noctaves, minmaxvalue=rescaling)
```

And rescaling is calculated by 
```
rescaling = rescalenotes(y, minmaxflux, keynotes)
```

Which takes the flux values to be sonified, and the max range of flux allowed (which should strictly be larger than the range in the present data).

## drone 

Additional note: I also implemented a couple of drones. Note that the notes can be played as rapidly as one desires. The 
```
quantize_x_value(list_to_quantize, steps=0.5)
```

sets the values to be spaced by defined intervals, which aids listenability, but it can be skipped to play the notes at exactly the times of the observations, or called with a smaller value of step to enable finer quantization. However, the y notes are fixed to the scale, and at best we could create a chromatic scale, no finer than ½ note interval. Additionally, as the notes are played rapidly significant distortion is generated.
I implemented a step function drone that plays one note per month going through a F-A cycle each year (six months per note) with a C base and a glissando drone in F major Lydian with a 12 notes glissando per year. Those are added as tracks and set to use “voice oohs” with low volume (volume set to 40). They are added to a multisonification in the multisonification function 

```
multiSonification(data, objectID, instruments=None, key=None,
                     transposing=False, rescaled=False, noctaves=configs.NOCT,
                     drone=True, save=False, plot=True):
```

By unsetting drone=None. Currently to switch from one to the other you can set the keyword tp "gliss" or "step"

## volume
I also implemented volume, proportional to the uncertainty in the data (and softer for the drone)



