# Arbeitsstand

**Zuletzt aktualisiert:** 2026-10-13

Jede KI-Sitzung trägt sich **vor Beginn** unter „In Arbeit“ ein und schreibt **am Ende** eine Übergabe. So arbeiten zwei KIs nicht an derselben Stelle und die nächste Sitzung weiß, wo es weitergeht.

## In Arbeit
| KI / Sitzung | Ordner | seit | Ziel |
|---|---|---|---|
| – | – | – | – |

## Nächste Schritte (Vorschlag, Reihenfolge nach `00_Projekt/Designablauf.md` §2)
1. **C05 Variantenvergleich:** Schutzvariante A (passiv), B (Surge-Stopper) oder C (eFuse) festlegen. Davon hängen ab: L1 (Surge-Längsglied), Nennspannung der Elkos (35 V nur mit Stopper), FET-Spannungsklasse in A03. Siehe Prüfvermerk in `03_Stueckliste/02_Bauteilkandidaten.md` (D5).
2. **A01/A02:** Schaltfrequenz, Spule, R_SENSE/ILIM festlegen; Nachweis R13 (Ausgangs-Überstrom) nach `A_Leistungsstufe/README.md`.
3. **D01 Eingangsfilter:** L401/C_F nach gewählter Schutzvariante, Dämpfung und Middlebrook prüfen.
4. **B03 Kompensation** auf dem gemeinsamen Buck-Modell (`06_Simulation_Gesamt/`).
5. Fragen F1–F7 an den Prof (`00_Projekt/00_Projektkontext.md` §10).

## Übergaben (neueste oben)
### 2026-10-13 – Designablauf und Werkzeuge
- Neu: `00_Projekt/Designablauf.md` (Reihenfolge 0–18 mit Abhängigkeiten; Pin-Tabelle LTC7800 nach Q01 S. 8–9; Anforderungen MOSFETs; Blöcke vor und nach dem Controller).
- Designablauf gegliedert in Kern (LTC7800 + Spule, R_SENSE, C_IN, C_OUT, Rückführung, Kompensation – wird zuerst ausgelegt), Eingangsseite und Ausgangsseite.
- `AGENTS.md`: Designablauf als Pflichtlektüre, Abschnitt 6 Werkzeuge (LTspice für Simulation, KiCad für Schaltplan/PCB).
### 2026-10-12 – Repo angelegt
- Struktur, Quellen Q01–Q72, Modelle, Bauteilkandidaten, Material der früheren KI mit Präfix `altKI_`.
- Geprüft: Filterdrossel 22 µH vs. 2,2/3,3 µH und Elko 35 V vs. 50 V → Prüfvermerk in `03_Stueckliste/02_Bauteilkandidaten.md`. Entscheidung offen (hängt an C05).
- LTspice-Dateien `altKI_*.cir`: Modellpfade auf relativ umgestellt, in LTspice noch **nicht** getestet.
