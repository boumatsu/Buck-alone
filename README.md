# LTC7800-Buck – persönliches Arbeits-Repo

Nicht isolierter DC/DC-Wandler (Buck) mit dem LTC7800: **22…26 V → 12 V / 3 A**, mit Eingangsschutz (Verpolung, Überstrom, Surge 1 kV, Burst 2 kV), Ausgangs-Überstromschutz und EMV-Filter. Budget 100 € netto. Details: [`00_Projekt/00_Projektkontext.md`](00_Projekt/00_Projektkontext.md).

Dieses Repo ist mein eigener Arbeitsstand: Ich bearbeite hier das ganze Projekt allein bzw. mit Hilfe von ein bis zwei KI-Assistenten – unabhängig vom Gruppen-Repo [boumatsu/LTC7800-Buck](https://github.com/boumatsu/LTC7800-Buck). Einzelne Ergebnisse gebe ich nur dann an die Gruppe weiter, wenn es passt; eine Pflicht zum Abgleich gibt es nicht.

## Einstieg
- **Aktueller Stand, was gerade läuft, nächste Schritte:** [`STATUS.md`](STATUS.md)
- **Regeln für KIs (und für mich):** [`AGENTS.md`](AGENTS.md)
- **Reihenfolge des Entwurfs, was jeder Block braucht:** [`00_Projekt/Designablauf.md`](00_Projekt/Designablauf.md)
- **Werkzeuge:** LTspice (Simulation), KiCad (Schaltplan, PCB)

## Ordner
```
00_Projekt/            Projektkontext, Aufgabenstellung, Entscheidungen (§9), offene Fragen (§10)
01_Quellen/            Quellenliste + PDFs (Q01…Q72)
02_Modelle/            LTspice-/KiCad-Modelle, ADI-Referenzschaltungen
03_Stueckliste/        gemeinsame Stückliste, Bauteilkandidaten, Budget
04_Schaltplan_Layout/  KiCad-Projekt
05_Dokumentation/      Bericht, Bilder, Messungen
06_Simulation_Gesamt/  gemeinsames Buck-Modell, Gesamtkette
A_ … D_/               je Bereich: README (Stand, Ergebnisse), Arbeitsanleitung, Themenordner
```

Dateien mit Präfix `altKI_` stammen aus einer früheren KI-Sitzung und sind **ungeprüft** – nur zum Gegenprüfen eigener Ergebnisse.
