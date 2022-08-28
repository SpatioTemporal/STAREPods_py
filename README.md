# STAREPods_py


Rilee, M., Kuo, K.S., Gallagher, J., Frew, J., Griessbaum, N., Hartnett, E., Wolfe, R., Heber, G. & Khalsa, S.J. (2020). “STARE-PODS: A Versatile data store leveraging the hdf virtual object layer for compatibility.” ESIP Summer Meeting (virtual), 14-24 July 2020.


https://figshare.com/articles/presentation/SpatioTemporal_Adaptive_Resolution_Encoding_STARE-enabled_Event-Based_Analysis_Using_STARE-PODS_Concepts/19597234/1

https://esip.figshare.com/articles/presentation/SpatioTemporal_Adaptive_Resolution_Encoding_STARE-enabled_Event-Based_Analysis_Using_STARE-PODS_Concepts/19597234
10.6084/m9.figshare.19597234.v1

@INPROCEEDINGS{2021AGUFMIN32A..05G,
       author = {{Griessbaum}, Niklas and {Kuo}, Kwo-Sen and {Rilee}, Michael and {Frew}, James and {Gallagher}, James and {Ton That}, Dai Hai},
        title = "{Harmonizing with STARE-PODS to enable best-resolution Analysis-ready data}",
    booktitle = {AGU Fall Meeting Abstracts},
         year = 2021,
       volume = {2021},
        month = dec,
          eid = {IN32A-05},
        pages = {IN32A-05},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021AGUFMIN32A..05G},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}



Many integrative analyses take for granted that data must be interpolated, that is, homogenized, onto a common grid for subsequent analysis. Great value, however, is lost if we take analysis-ready data (ARD) to be only that which has been processed away from its inherent spatiotemporal distribution. For the case of observational data, important physical signatures and traceability are lost as soon as interpolation comes into play. This "premature estimation" hampers our understanding of uncertainties and limits physics-based modelling and parameter retrieval using multiple, diverse sources. Furthermore, by its very nature, interpolation washes out detail and signals at the highest resolutions of a dataset, which are important for real-world applications, such as weather or real-time situation awareness.
To obtain the full value residing in ungridded or diversely gridded data, data must be harmonized, as opposed to homogenized by common gridding. Harmonization data are organized or indexed in a universal manner so that diverse data can be brought together efficiently and at scale. Additionally, end-users and (data) scientists cannot be expected to devote scarce time and resources to wrangling diverse data into an ARD form. Instead, we must capitalize technologies and infrastructure that allow data harmonization to be automated and taken for granted by nearly all data users. The SpatioTemporal Adaptive Resolution Encoding (STARE) is a foundational technology developed by the NASA/ACCESS program to enable integrative Earth Science data analysis scalability in both data size and diversity.
