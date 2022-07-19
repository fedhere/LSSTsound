# Siddharth Patel - Week of 06/18/2021 - Report 1



## 1. Work done

### 1.1 Papers Read
---

**PLAsTiCC Paper** [[Arxiv Link](https://arxiv.org/pdf/1810.00001.pdf)] : Learned that times series are the light curves we are going to be working with. 

Light curves are the object's brightness overtime ; flux. Will be measured in 6 filters (passbands): u,g,r,i,z,y; which range from ultra-violet, optical and infrared wavelengths. 

Spectroscopy takes too long, do photometry instead (passbands method); photometry allows observation of further and fainter objects

Deep Drilling Fields (DDFs): small patch in sky, but sampled often → small error in flux (well determined). 

Wide Fast Deep (WFD): large part of sky, 400x area of DDF, observed less → larger uncertainties, but discover more with larger area for observation.

---

**LSST Paper** [[Arxiv Link](https://arxiv.org/pdf/0805.2366.pdf)]: Rubin Observatory Telescope mostly will look at the sky for ~800 times an area of 18000 sq. degrees over 10 years. Will use photometry (ugrizy). Main goals: dark energy/matter, solar system inventory, transients, mapping milky way. Data will be available for everyone. 


---


### 1.2 Code Written 
[[GitHub Link](https://github.com/fedhere/RubinRhapsodies/blob/main/Sid's_copy_of_rubin_rhapsodies.ipynb)]

Sid's copy of rubin_rhapsodies.ipynb (Riley's → My Edits) : Used Riley's visualization notebook to relearn Python, and understand how matplotlib/pandas libraries work. Went through the cells, and tested out different ways to interact with the .csv data based on example code. For example, based on the example code I listed the unique object types in the metadata.





## 2. Figures (at least 1 figure)


| Figure 1 : This is the first object in the PLAsTiCC training data shown in all 6 passbands u,g,r,i,z,y. [[GitHub Link](https://github.com/fedhere/RubinRhapsodies/blob/main/Sid's_copy_of_rubin_rhapsodies.ipynb)] |
| :----------------------------------------------------------: |
| <img src="./figures/r1 f1.png" alt="Figure 1" style="zoom: 50%;" /> |




| Figure 2 : This is the first object in the PLAsTiCC training data, as shown in Figure 1, but only with passband 'z'. This helped show the individual band, which was more insightful to see, than all 6 passbands at once, for me at this point. [[GitHub Link](https://github.com/fedhere/RubinRhapsodies/blob/main/Sid's_copy_of_rubin_rhapsodies.ipynb)] |
| :----------------------------------------------------------: |
| <img src="./figures/r1 f2.png" alt="Figure 2" style="zoom: 50%;" /> |






## 3. Results

To better handle this project, I had to understand how to make use of python libraries, meaning I had to read a documentation and do trial and error to get my coding skills up to proficiency. But before I could do this, I also had to read the background on the PLAsTiCC data set to know what the data I am working with represents. After this I played around with the Riley's example notebook to practice and get familiar with manipulating the data using python; produced different data outputs and figures as shown and explained in the figures section above, and in section 1.2





## 4. Planning

Sonify one light curve from the PLAsTiCC Training Data set and produce a sound clip of the light curve.

Find out different sounds/instruments, that can potentially be mapped onto properties from the data set, to sonify light curves using Astronify/audio-plot-lib or another audio program.
