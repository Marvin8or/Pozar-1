# Pozar

Bok,
Veličinu domene i rezoluciju mreže prilagodite iskustvenim saznanjima i trajanju simulacije.
Mislim da je 1 km x 1 km razumno. Veličina ćelije 1 m x 1 m.

Pripremite podatke za neko područje (teren, vegetaciju, vjetar) i probajte napraviti simulaciju širenja požara.

Odredite neko proizvoljno opožareno područje.

Tada napravite Python kod (funkciju) koji:
prima koordinate i početak (ili proteklo vrijeme od) izvora požara (x, y, T)
kopira ulazne datoteke simulacije na novu lokaciju
mijenja koordinate izvora u ulaznim datotekama i postavlja trajanje simulacije (T)
izračunajte razliku između simuliranog i pretpostavljenog/mjerenog opožarenog područja: r=np.sum(np.abs(S_sim - S_mj)
U seminaru dajte uvod u model i problem. definirajte optimizacijski problem i dokumentirajte cijeli postupak.

Nadam se da je jasnije.
Ako ima još pitanja - pitajte!
Pozdrav,
Stefan

S Pythonom mjenjate parametre OpenFOAM simulacije požara.
Ali prilagodite si simulaciju (Ulazne datoteke za OpenFOAM) da vam bude pogodna za rješavanje ovog problema (npr. domena ni premala (nedovoljno vremena za simuliranje požara) ni prevelika (spora simulacija)).


Zbog malog broja varijabli i relativno spore evaluacije ja bih preporučio neku MADS metodu. Pogledajte si video lekciju i kako podesiti i pokrenuti optimizaciju pomoću NOAMD-a.
