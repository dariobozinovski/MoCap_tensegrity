# Motion Capture Data Analysis and Visualisation for Jumping Tensegrity Robot
Jonathan Green and Dario Bozinovski, 2024
\\
## Overview
Jumping tensegrity robot developed at the Robotic Systems Lab, ETH Zurich \
Motion capture data recorded at 120fps using an OptiTrack motion capture system \
The data is handled as follows: \
 - Outliers from erroneous reflections during MoCap detected and removed
 - Robot centre of mass estimated from data in every frame
 - Trajectory constructed and passed through smoothing filter
 - Data visualised and videos created

## Example Outputs
![smoothed_trajectory](https://github.com/dariobozinovski/MoCap_tensegrity/assets/19606313/97a9a22d-5d78-4c6a-ae30-42618aec5448)
![removed_outliers](https://github.com/dariobozinovski/MoCap_tensegrity/assets/19606313/9446f88a-ddd5-44e0-aa4c-93bb8fac8e8b)
![raw_scatterplot](https://github.com/dariobozinovski/MoCap_tensegrity/assets/19606313/5b9525bd-1d2b-4a5a-88f4-829a269afaa5)
![mocap_closeup](https://github.com/dariobozinovski/MoCap_tensegrity/assets/19606313/ddf19dff-739d-4985-8095-baa73bc0d1d3)
https://github.com/dariobozinovski/MoCap_tensegrity/assets/19606313/4eecb2e2-73e4-42d2-95c1-83209a31868d

## Dependancies
 - OpenCV
 - Pandas
 - Numpy
 - Matplotlib
 - Ipywidgets
 - Plotly
 - IPython
 - scikit-learn
 - Scipy
 - Moviepy
