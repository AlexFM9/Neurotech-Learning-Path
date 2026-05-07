rutas = mne.datasets.eegbci.load_data(subjects=5, runs=[5])
raw = mne.io.read_raw_edf(rutas[0], preload=True)

# Renombra los canales usando una expresion lambda y .strip('.')
mne.rename_channels(raw.info, lambda name: name.strip('.'))

# Imprime si "Cz" está ahora en las info de los canales para corroborarlo! :-D
if "Cz" in raw.info['ch_names']:
    print("El canal Cz está presente en el registro (¡Ahora está limpio!).")
else:
    print("El canal Cz NO está presente en el registro.")

# Recorta el dataset dejando exclusivamente 'C3', 'Cz', y 'C4'
raw.pick(['C3', 'Cz', 'C4'])

# Plotea interactivamente lo que ha quedado
raw.plot(n_channels=3, duration=5.0, scalings={'eeg': 50e-6}, block=True)
