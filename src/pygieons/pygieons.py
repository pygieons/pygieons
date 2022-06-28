import pandas as pd
import pypistats
import json
import numpy as np
import palettable as palette
from pyvis.network import Network
import time
import requests
from bs4 import BeautifulSoup
from IPython.display import HTML
from tqdm.auto import tqdm

tqdm.pandas()

# Load edges
from .ecosystem_connections import LINKS
# Load nodes according to categories
from .ecosystem_pkgs import (PKGS,
                             NO_DISTRO,
                             GENERIC_CORE,
                             GIS_CORE,
                             GENERIC_VISUALS,
                             NOT_ACTIVE,
                             FUNDAMENTAL_CORE,
                             NO_CONDA_FORGE_DISTRO,
                             )

# These packages won't be plotted
SKIPPED = NO_DISTRO + NOT_ACTIVE


def load_nodes_and_edges():
    """Loads nodes and edges based on links assigned in ecosystem_connections.py """
    edges = pd.DataFrame(LINKS)
    edges = edges.drop_duplicates()

    # Extract node list and assign URLs to PyPi
    pkgs = list(set(edges["from"].to_list() + edges["to"].to_list()))
    node_list = [{"id": pkg, "category": None, "url": f"https://pypi.org/project/{pkg}/"} for pkg in pkgs]
    nodes = pd.DataFrame(node_list)

    # Sort
    nodes = nodes.sort_values(by=["id"]).copy()

    return nodes, edges


def clean_nodes(nodes):
    """Removes pkgs which are not available from PyPi or which are not maintained anymore."""
    nodes = nodes.loc[~nodes["id"].isin(NOT_ACTIVE + NO_DISTRO)].copy()
    return nodes


def assign_categories(nodes):
    """Adds a column to nodes DataFrame about categories and subcategories"""
    # Update categories
    for category, data in PKGS.items():
        nodes.loc[nodes["id"].isin(data["pkgs"]), "category"] = category

    for idx, row in nodes.iterrows():
        name = row["id"]
        category = row["category"]
        nodes.loc[idx, "subcategory"] = get_subcategory(name, category, PKGS)

    return nodes


def get_number_of_pypi_downloads(nodes, sleep_time=0.25, log=True):
    """Finds out the number of monthly downloads according to pypistats"""
    disable = True
    if log:
        print("Find out the number of monthly downloads from PyPi for the libraries ..")
        disable = False
    nodes["PyPi downloads (monthly)"] = None

    # Update downloads
    for idx, row in tqdm(nodes.iterrows(), total=nodes.shape[0], disable=disable):
        name = row["id"]
        if name in NO_DISTRO:
            continue
        r = pypistats.recent(name, "month", format="json")
        downloads = json.loads(r)["data"]["last_month"]
        nodes.loc[idx, "PyPi downloads (monthly)"] = downloads
        time.sleep(sleep_time)

    # Scale the download values by taking a log
    nodes["log10_downloads"] = np.log10(nodes["PyPi downloads (monthly)"].astype(float))
    nodes["log2_downloads"] = np.log2(nodes["PyPi downloads (monthly)"].astype(float))
    return nodes


def get_project_details(nodes, log=True):
    """Finds out the Home and Documentation URLs and project description from PyPi project page"""
    disable = True
    if log:
        print("Extract project details ..")
        disable = False

    for idx, node in tqdm(nodes.iterrows(), total=nodes.shape[0], disable=disable):
        url = node["url"]
        name = node["id"]

        if name in NO_DISTRO:
            continue

        # Retrieve data
        response = requests.get(url)

        # Make soup
        soup = BeautifulSoup(response.text, features="lxml")

        # Find links to homepage and docs
        project_links = soup.find_all("div", {'class': 'sidebar-section'})[1].find_all("a", href=True)
        homepage = None
        docs_url = None
        description = "NA"

        for link in project_links:
            if link.text.strip().lower().startswith("home"):
                homepage = link["href"]
            elif link.text.strip().lower().startswith("doc"):
                docs_url = link["href"]

        nodes.loc[idx, "homepage_url"] = homepage
        nodes.loc[idx, "docs_url"] = docs_url
        nodes.loc[idx, "Homepage"] = f'<a href="{homepage}">🏠</a>'
        if docs_url is not None:
            nodes.loc[idx, "Documentation"] = f'<a href="{docs_url}">📖</a>'
        else:
            nodes.loc[idx, "Documentation"] = 'NA'

        # Project description
        description = soup.find("p", {'class': "package-description__summary"}).text
        nodes.loc[idx, "Info"] = f'<span title="{description}"><strong>ⓘ</strong></span>'

        time.sleep(0.25)
    return nodes


def prepare_html_links_and_badges(nodes):
    """Prepares HTML links and badges for Python projects"""
    pypi_root = "https://pypi.org/project"
    pypistats_root = "https://pypistats.org/packages"
    fury_root = "https://badge.fury.io/py"
    shields_root = "https://img.shields.io/pypi/dm"
    conda_root = "https://anaconda.org/conda-forge"
    nodes['pypi_link'] = nodes["id"].apply(lambda x: f'{pypi_root}/{x}/')
    nodes["PyPi version"] = nodes['id'].apply(lambda x: f'<a href="{pypi_root}/{x}/">'
                                                        f'<img src="{fury_root}/{x}.svg" '
                                                        f'alt="PyPI version" height="18"></a>')
    nodes["PyPi downloads"] = nodes['id'].apply(lambda x: f'<a href="{pypistats_root}/{x}/">'
                                                          f'<img src="{shields_root}/{x}'
                                                          f'?color=yellow&label=Downloads" '
                                                          f'alt="PyPI downloads" height="18"></a>')
    nodes["Conda-forge version"] = nodes['id'].apply(lambda x: f'<a href="{conda_root}/{x}/">'
                                                               f'<img src="{conda_root}/{x}/badges/version.svg" '
                                                               f'alt="Conda version"></a>')
    nodes["Conda-forge downloads"] = nodes['id'].apply(lambda x: f'<a href="{conda_root}/{x}/">'
                                                                 f'<img src="{conda_root}/{x}/badges/downloads.svg" '
                                                                 f'alt="Conda downloads"></a>')
    nodes["Conda-forge latest release"] = nodes['id'].apply(lambda x: f'<a href="{conda_root}/{x}/">'
                                                                      f'<img src="{conda_root}/{x}/badges/latest_release_date.svg" '
                                                                      f'alt="Conda latest release"></a>')

    nodes["License"] = nodes['id'].apply(lambda x: f'<a href="{conda_root}/{x}/">'
                                                   f'<img src="{conda_root}/{x}/badges/license.svg" '
                                                   f'alt="License"></a>')

    # If package is not available on conda-forge remove badge
    nodes.loc[nodes["id"].isin(NO_CONDA_FORGE_DISTRO), "Conda-forge version"] = "NA"
    nodes.loc[nodes["id"].isin(NO_CONDA_FORGE_DISTRO), "Conda-forge downloads"] = "NA"
    nodes.loc[nodes["id"].isin(NO_CONDA_FORGE_DISTRO), "Conda-forge latest release"] = "NA"
    nodes.loc[nodes["id"].isin(NO_CONDA_FORGE_DISTRO), "License"] = "NA"

    nodes["Name"] = "<strong>" + nodes["id"] + "</strong>"

    if isinstance(nodes.iloc[0]["PyPi downloads (monthly)"], int):
        nodes["PyPi downloads (monthly)"] = nodes["PyPi downloads (monthly)"].map('{:,.0f}'.format)

    return nodes


def get_subcategory(name, category, categories):
    """Finds out to which subcategory a package belong to"""
    try:
        if name in categories[category]["vector"]:
            return "vector"
        if name in categories[category]["raster"]:
            return "raster"
        if name in categories[category]["generic"]:
            return "generic"
    except Exception:
        print(f"Library '{name}' does not seem to be part of any category.")


def get_color(category, color_palette):
    """Get a color from color scheme based on the type of package"""
    colors = {"analysis / modelling": color_palette[0],
              "core / data structures": color_palette[1],
              "visualization": color_palette[2],
              "data extraction / processing": color_palette[3]}
    return colors[category]


def get_shape(name, nodes_df):
    """Get a shape for the node based on the type of package"""
    shapes = {"vector": "dot",
              "raster": "dot",
              "generic": "dot"}

    if name in GIS_CORE or name in FUNDAMENTAL_CORE:
        return "star"

    if name in GENERIC_CORE or name in GENERIC_VISUALS:
        return "diamond"

    return shapes[nodes_df.loc[nodes_df["id"] == name, "subcategory"].values[0]]


def get_node_color(nodes, name, color_palette):
    """Get a color for package based on its type."""
    # Use default color for these packages
    if name in GIS_CORE or name in FUNDAMENTAL_CORE:
        return None
    try:
        return get_color(nodes.loc[nodes["id"] == name]["category"].values[0], color_palette)
    except Exception:
        raise Exception(f"Package '{name}' does not seem to be part of any category. Please check.")


def get_node_size(nodes, name, size_column):
    """Returns a size of the node according the downloads"""
    return nodes.loc[nodes["id"] == name][size_column].values[0]


def prepare_network_plot(nt, nodes, edges, label_fontsize, font_family, edge_color, color_palette):
    """Prepares a pyvis network that can be used to visualize it"""
    # Take a copy of nodes
    nodes_copy = nodes.copy()

    # Pkg names
    pkgs = nodes_copy["id"].to_list()

    # Check if there are pkgs that are not connected to the graph
    edge_ids = list(set(edges["from"].to_list() + edges["to"].to_list()))
    # 1. Keep only ids that are part of selected nodes
    edge_ids = [edge_id for edge_id in edge_ids if edge_id in pkgs]
    # 2. Remove nodes that do not connect to any other node
    not_connected = [pkg for pkg in pkgs if pkg not in edge_ids]

    # Add nodes
    for idx, node in nodes_copy.iterrows():
        name = node["id"]

        if name in SKIPPED or name in not_connected:
            continue

        url = node["url"]
        nt.add_node(n_id=name, label=name, title=f'<a href="{url}" target="_blank">{name}</a>',
                    size=get_node_size(nodes, name, "log2_downloads"),
                    color=get_node_color(nodes, name=name, color_palette=color_palette),
                    font={"size": label_fontsize, "face": font_family}, shape=get_shape(name, nodes))

    # Add edges
    for idx, edge in edges.iterrows():
        source = edge["from"]
        target = edge["to"]

        # If pkg has been tagged as SKIPPED
        if source in SKIPPED or target in SKIPPED:
            continue

        # If pkg is not part of the nodes (e.g. if plotting only vector or raster data)
        if source not in pkgs or target not in pkgs:
            continue

        nt.add_edge(source, target, color=edge_color)

    # Add Legend Nodes
    step = 80
    x = -1900
    y = 200

    for i, key in enumerate(PKGS.keys()):
        nt.add_node(n_id=i, group=key, label=key, size=150, physics=False, x=x, y=f"{y + i * step}px", shape="box",
                    widthConstraint=300, font={"size": 30, "color": "white", "face": font_family},
                    color=get_color(key, color_palette))

        # Add legend for symbols
    i += 1
    nt.add_node(n_id=i, label="Python GIS library", size=20, physics=False, x=x, y=f"{y + i * step}px", shape="dot",
                color="grey", font={"size": 30, "face": font_family})
    i += 1
    nt.add_node(n_id=i, label="Fundamental underlying\nC/C++ library", size=20, physics=False, x=x,
                y=f"{y + i * step * 1.05}px", shape="star", color="grey", font={"size": 30, "face": font_family})
    i += 1
    nt.add_node(n_id=i, label="Generic library\nnot specific to GIS", size=20, physics=False, x=x,
                y=f"{y + i * (step * 1.15)}px", shape="diamond", color="grey", font={"size": 30, "face": font_family})
    return nt


def prepare_table_plot(nodes, cols):
    """
    Prepares a pandas.HTML table for the Python GIS libraries that are currently listed in pygieons.
    """
    align_center_cols = ["Homepage"]

    if "Documentation" in cols:
        align_center_cols.append("Documentation")

    # Style properties
    style_props = [
        # Column headers
        dict(selector="th", props=[("font-size", "100%"),
                                   ("text-align", "center"),
                                   ("background-color", "#F0F3CF"),
                                   ]),
        # Table titles
        dict(selector="caption", props=[("caption-side", "top"),
                                        ("font-size", "130%"),
                                        ("font-weight", "bold"),
                                        ("text-align", "left"),
                                        ('height', '50px'),
                                        ('color', 'black')]),
        # Table content text
        dict(selector="td", props=[("font-size", "90%"),
                                   ("text-align", "center"),
                                   ]),

    ]
    # Generate tables from subcategories
    grouped = nodes.groupby("category")

    # Set tooltips
    if "Info" in cols:
        ttips = pd.DataFrame(data=nodes.Info, columns=["Info"], index=nodes.index)
        html_stack = []
        for name, rows in grouped:
            html_stack.append(
                (rows[cols].style
                 .set_properties(subset=align_center_cols, **{"text-align": "center"})
                 .hide(axis="index")
                 .set_caption(f"<strong>{name.capitalize()}</strong>")
                 .set_tooltips(ttips)
                 .set_table_styles(style_props)
                 .to_html())
            )

        return HTML("".join(html_stack))

    html_stack = []
    for name, rows in grouped:
        html_stack.append(
            (rows[cols].style
             .set_properties(subset=align_center_cols, **{"text-align": "center"})
             .hide(axis="index")
             .set_caption(f"<strong>{name.capitalize()}</strong>")
             .set_table_styles(style_props)
             .to_html())
        )
    return HTML("".join(html_stack))


class Table:
    def __init__(self, tableview):
        """A simple wrapper to imitate similar behavior as with pyvis.Network visualization."""
        self.tableview = tableview

    def show(self):
        return self.tableview


class Net:
    def __init__(self, network_view):
        """A simple wrapper to imitate similar behavior as with pyvis.Network visualization."""
        self.network_view = network_view

    def show(self):
        return HTML(self.network_view.generate_html(notebook=True))

    def save(self, output_fp=None):
        self.network_view.write_html(output_fp)


class Ecosystem:
    def __init__(self, plot_type="all", keep_all=False, log=True):
        """
        A class for parsing and visualization information about Python GIS ecosystem

        Parameters
        ==========

        plot_type : str
            This can be used to specify if you want to plot all packages in same figure, or only vector or raster.
            Possible values are: "all", "vector", "raster", "generic", "vector+generic", "raster+generic".
        keep_all : bool
            If True, also packages that are not available from PyPi or which are not maintained will be kept.
        log: bool
            If True, will print messages during process.
        """
        self.nodes = None
        self.edges = None
        self.plot_type = plot_type
        self.keep_all = keep_all
        self.log = log

    def prepare_data(self, parse_urls=False):
        """Loads the data and filters it if needed."""
        # Load nodes and edges
        nodes, edges = load_nodes_and_edges()

        # Assign categories
        nodes = assign_categories(nodes)

        if self.plot_type == "all":
            pass
        elif self.plot_type.lower() == "vector":
            nodes = nodes.loc[nodes["subcategory"].isin(["vector"])].copy()
        elif self.plot_type.lower() == "raster":
            nodes = nodes.loc[nodes["subcategory"].isin(["raster"])].copy()
        elif self.plot_type.lower() == "generic":
            nodes = nodes.loc[nodes["subcategory"].isin(["generic"])].copy()
        elif self.plot_type.lower() == "vector+generic":
            nodes = nodes.loc[nodes["subcategory"].isin(["vector", "generic"])].copy()
        elif self.plot_type.lower() == "raster+generic":
            nodes = nodes.loc[nodes["subcategory"].isin(["raster", "generic"])].copy()
        else:
            raise ValueError(f"'plot_type' can be 'all', 'vector', 'raster', 'vector+generic', "
                             f"or 'raster+generic'. Got: {self.plot_type}")

        # Drop packages that are not available from PyPi or which are not active
        if not self.keep_all:
            nodes = clean_nodes(nodes)

        # Retrieve the number of downloads
        if "downloads" not in nodes.columns.to_list():
            nodes = get_number_of_pypi_downloads(nodes, log=self.log)

        # Retrieve the project URLs (homepage and docs URL)
        if parse_urls:
            nodes = get_project_details(nodes, log=self.log)

        # Update attributes
        self.nodes = nodes
        self.edges = edges

    def prepare_net(self,
                    dark_background=False,
                    directed_graph=True,
                    label_fontsize=24,
                    font_family="verdana",
                    color_palette=None,
                    fig_width="900px",
                    fig_height="700px",
                    show_buttons=False,
                    ):
        """
        Prepares a pyvis.Network for the Python GIS libraries that are currently listed in pygieons.

        Parameters
        ==========

        directed_graph : bool
            Treat the network as directed. If True, will add arrows showing the direction of the link.
        dark_background : bool
            If True, will produce the visualization with dark background.
        label_fontsize : int
            Fontsize for the labels.
        font_family : str
            Font family applied to labels. Possible values "arial", "verdana", "tahoma".
        color_palette : list of hex colors
            By default the color are based on palettable color schemes, but you can customize the colors by passing a list of
            four colors as hex codes.
        fig_width : str
            Width of the figure in pixels.
        fig_height : str
            Height of the figure in pixels.
        show_buttons : bool
            If True, adds a control panel underneath the visualization which allows you to play around with different settings for the graph.
        """

        # Parse data
        if self.nodes is None:
            self.prepare_data(parse_urls=False)

        # ===============
        # PARAMS
        # ===============

        # Initialize the network and colors
        if dark_background:
            edge_color = "lightblue"
            if color_palette is None:
                color_palette = palette.cartocolors.qualitative.Pastel_4.hex_colors
            nt = Network(widht=fig_width, height=fig_height, notebook=True, bgcolor='black', font_color='white',
                         directed=directed_graph)
        else:
            edge_color = "grey"
            nt = Network(width=fig_width, height=fig_height, notebook=True, directed=directed_graph)

            # Use the first 4 colours from GrandBudapest5_5 which gives quite nice appearance
            if color_palette is None:
                color_palette = palette.wesanderson.GrandBudapest5_5.hex_colors

        # Gravity model
        nt.force_atlas_2based(central_gravity=0.02, overlap=0.3)

        # Prepare the plot
        nt = prepare_network_plot(nt,
                                  self.nodes,
                                  self.edges,
                                  label_fontsize,
                                  font_family,
                                  edge_color,
                                  color_palette
                                  )

        if show_buttons:
            nt.show_buttons(filter_=['physics', 'nodes'])
        return Net(network_view=nt)

    def prepare_table(self,
                      cols=[
                          "Name",
                          "Homepage",
                          "Info",
                          "License",
                          "PyPi version",
                          "PyPi downloads (monthly)",
                          "Conda-forge version",
                          "Conda-forge downloads",
                          "Conda-forge latest release"
                      ]
                      ):
        """
        Prepares a pandas.HTML table for the Python GIS libraries that are currently listed in pygieons.

        Parameters
        ==========

        cols : list
            A list of attributes that will be shown in the output table.
            By default, prints out statistics and information both for PyPi and Conda-forge.
        """
        # Parse data
        if self.nodes is None:
            self.prepare_data(parse_urls=True)

        elif "Homepage" not in self.nodes.columns.to_list():
            self.prepare_data(parse_urls=True)

        # Prepare links and badges
        self.nodes = prepare_html_links_and_badges(self.nodes)

        # Prepare table
        return Table(prepare_table_plot(self.nodes, cols))
