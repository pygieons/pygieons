import pandas as pd
import pypistats
import json
import numpy as np
import palettable as palette
from pyvis.network import Network
import time
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
                            PYGIS_CORE,
                            FUNDAMENTAL_CORE
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

    return nodes, edges


def assign_categories(nodes):
    """Adds a column to nodes DataFrame about subcategories"""
    # Update categories
    for category, data in PKGS.items():
        nodes.loc[nodes["id"].isin(data["pkgs"]), "category"] = category
    return nodes


def get_number_of_pypi_downloads(nodes, sleep_time=0.5):
    """Finds out the number of monthly downloads according to pypistats"""
    print("Find out the number of monthly downloads from PyPi for the libraries ..")
    nodes["downloads"] = None

    # Update downloads
    for idx, row in tqdm(nodes.iterrows(), total=nodes.shape[0]):
        name = row["id"]
        category = row["category"]
        nodes.loc[idx, "subcategory"] = get_subcategory(name, category, PKGS)

        if name in NO_DISTRO:
            continue

        r = pypistats.recent(name, "month", format="json")
        downloads = json.loads(r)["data"]["last_month"]
        nodes.loc[idx, "downloads"] = downloads
        time.sleep(sleep_time)

    # Scale the download values by taking a log
    nodes["log10_downloads"] = np.log10(nodes["downloads"].astype(float))
    nodes["log2_downloads"] = np.log2(nodes["downloads"].astype(float))
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


def prepare_network_plot(nt, nodes, edges, plot_type, label_fontsize, font_family, edge_color, color_palette):
    """Prepares a pyvis network that can be used to visualize it"""
    # Take a copy of nodes
    nodes_copy = nodes.copy()

    if plot_type == "all":
        pass
    elif plot_type == "vector":
        nodes_copy = nodes_copy.loc[nodes_copy["subcategory"].isin(["vector", "generic"])].copy()
    elif plot_type == "raster":
        nodes_copy = nodes_copy.loc[nodes_copy["subcategory"].isin(["raster", "generic"])].copy()

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


def prepare_net(dark_background=False,
                directed_graph=True,
                label_fontsize=24,
                font_family="verdana",
                plot_type="all",
                color_palette=None,
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
    plot_type : str
        This can be used to specify if you want to plot all packages in same figure, or only vector or raster.
        Possible values are: "all", "vector", "raster".
    color_palette : list of hex colors
        By default the color are based on palettable color schemes, but you can customize the colors by passing a list of
        four colors as hex codes.
    show_buttons : bool
        If True, adds a control panel underneath the visualization which allows you to play around with different settings for the graph.
    """

    # ===============
    # PARAMS
    # ===============

    # Load nodes and edges
    nodes, edges = load_nodes_and_edges()

    # Assign categories
    nodes = assign_categories(nodes)

    # Retrieve the number of downloads
    nodes = get_number_of_pypi_downloads(nodes)

    # Initialize the network and colors
    if dark_background:
        edge_color = "lightblue"
        if color_palette is None:
            color_palette = palette.cartocolors.qualitative.Pastel_4.hex_colors
        nt = Network('1000px', '1500px', notebook=True, bgcolor='black', font_color='white', directed=directed_graph)
    else:
        edge_color = "grey"
        nt = Network('1000px', '1500px', notebook=True, directed=directed_graph)

        # Use the first 4 colours from GrandBudapest5_5 which gives quite nice appearance
        if color_palette is None:
            color_palette = palette.wesanderson.GrandBudapest5_5.hex_colors

    # Gravity model
    nt.force_atlas_2based(central_gravity=0.02, overlap=0.3)

    # Prepare the plot
    nt = prepare_network_plot(nt, nodes, edges, plot_type, label_fontsize, font_family, edge_color, color_palette)

    if show_buttons:
        nt.show_buttons(filter_=['physics', 'nodes'])
    return nt
