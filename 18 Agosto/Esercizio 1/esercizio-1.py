def conta_righe(testo):
    return len(testo.splitlines())

def pulisci_testo(testo): 
    testo = testo.lower()
    testo = pd.Series([testo]).str.replace(r'[^\w\s]', ' ', regex=True).iloc[0]
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

def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            testo = f.read()
    except FileNotFoundError:
        print('Errore: file input.txt non trovato. Verifica il percorso e riprova.')
        return
        
    print('Totale righe:', conta_righe(testo))
    print('Totale parole:', conta_parole(testo))
    print('Top-5 parole più frequenti:')
    top = parole_frequenti(testo, top=5)
    if top.empty:
        print('(nessuna parola trovata)')
    else:
        for parola, cnt in top.items():
            print(f'{parola}: {int(cnt)}')

if __name__ == '__main__':
    main()