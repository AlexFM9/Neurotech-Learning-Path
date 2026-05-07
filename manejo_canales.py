rutas = mne.datasets.eegbci.load_data(subjects=5, runs=[5])
mi_ruta = rutas[0]

raw_movimiento = mne.io.read_raw_edf(mi_ruta, preload=True)

nombres_canales = raw_movimiento.info['ch_names']

if any(canal.startswith("Cz") for canal in nombres_canales):
    print("El canal Cz (o variaciones con puntos) está presente en el registro.")
    canales_que_empiezan_por_Cz = [canal for canal in nombres_canales if canal.startswith("Cz")]
    print("Exactamente se llama así:", canales_que_empiezan_por_Cz)
else:
    print("El canal Cz NO está presente en el registro.")
