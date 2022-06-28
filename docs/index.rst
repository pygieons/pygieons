Python OS Ecosystem for GIS and Earth Observation
=================================================

This website aims to list all open-source (OS) Python libraries that can be used for doing
various operations, analyses, visualizations etc. related to GIS and Earth Observation.
The libraries are categorized into ``core / data structures``, ``analysis & modelling``, ``visualization``,
and ``data extraction / processing``. There are separate pages listing packages
that are commonly used to work with vector or raster data, or which are generic packages
(not specific to data type or GIS in general). You can browse through the website by clicking on the links
on the left.

.. figure:: pythongis-ecosystem.png
   :width: 70%
   :target: _static/pythongis-ecosystem-large.html

   Python GIS/EO ecosystem linkages (click to enlarge).


**Why?** We believe it is useful to have a dedicated website providing a good overview of Python
Ecosystem for GIS and Earth Observation with relevant information. The actual initiator for creating this website was, in fact, to support `pythongis.org <https://pythongis.org>`_ -project which is an open online book giving an *Introduction to Python for Geographic Data Analysis*. Although related, the book and this website have separate lives and are not strictly bound to each other. 

**Inspiration**: This website is heavily inspired by `pyviz.org <http://pyviz.org>`_ which provides similar information related to Python
visualization libraries. However, the websites do not have anything else in common (except the inspiration), as the underlying mechanisms
for generating the content are totally different.

**Acknowledgements**: There are many sources for the packages listed on this website. Many people helped gathering the information by answering to a `call on Twitter <https://twitter.com/tenkahen/status/1538916633024073732>`_. Especially useful sources of information have been earlier listings at `Awesome-Geospatial <https://github.com/sacridini/Awesome-Geospatial>`_ by Eduardo Lacerda and `Python-geospatial <https://github.com/giswqs/python-geospatial>`_ by Qiusheng Wu. 

**Please help**: If you would like to help contributing to this website or maintaining the tool that make this website possible, please contact via Github. Read more from :ref:`Contribution guidelines <contributing>`. We are looking for people who would like to help maintaining this project that aims to be a tool for common use.

**Citing and license:** The tool is licensed with MIT (`read license <https://github.com/pygieons/pygieons/blob/main/LICENSE>`_). The outputs of this tool and website can be used and are licensed under Creative Commons 4.0 BY-SA. If you use the visualizations for any purpose, please cite appropariately the source:

.. code:: 

    @article{Tenkanen_2022,
        author={Tenkanen, Henrikki},
        title={pygieons: Software to visualize Python OS Ecosystem for GIS and Earth Observation},
        journal={URL: https://github.com/pygieons/pygieons},
        year={2022},
    }



.. toctree::
   :maxdepth: 2
   :caption: Tools

   all-tools.ipynb
   vector-libraries.ipynb
   raster-libraries.ipynb
   generic-libraries.ipynb
   
.. toctree::
   :maxdepth: 2
   :caption: Maintenance

   contributing.ipynb
   pygieons.ipynb
   