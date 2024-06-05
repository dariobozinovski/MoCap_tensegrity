# Motion Capture Data Analysis and Visualisation for Jumping Tensegrity Robot
### Jonathan Green and Dario Bozinovski, 2024
//
## Overview
Jumping tensegrity robot developed at the Robotic Systems Lab, ETH Zurich /
Motion capture data recorded at 120fps using an OptiTrack motion capture system /
The data is handled as follows: /
 - Outliers from erroneous reflections during MoCap detected and removed
 - Robot centre of mass estimated from data in every frame
 - Trajectory constructed and passed through smoothing filter
 - Data visualised and videos created

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
