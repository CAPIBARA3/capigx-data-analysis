import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import PatchCollection

def generate_tiles(tiling_type, tile_size, projection='mollweide'):
    """
    Generate a tiling map of the sky with specified tile type and size.

    Parameters:
        tiling_type (str): 'circle' or 'square' to specify the tile shape.
        tile_size (float): Size of the tiles in degrees (radius for circle, side length for square).
        projection (str): Type of projection for the map ('mollweide' by default).

    Returns:
        None
    """
    # Convert tile size to radians for plotting
    tile_size_rad = np.radians(tile_size)
    
    # Create figure and axis with chosen projection
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection=projection)
    ax.grid(True)
    ax.set_title(f"{tiling_type.capitalize()} Tiles with {tile_size}' Size")
    
    # Generate tiling for full sky
    patches = []
    step = tile_size_rad if tiling_type == 'circle' else tile_size_rad / np.sqrt(2)
    for lon in np.arange(-180, 180, np.degrees(step)):
        for lat in np.arange(-90, 90, np.degrees(step)):
            x, y = np.radians(lon), np.radians(lat)
            if tiling_type == 'circle':
                patches.append(Circle((x, y), tile_size_rad))
            elif tiling_type == 'square':
                patches.append(Rectangle((x - tile_size_rad/2, y - tile_size_rad/2),
                                         tile_size_rad, tile_size_rad))
    
    # Add patches to the plot
    collection = PatchCollection(patches, alpha=0.4, edgecolor='black', facecolor='blue')
    ax.add_collection(collection)

    # Final adjustments and show plot
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-np.pi/2, np.pi/2)
    plt.show()

# Define parameters for the plots
tile_size_arcmin = 5  # in arcminutes
tile_size_deg = tile_size_arcmin / 60  # convert to degrees

# Generate plots for circular and square tiles
generate_tiles('circle', tile_size_deg, projection='mollweide')
generate_tiles('square', tile_size_deg, projection='mollweide')