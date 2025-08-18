import string

def conta_righe(testo):
    return len(testo.splitlines())

def pulisci_testo(testo): 
    testo = testo.lower()
    testo = testo.translate(str.maketrans('', '', string.punctuation))
    return testo

def conta_parole(testo):
    nuovo_testo = pulisci_testo(testo)
    if not nuovo_testo:
        return 0
    return len(nuovo_testo.split())

def parole_frequenti(testo, top=5):
    nuovo_testo = pulisci_testo(testo)
    if not nuovo_testo:
        return 0
    serie = pd.Series(nuovo_testo.split())
    return serie.value_counts().head(top)
