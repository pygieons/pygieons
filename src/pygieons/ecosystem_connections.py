# Edge connections
# ----------------
# Note: These are not necessarily hard dependencies,
# but a link might sometime illustrate a typical connection to broader Geo-Python ecosystem.
# Packages that require installing external GIS desktop (GUI) software,
# such as database (Postgres/GIS) or desktop GIS (QGIS, ArcGIS etc.) are not included.
LINKS = [
    {"from": "access", "to": "pysal"},
    {"from": "astropy", "to": "numpy"},
    {"from": "astropy", "to": "scipy"},
    {"from": "astropy", "to": "matplotlib"},
    {"from": "basemap", "to": "matplotlib"},
    {"from": "basemap", "to": "numpy"},
    {"from": "basemap", "to": "pyproj"},
    {"from": "basemap", "to": "pyshp"},
    {"from": "contextily", "to": "geopandas"},
    {"from": "contextily", "to": "matplotlib"},
    {"from": "cudf", "to": "pandas"},
    {"from": "cudf", "to": "pyarrow"},
    {"from": "cuspatial", "to": "cudf"},
    {"from": "cuspatial", "to": "geopandas"},
    {"from": "dask-geopandas", "to": "geopandas"},
    {"from": "earthpy", "to": "geopandas"},
    {"from": "earthpy", "to": "matplotlib"},
    {"from": "earthpy", "to": "rasterio"},
    {"from": "earthpy", "to": "scikit-image"},
    {"from": "easystac", "to": "planetary-computer"},
    {"from": "easystac", "to": "radiant-mlhub"},
    {"from": "easystac", "to": "stackstac"},
    {"from": "eomaps", "to": "cartopy"},
    {"from": "eomaps", "to": "geopandas"},
    {"from": "eomaps", "to": "mapclassify"},
    {"from": "eomaps", "to": "pyepsg"},
    {"from": "esda", "to": "pysal"},
    {"from": "fiona", "to": "GDAL"},
    {"from": "geemap", "to": "earthengine-api"},
    {"from": "geemap", "to": "folium"},
    {"from": "geemap", "to": "geojson"},
    {"from": "geemap", "to": "geopandas"},
    {"from": "geemap", "to": "matplotlib"},
    {"from": "geemap", "to": "numpy"},
    {"from": "geemap", "to": "pycrs"},
    {"from": "geemap", "to": "xyzservices"},
    {"from": "gempy", "to": "matplotlib"},
    {"from": "gempy", "to": "networkx"},
    {"from": "gempy", "to": "pandas"},
    {"from": "gempy", "to": "pyvista"},
    {"from": "gempy", "to": "scikit-image"},
    {"from": "gempy", "to": "seaborn"},
    {"from": "geoalchemy2", "to": "geopandas"},
    {"from": "geocube", "to": "geopandas"},
    {"from": "geocube", "to": "xarray"},
    {"from": "geopandas", "to": "contextily"},
    {"from": "geopandas", "to": "fiona"},
    {"from": "geopandas", "to": "folium"},
    {"from": "geopandas", "to": "geopy"},
    {"from": "geopandas", "to": "matplotlib"},
    {"from": "geopandas", "to": "pandas"},
    {"from": "geopandas", "to": "pygeos"},
    {"from": "geopandas", "to": "pyproj"},
    {"from": "geopandas", "to": "rtree"},
    {"from": "geopandas", "to": "shapely"},
    {"from": "geoplot", "to": "geopandas"},
    {"from": "geosnap", "to": "geopandas"},
    {"from": "geosnap", "to": "pysal"},
    {"from": "geowombat", "to": "dask"},
    {"from": "geowombat", "to": "geopandas"},
    {"from": "geowombat", "to": "rasterio"},
    {"from": "geowombat", "to": "scikit-learn"},
    {"from": "geowombat", "to": "scipy"},
    {"from": "geowombat", "to": "xarray"},
    {"from": "giddy", "to": "pysal"},
    {"from": "gstools", "to": "pykrige"},
    {"from": "gstools", "to": "scipy"},
    {"from": "h3", "to": "geopandas"},
    {"from": "h3", "to": "numpy"},
    {"from": "hvplot", "to": "bokeh"},
    {"from": "hvplot", "to": "datashader"},
    {"from": "hvplot", "to": "geopandas"},
    {"from": "hvplot", "to": "geoviews"},
    {"from": "hvplot", "to": "holoviews"},
    {"from": "hvplot", "to": "matplotlib"},
    {"from": "hvplot", "to": "plotly"},
    {"from": "hvplot", "to": "xarray"},
    {"from": "inequality", "to": "pysal"},
    {"from": "iris", "to": "cartopy"},
    {"from": "iris", "to": "matplotlib"},
    {"from": "iris", "to": "pandas"},
    {"from": "iris", "to": "scipy"},
    {"from": "keplergl", "to": "geopandas"},
    {"from": "keplergl", "to": "pydeck"},
    {"from": "laspy", "to": "numpy"},
    {"from": "leafmap", "to": "geopandas"},
    {"from": "leafmap", "to": "keplergl"},
    {"from": "leafmap", "to": "laspy"},
    {"from": "leafmap", "to": "pystac-client"},
    {"from": "leafmap", "to": "rio-cogeo"},
    {"from": "leafmap", "to": "rioxarray"},
    {"from": "legendgram", "to": "pysal"},
    {"from": "libpysal", "to": "pysal"},
    {"from": "libpysal", "to": "scipy"},
    {"from": "lidar", "to": "pyshp"},
    {"from": "lidar", "to": "richdem"},
    {"from": "lidar", "to": "scikit-image"},
    {"from": "lidar", "to": "scipy"},
    {"from": "lidar", "to": "whitebox"},
    {"from": "mapclassify", "to": "geopandas"},
    {"from": "mapclassify", "to": "pysal"},
    {"from": "mesa-geo", "to": "geopandas"},
    {"from": "mesa-geo", "to": "mesa"},
    {"from": "mgwr", "to": "pysal"},
    {"from": "momepy", "to": "pysal"},
    {"from": "movingpandas", "to": "bokeh"},
    {"from": "movingpandas", "to": "cartopy"},
    {"from": "movingpandas", "to": "geopandas"},
    {"from": "movingpandas", "to": "geoviews"},
    {"from": "movingpandas", "to": "hvplot"},
    {"from": "mplleaflet", "to": "geopandas"},
    {"from": "mplleaflet", "to": "matplotlib"},
    {"from": "mplleaflet", "to": "numpy"},
    {"from": "obspy", "to": "cartopy"},
    {"from": "obspy", "to": "geographiclib"},
    {"from": "obspy", "to": "pyproj"},
    {"from": "obspy", "to": "pyshp"},
    {"from": "obspy", "to": "scipy"},
    {"from": "odc-stac", "to": "pandas"},
    {"from": "odc-stac", "to": "pystac"},
    {"from": "odc-stac", "to": "rasterio"},
    {"from": "odc-stac", "to": "xarray"},
    {"from": "osmnet", "to": "pandana"},
    {"from": "osmnx", "to": "folium"},
    {"from": "osmnx", "to": "geopandas"},
    {"from": "osmnx", "to": "geopy"},
    {"from": "osmnx", "to": "networkx"},
    {"from": "owslib", "to": "geopandas"},  # OWSLib provides OGC API connection both for vector (WFS) and raster (WCS)
    {"from": "owslib", "to": "pyproj"},
    {"from": "owslib", "to": "rasterio"},
    {"from": "owslib", "to": "xarray"},
    {"from": "pandana", "to": "pandas"},
    {"from": "pandana", "to": "scikit-learn"},
    {"from": "pandas", "to": "numpy"},
    {"from": "pandas", "to": "pyarrow"},
    {"from": "pandas", "to": "xarray"},
    {"from": "pandas-bokeh", "to": "bokeh"},
    {"from": "pandas-bokeh", "to": "geopandas"},
    {"from": "PDAL", "to": "numpy"},
    {"from": "plotly", "to": "geopandas"},
    {"from": "plotly", "to": "pandas"},
    {"from": "pointpats", "to": "pysal"},
    {"from": "proplot", "to": "cartopy"},
    {"from": "proplot", "to": "matplotlib"},
    {"from": "pygmt", "to": "netcdf4"},
    {"from": "pygmt", "to": "pandas"},
    {"from": "pygmt", "to": "xarray"},
    {"from": "pyinterpolate", "to": "geopandas"},
    {"from": "pyinterpolate", "to": "scipy"},
    {"from": "pykrige", "to": "scikit-learn"},
    {"from": "pykrige", "to": "scipy"},
    {"from": "pymap3d", "to": "astropy"},
    {"from": "pymap3d", "to": "xarray"},
    {"from": "pyntcloud", "to": "laspy"},
    {"from": "pyntcloud", "to": "matplotlib"},
    {"from": "pyntcloud", "to": "pandas"},
    {"from": "pyntcloud", "to": "pyvista"},
    {"from": "pyntcloud", "to": "scipy"},
    {"from": "pyogrio", "to": "geopandas"},
    {"from": "pyogrio", "to": "pygeos"},
    {"from": "pyproj", "to": "PROJ"},
    {"from": "pyrat", "to": "GDAL"},
    {"from": "pyrat", "to": "matplotlib"},
    {"from": "pyrat", "to": "scikit-image"},
    {"from": "pyrat", "to": "scipy"},
    {"from": "pyrosar", "to": "geoalchemy2"},
    {"from": "pyrosar", "to": "numpy"},
    {"from": "pyrosm", "to": "geopandas"},
    {"from": "pyrosm", "to": "networkx"},
    {"from": "pyrosm", "to": "osmnx"},
    {"from": "pyrosm", "to": "pandana"},
    {"from": "pyrosm", "to": "python-igraph"},
    {"from": "pyrosm", "to": "vaex"},
    {"from": "pysal", "to": "geopandas"},
    {"from": "pysal", "to": "scipy"},
    {"from": "pysheds", "to": "geojson"},
    {"from": "pysheds", "to": "numba"},
    {"from": "pysheds", "to": "numpy"},
    {"from": "pysheds", "to": "pandas"},
    {"from": "pysheds", "to": "pyproj"},
    {"from": "pysheds", "to": "rasterio"},
    {"from": "pysheds", "to": "scikit-image"},
    {"from": "pysheds", "to": "scipy"},
    {"from": "pyspatialml", "to": "geopandas"},
    {"from": "pyspatialml", "to": "rasterio"},
    {"from": "pyspatialml", "to": "scikit-learn"},
    {"from": "pystac-client", "to": "pyproj"},
    {"from": "pyvista-xarray", "to": "dask"},
    {"from": "pyvista-xarray", "to": "pyvista"},
    {"from": "pyvista-xarray", "to": "rioxarray"},
    {"from": "pyvista-xarray", "to": "xarray"},
    {"from": "r5py", "to": "geopandas"},
    {"from": "radiant-mlhub", "to": "pystac"},
    {"from": "radiant-mlhub", "to": "shapely"},
    {"from": "rasterio", "to": "affine"},
    {"from": "rasterio", "to": "GDAL"},
    {"from": "rasterio", "to": "matplotlib"},
    {"from": "rasterio", "to": "numpy"},
    {"from": "rasterstats", "to": "rasterio"},
    {"from": "richdem", "to": "GDAL"},
    {"from": "richdem", "to": "numpy"},
    {"from": "rio-color", "to": "rasterio"},
    {"from": "rio-hist", "to": "matplotlib"},
    {"from": "rio-hist", "to": "rasterio"},
    {"from": "rio-hist", "to": "rio-color"},
    {"from": "rio-hist", "to": "rio-mucho"},
    {"from": "rio-mucho", "to": "rasterio"},
    {"from": "rio-tiler", "to": "rasterio"},
    {"from": "rio-tiler", "to": "rio-color"},
    {"from": "rio-tiler", "to": "pystac"},
    {"from": "rioxarray", "to": "rasterio"},
    {"from": "rioxarray", "to": "xarray"},
    {"from": "salem", "to": "pandas"},
    {"from": "salem", "to": "pyproj"},
    {"from": "salem", "to": "scipy"},
    {"from": "salem", "to": "xarray"},
    {"from": "sarpy", "to": "scipy"},
    {"from": "sarsen", "to": "pandas"},
    {"from": "sarsen", "to": "rioxarray"},
    {"from": "sarsen", "to": "xarray"},
    {"from": "sarsen", "to": "xarray-sentinel"},
    {"from": "satpy", "to": "dask"},
    {"from": "satpy", "to": "geoviews"},
    {"from": "satpy", "to": "pyproj"},
    {"from": "satpy", "to": "rioxarray"},
    {"from": "satpy", "to": "xarray"},
    {"from": "satpy", "to": "zarr"},
    {"from": "scikit-mobility", "to": "folium"},
    {"from": "scikit-mobility", "to": "geopandas"},
    {"from": "scikit-mobility", "to": "python-igraph"},
    {"from": "scikit-mobility", "to": "scikit-learn"},
    {"from": "scipy", "to": "numpy"},
    {"from": "seaborn", "to": "matplotlib"},
    {"from": "segregation", "to": "pysal"},
    {"from": "sentinelsat", "to": "geojson"},
    {"from": "shapely", "to": "GEOS"},
    {"from": "shapely", "to": "numpy"},
    {"from": "snkit", "to": "geopandas"},
    {"from": "snkit", "to": "networkx"},
    {"from": "spaghetti", "to": "pysal"},
    {"from": "spglm", "to": "pysal"},
    {"from": "spint", "to": "pysal"},
    {"from": "splot", "to": "pysal"},
    #{"from": "spopt", "to": "networkx"},
    {"from": "spopt", "to": "pysal"},
    #{"from": "spopt", "to": "scipy"},
    {"from": "spopt", "to": "spaghetti"},
    {"from": "spreg", "to": "pysal"},
    {"from": "spvcm", "to": "pysal"},
    {"from": "spyndex", "to": "earthengine-api"},
    {"from": "spyndex", "to": "eemont"},
    {"from": "spyndex", "to": "matplotlib"},
    {"from": "spyndex", "to": "pandas"},
    {"from": "spyndex", "to": "seaborn"},
    {"from": "spyndex", "to": "xarray"},
    {"from": "stackstac", "to": "pyproj"},
    {"from": "stackstac", "to": "pystac-client"},
    {"from": "stackstac", "to": "rasterio"},
    {"from": "stackstac", "to": "scipy"},
    {"from": "stackstac", "to": "xarray"},
    {"from": "statsmodels", "to": "pandas"},
    {"from": "statsmodels", "to": "scipy"},
    {"from": "tobler", "to": "pysal"},
    {"from": "trackintel", "to": "geoalchemy2"},
    {"from": "trackintel", "to": "geopandas"},
    {"from": "trackintel", "to": "osmnx"},
    {"from": "trackintel", "to": "scikit-learn"},
    {"from": "transbigdata", "to": "geopandas"},
    {"from": "transbigdata", "to": "keplergl"},
    {"from": "transbigdata", "to": "matplotlib"},
    {"from": "transbigdata", "to": "networkx"},
    {"from": "transbigdata", "to": "seaborn"},
    {"from": "urbanaccess", "to": "osmnet"},
    {"from": "urbanaccess", "to": "pandana"},
    {"from": "urbansim", "to": "pandana"},
    {"from": "urbansim", "to": "pandas"},
    {"from": "urbansim", "to": "scipy"},
    {"from": "urbansim", "to": "statsmodels"},
    {"from": "vaex", "to": "pandas"},
    {"from": "verde", "to": "pandas"},
    {"from": "verde", "to": "scikit-learn"},
    {"from": "verde", "to": "scipy"},
    {"from": "verde", "to": "xarray"},
    {"from": "vizent", "to": "cartopy"},
    {"from": "vizent", "to": "matplotlib"},
    {"from": "xarray_leaflet", "to": "xarray"},
    {"from": "xarray-sentinel", "to": "pandas"},
    {"from": "xarray-sentinel", "to": "rioxarray"},
    {"from": "xarray-spatial", "to": "datashader"},
    {"from": "xarray-spatial", "to": "xarray"},
    {"from": "xarray", "to": "numpy"},
]
