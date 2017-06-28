#!/usr/bin/env python3.5
""" Verifica e eseguire script """

# Tutto il codice nel modulo/script è eseguito quando viene importato.
# Se vuoi che il tuo programma possa essere usato sia come modulo 
# importabile sia come programma eseguibile, aggiungi alla fine di esso 
# qualcosa come:

def go():

    print("ex_script.py >>> Eseguito direttamente come script")
    # return # non è necessario esplicitarlo

if __name__ == "__main__": go()

# Per NON eseguirlo come script eseguire ex_script_2.py
else: print("ex_script.py >>> Richiamato da altro script")


# NOTA: Questo è un modo magico per dire che se questo modulo viene fatto girare 
# come script eseguibile (cioè, se non stiamo venendo importati da un altri script), 
# allora va chiamata la funzione go. Naturalmente, potresti fare qualsiasi 
# cosa in questa posizione dopo il due-punti... :)