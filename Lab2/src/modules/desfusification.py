import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz


# Generate trapezoidal membership function on range [0, 1]
x = np.arange(0, 5.05, 0.1)



def desfuzzy(universe,fuzzy_array):
    # Defuzzify this membership function five ways
    defuzz_centroid = fuzz.defuzz(universe, fuzzy_array, 'centroid')  # Same as skfuzzy.centroid
    defuzz_bisector = fuzz.defuzz(universe, fuzzy_array, 'bisector')

    # Collect info for vertical lines
    labels = ['centroid', 'bisector', 'mean of maximum', 'min of maximum',
            'max of maximum']
    xvals = [defuzz_centroid,
            defuzz_bisector]
    colors = ['r', 'b']

    ymax = [fuzz.interp_membership(universe, fuzzy_array, i) for i in xvals]

    # Display and compare defuzzification results against membership function
    plt.figure(figsize=(8, 5))

    plt.plot(universe, fuzzy_array, 'k')
    for xv, y, label, color in zip(xvals, ymax, labels, colors):
        plt.vlines(xv, 0, y, label=label, color=color)
    plt.ylabel('Fuzzy membership')
    plt.xlabel('Universe variable (arb)')
    plt.ylim(-0.1, 1.1)
    plt.legend(loc=2)

    plt.show()