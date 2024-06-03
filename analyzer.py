import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets
from IPython.display import display
# Path to the CSV file
file_path = '/home/ubuntu/MoCap/T1_1Act_quarterComp/T1_1act_quarterComp.csv'

# Read the file and find the start of frame data
with open(file_path, 'r') as file:
    lines = file.readlines()

frame_start_index = None
for index, line in enumerate(lines):
    if line.startswith('frame'):
        frame_start_index = index
        break

# Initialize lists for storing average positions and time stamps
average_positions = []
time_stamps = []

# Process each line to extract coordinates and compute averages
for line in lines[frame_start_index:]:
    parts = line.split(',')
    if parts[0] != 'frame':
        continue
    
    # Extract frame time
    frame_time = float(parts[2])
    time_stamps.append(frame_time)
    
    # Extract all x, y, z coordinates for the current frame
    num_points = int(parts[4])
    positions = []
    for i in range(num_points):
        base_index = 5 + i * 5  # Calculate the starting index of x, y, z for each marker
        x = float(parts[base_index])
        y = float(parts[base_index + 1])
        z = float(parts[base_index + 2])
        positions.append((x, y, z))
    
    # Compute the average position for this frame
    if positions:
        average_position = np.mean(positions, axis=0)
        average_positions.append(average_position.tolist())
    else:
        average_positions.append([np.nan, np.nan, np.nan])  # Handle frames with no markers

# Convert results to numpy array for easier handling in plotting
average_positions = np.array(average_positions)
time_stamps = np.array(time_stamps)

# Assuming 'average_positions' and 'time_stamps' are loaded as shown previously
average_positions = np.array(average_positions)  # Make sure this is a numpy array
time_stamps = np.array(time_stamps)

def update_plot(frames_to_show, start_frame):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Calculate the end frame based on the start frame and the number of frames to show
    end_frame = start_frame + frames_to_show
    if end_frame > len(average_positions):
        end_frame = len(average_positions)
        start_frame = end_frame - frames_to_show if end_frame - frames_to_show > 0 else 0
    
    # Update the plot
    ax.scatter(
        average_positions[start_frame:end_frame, 0],
        average_positions[start_frame:end_frame, 1],
        average_positions[start_frame:end_frame, 2],
        c=time_stamps[start_frame:end_frame],
        cmap='viridis'
    )
    
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Z Coordinate')
    ax.set_title('Interactive Plot of Average Marker Positions')
    plt.show()

# Create sliders
frames_to_show_slider = widgets.IntSlider(min=1, max=len(average_positions), step=1, value=50, description='Frames to Show:')
start_frame_slider = widgets.IntSlider(min=0, max=len(average_positions)-1, step=1, value=0, description='Start Frame:')

# Interactive widget
ui = widgets.VBox([
    frames_to_show_slider,
    start_frame_slider
])
out = widgets.interactive_output(update_plot, {'frames_to_show': frames_to_show_slider, 'start_frame': start_frame_slider})

# Display the interactive plot with sliders
display(ui, out)