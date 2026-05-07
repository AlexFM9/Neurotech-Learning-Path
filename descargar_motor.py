subject=5
runs=[5,9,13]

rutas_ficheros = mne.datasets.eegbci.load_data(subjects=subject, runs=runs)

for ruta in rutas_ficheros:
    print(ruta)
