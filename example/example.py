import h5py
import numpy as np

from bragg_detect import detect_bragg_peaks, plot_peaks_over_data

if __name__ == '__main__':
    # read data
    print(f'Data file: data.hdf5')
    with h5py.File(f'data.hdf5', 'r') as file:
        data = file[list(file.keys())[0]][:]

    # detect
    peaks = detect_bragg_peaks(data, large_peak_size=[10, 10, 50],
                               threshold=.2, workers=1)

    # save peak locations
    np.savetxt(f'result/peak_locations.txt', peaks, fmt='%d')

    # plot image without peaks
    plot_peaks_over_data(data, plot_size=(2000, 1000, 3000),
                         vmax=(.5, 0.05, 0.05),
                         peak_sets=[], axis_on=True,
                         save_to_file=f'result/input_image.png')

    # plot image with peaks
    plot_peaks_over_data(data, plot_size=(2000, 1000, 3000),
                         vmax=(.5, 0.05, 0.05),
                         peak_sets=[(peaks, 'w', 'o', 3, 0)], axis_on=True,
                         save_to_file=f'result/peaks_on_image.png')
