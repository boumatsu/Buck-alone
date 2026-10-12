# A – Leistungsstufe: Schaltfrequenz, Spule, Strommessung, MOSFETs, Schottky, Bootstrap, C_IN, Verluste

**Stand:** _Datum + ein Satz_

Arbeitsanleitung mit allen Schritten: [`A_Leistungsstufe.md`](A_Leistungsstufe.md).

## Themenordner
| Ordner | Schritte aus der Anleitung | Inhalt |
|---|---|---|
| `A01_Frequenz_Rippel_Spule/` | A2, A3, A5 | Schaltfrequenz, Rippelstrom-Ziel, Spule L101 |
| `A02_Strommessung_Ausgangsschutz/` | A4 | R_SENSE R101, ILIM, Nachweis Überstromschutz am Ausgang (R13) |
| `A03_MOSFETs_Schottky/` | A6, A7, A8 | FET-Spannungsklasse (mit C), Q101/Q102, D102 |
| `A04_Bootstrap/` | A9 | C120, D101, R120 |
| `A05_Eingangskondensatoren/` | A10 | C_IN |
| `A06_Verluste_Thermik/` | A11 | Verlustbilanz und Temperatur |

Übrige Schritte: A1 Vorbereitung → kein Ordner. A12 Stellschrauben → README dieses Bereichs und `D_Filter_Platine/D04_Layout_Vorgaben/`. A13 Simulation → `06_Simulation_Gesamt/` (gemeinsames Buck-Modell). A14 Stückliste → `03_Stueckliste/`.

## Nachweis R13 – Überstromschutz am Ausgang
Anforderung R13 [fest]: Überstromschutz am Ausgang. Lösungsansatz: Strombegrenzung des LTC7800 (R_SENSE, ILIM) mit Foldback, ohne zusätzliches Bauteil. Ob das als Schutz reicht, klärt Frage F7 (`00_Projekt/00_Projektkontext.md` §10). Nachzuweisen in `A02_Strommessung_Ausgangsschutz/`:
| Fall | Was zeigen | Womit |
|---|---|---|
| Dauer-Überlast zwischen 3 A und Stromgrenze (kein Foldback) | Höchster Ausgangsstrom mit **V_SENSE(MAX),max** (nicht typ); Q101, Q102, D102, L101, R101 und Leiterbahnen halten diesen Strom dauerhaft (Verlust, Temperatur, I_SAT) | Rechnung (A4, A11), Simulation mit B |
| Kurzschluss im Betrieb und beim Einschalten | Foldback greift, I_SC = 45 % · I_LIM(MAX) − ½ · ΔI_L(SC); Bauteile halten I_SC dauerhaft; Wiederanlauf nach Wegnahme des Kurzschlusses | Rechnung (A4), Simulation Testfall „Kurzschluss“ (B) |
| Eingangsseite | Eingangsstrom bei Stromgrenze bleibt unter der Auslöseschwelle des Eingangsschutzes (Wert an C) | Rechnung, Abstimmung mit C |
Falls F7 mit „nein“ beantwortet wird: Ausgangs-eFuse oder PTC ergänzen (Verlust, Kosten, Platz) – dann mit D abstimmen.

## Ergebnisse (Stand eintragen, wenn ein Wert feststeht)
| Größe | Wert | Quelle / Datei | Status |
|---|---|---|---|
| | | | |

## Stellschrauben für die Inbetriebnahme
- 

## Offene Punkte
- 
