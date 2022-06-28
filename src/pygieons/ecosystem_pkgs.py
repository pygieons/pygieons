# Python GIS / geospatial related libraries categorized based on targeted spatial data formats (vector, raster or generic)
# as well as, based on primary usage (core/data structures, visualization, analysis/modelling, data extraction/processing).
# This listing focuses on libraries that can be used programmably from Python.
# Packages that require installing a desktop software or a database (Postgres/GIS, QGIS, ArcGIS etc.)
# are not included. Open source command line software with Python wrappers are included.
# Packages that cannot be installed from PyPi are not recommended to be listed. However, if they are listed,
# they should be added to "no_distro" list below.

# ======================
# Packages by categories
# ======================

PKGS = {
    "core / data structures": {
        "generic": ['GDAL', 'PROJ', 'astropy', 'cudf', 'dask', 'geoalchemy2', 'geojson', 'netcdf4', 'networkx', 'numba',
                    'numpy', 'pandas', 'pyarrow', 'pycrs', 'pyepsg', 'pyproj', 'scipy', 'vaex', 'zarr'],
        "vector": ['GEOS', 'PDAL', 'cuspatial', 'dask-geopandas', 'fiona', 'geographiclib', 'geopandas', 'laspy',
                   'libpysal',
                   'pdal', 'pygeos', 'pyogrio', 'pyshp', 'python-igraph', 'rtree', 'shapely'],
        "raster": ['affine', 'geowombat', 'iris', 'pyrat', 'rasterio', 'rio-cogeo', 'rioxarray', 'sarpy', 'sarsen',
                   'simpleitk', 'xarray'],
    },
    "visualization": {
        "generic": ['basemap', 'bokeh', 'cartopy', 'datashader', 'earthpy', 'eomaps', 'folium', 'geemap', 'gempy',
                    'geoviews', 'holoviews', 'hvplot', 'keplergl', 'leafmap', 'mapclassify', 'matplotlib', 'plotly',
                    'proplot', 'pydeck', 'pygmt', 'pyvista', 'seaborn', 'voila'],
        "vector": ['geoplot', 'legendgram', 'mplleaflet', 'pandas-bokeh', 'vizent'],
        "raster": ['contextily', 'rio-color', 'xarray_leaflet'],
    },
    "analysis / modelling": {
        "generic": ["obspy", "statsmodels"],
        "vector": ['access', 'esda', 'geosnap', 'giddy', 'inequality', 'mesa', 'mesa-geo', 'mgwr', 'momepy',
                   'movingpandas', 'pandana', 'pointpats', 'pyinterpolate', 'pysal', 'r5py', 'scikit-mobility',
                   'segregation', 'spaghetti', 'spglm', 'spint', 'splot', 'spopt', 'spreg', 'spvcm', 'tobler',
                   'trackintel', 'transbigdata', 'urbanaccess', 'urbansim'],
        "raster": ['gstools', 'pykrige', 'pysheds', 'pyspatialml', 'rasterstats', 'richdem', 'scikit-learn', 'spyndex',
                   'xarray-spatial'],
    },
    "data extraction / processing": {
        "generic": ['astropy', 'geocube', 'owslib', 'scikit-image', 'whitebox'],
        "vector": ['geopy', 'h3', 'osmnet', 'osmnx', 'pyntcloud', 'pyrosm', 'snkit'],
        "raster": ['earthengine-api', 'easystac', 'eemont', 'lidar', 'odc-stac', 'planetary-computer', 'pymap3d',
                   'pyotb', 'pyrosar', 'pystac', 'pystac-client', 'radiant-mlhub', 'rio-hist', 'rio-mucho', 'rio-tiler',
                   'salem', 'satpy', 'sentinelsat', 'stackstac', 'verde', 'xarray-sentinel', 'xyzservices'],
    }
}

# ======================
# Special classification
# ======================

# Libraries with no distro (cannot be installed from PyPi or with conda)
NO_DISTRO = ["geowombat", "pyrat"]

# Libraries that which do not seem to be actively maintained
GENERIC_CORE = ['cudf', 'dask', 'h5py', 'netcdf4', 'networkx', 'numba', 'numpy', 'pandas', 'pyarrow', 'python-igraph',
                'scikit-learn', 'scipy', 'vaex']
FUNDAMENTAL_CORE = ["numpy"]
GENERIC_VISUALS = ['holoviews', 'matplotlib', 'pydeck', 'seaborn']
PYGIS_CORE = ['fiona', 'geopandas', 'pyproj', 'pysal', 'rasterio', 'rtree', 'shapely', 'xarray']
GIS_CORE = ["GDAL", "GEOS", "PROJ"]

# Libraries that which do not seem to be actively maintained (many years without activity)
NOT_ACTIVE = ["mplleaflet", "pyrat"]

# Maintenance is questionable, if there are is no clear activity in Github in past year or so
MAYBE_ACTIVE = ["pandana", "urbansim", "vizent"]

# Libraries in their early development
EARLY_DEV = ["easystack", "r5py"]

# External or generic "language-independent" libraries (bindings for Python)
EXTERNAL = ['GDAL', 'GEOS', 'PDAL', 'pyarrow', 'pygmt', 'simpleitk', 'whitebox']

# Packages without conda distribution
NO_CONDA_FORGE_DISTRO = ["cuspatial", "mesa-geo", "pandas-bokeh", "pyinterpolate", "snkit", "trackintel", "vizent",
                         "pyspatialml", "rio-hist", "cudf"]

# --------------------
# Combine packages
# --------------------

core = "core / data structures"
PKGS[core]["pkgs"] = PKGS[core]["generic"] + PKGS[core]["vector"] + PKGS[core]["raster"]

processing = "data extraction / processing"
PKGS[processing]["pkgs"] = PKGS[processing]["generic"] + PKGS[processing]["vector"] + PKGS[processing]["raster"]

analysis = "analysis / modelling"
PKGS[analysis]["pkgs"] = PKGS[analysis]["generic"] + PKGS[analysis]["vector"] + PKGS[analysis]["raster"]
viz = "visualization"
PKGS[viz]["pkgs"] = PKGS[viz]["generic"] + PKGS[viz]["vector"] + PKGS[viz]["raster"]
