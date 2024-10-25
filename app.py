import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add title for the page
ui.page_opts(title="Mee's App with Plot",fillable=True)

with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20, step=1)
    # A string id("selected_number_of_bins") that uniquely identifies this input value
    # A string label (e.g., "Number of Bins") to be displayed alongside the slider.
    # An integer representing the minimum number of bins (e.g., 0).
    # An integer representing the maximum number of bins (e.g., 100).
    # An integer representing the initial value of the slider (e.g., 20).

@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), density=True)
