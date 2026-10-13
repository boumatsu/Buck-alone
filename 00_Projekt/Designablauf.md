# Designablauf – Reihenfolge, Abhängigkeiten, was jeder Block braucht

Diese Datei beantwortet drei Fragen: **In welcher Reihenfolge** wird entworfen? **Was hängt wovon ab?** **Was braucht jeder Block** (LTC7800, MOSFETs, alles davor, alles danach)? Die Schrittnummern (A2, B6, C5 …) verweisen auf die Arbeitsanleitungen der Bereiche, Q-Nummern auf `01_Quellen/`. Grenzwerte und Formeln stehen in `00_Projektkontext.md` (§3–§8) mit Datenblattseiten – hier nur die Logik.

---

## 1 Signalfluss (von der Buchse bis zum Ausgang)

```
                        VOR dem Controller                                   Leistungsstufe + Controller                      NACH dem Controller
J401/J402 ─► Verpolschutz ─► Überstrom ─► Surge/Burst-Klemmung ─► EMV-Filter ─► C_IN ─► Q101 (oben) ─► SW ─► L101 ─► R_SENSE ─► C_OUT ─► J403/J404
 (Buchse)       (C4)          (C5)          (C6, C8, C9)          (D4, D5)    (A10)    Q102 (unten) + D102              (A4)    (B5)   (Ausgang)
                                                                                         ▲ TG/BG/BOOST                    │                │
                                                                              LTC7800 U201 + Beschaltung ◄── SENSE± ──────┘   VFB-Teiler ◄─┘
                                                                              (B2–B11: FB, ITH, SS, RUN, FREQ, MODE,          PGOOD → LED (D6)
                                                                               ILIM, INTVCC/EXTVCC, Sense-Filter)             Messpunkte (D7)
```

---

## 2 Reihenfolge und warum

Grundregel: **Erst das festlegen, wovon viele andere Werte abhängen.** Wer mit der Kompensation oder dem Filter anfängt, rechnet später alles neu.

| # | Schritt | Ordner | Braucht vorher | Liefert an |
|---|---|---|---|---|
| 0 | Vorgaben und Grenzen sammeln: V_IN 22–26 V, V_OUT 12 V, I_OUT 3 A, Surge 1 kV, Burst 2 kV, Budget, Bauteilregeln | `00_Projekt/` | Aufgabenstellung | alles |
| 1 | **Schutzkonzept grob** (Variante A/B/C): höchste Spannung am Buck-Eingang | `C01`, `C05` | 0 | FET-Spannungsklasse, Nennspannung C_IN, VIN-Pin, Filter-C |
| 2 | **Schaltfrequenz f** | `A01` | 0, 1 | L, C_IN, C_OUT, Filter, Verluste, R_FREQ |
| 3 | **Spule L101**: L aus Rippelstrom-Ziel, I_SAT, DCR | `A01` | 2 | R_SENSE (I_PK), Kompensation, Kurzschlussstrom |
| 4 | **R_SENSE und ILIM**: Stromgrenze I_LIM, min/typ/max | `A02` | 3 | **Strom-Rating aller Bauteile im Leistungspfad**, Eingangsstrom bei Überlast (an C), R13-Nachweis |
| 5 | **MOSFETs Q101/Q102, Schottky D102** | `A03` | 1, 2, 4 | Verluste, Gate-Ladung (→ INTVCC, Bootstrap) |
| 6 | **Bootstrap** C_B, D_B | `A04` | 5 | – |
| 7 | **C_IN** (Rippelstrom, Nennspannung, DC-Bias) | `A05` | 1, 2, 4 | Filter (D), Hot-Plug (C), Stopper-Stabilität (C) |
| 8 | **C_OUT** (Rippel, Lastsprung, DC-Bias) | `B02` | 2, 3 | Kompensation |
| 9 | **Controller-Beschaltung**: Teiler, MODE, RUN, SS, FREQ, INTVCC/EXTVCC, Sense-Filter, PGOOD | `B01`, `B04`, `B05` | 2, 4, 5 | Kompensation, Schaltplan |
| 10 | **Kompensation** (ITH-Netzwerk), Phasenreserve ≥ 60° | `B03` | 3, 4, 8, 9 | Lastsprung, Stabilität |
| 11 | **Schutz detailliert**: Bauteile dimensionieren, Hot-Plug, Überstrom am Eingang | `C02`–`C06` | 1, 4, 7 | Filter-Lage, Verluste |
| 12 | **EMV-Filter** + Dämpfung, Middlebrook-Prüfung | `D01` | 2, 7, 11 | – |
| 13 | **Gesamtsimulation** LTspice: Anlauf, Lastsprung, Kurzschluss, Bode, Surge, Burst, Hot-Plug, Verpolung | `06_Simulation_Gesamt/` + Themenordner | 2–12 | Nachweise, ggf. Rücksprung zu 3–12 |
| 14 | **Verluste, Thermik, Wirkungsgrad, Budget** | `A06`, `03_Stueckliste/` | 5, 11, 12 | Entscheidung „fertig“ oder Rücksprung |
| 15 | **Stecker, LED, Messpunkte, Stellschrauben** (Bestückungsoptionen) | `D02` | 9, 13 | Schaltplan |
| 16 | **Schaltplan in KiCad**, Symbole/Footprints, Stückliste aus KiCad | `04_Schaltplan_Layout/` | 1–15 | Layout |
| 17 | **Layout-Vorgaben** (Schleifen, Masse, Kelvin, Abstände) → **Layout** → DRC → Fertigungsdaten | `D04`, `04_Schaltplan_Layout/` | 16, Platinenrahmen `D03` | Bestellung |
| 18 | Inbetriebnahme- und Messplan | `05_Dokumentation/` | 17 | – |

**Rücksprünge sind normal.** Typisch: Simulation (13) zeigt zu wenig Phasenreserve → C_OUT (8) oder Kompensation (10) ändern; Verluste (14) zu hoch → f (2) oder FETs (5) ändern; Budget überschritten → Schutzvariante (1) überdenken.

---

## 3 Was braucht der LTC7800 – Pin für Pin

Quelle: Q01 Datenblatt Rev. F, S. 8–9 (Pin Functions), Werte in `00_Projektkontext.md` §4. Gehäuse QFN-20 3 × 4 mm mit Exposed Pad.

| Pin | Name | Was muss dran | Hängt ab von |
|---|---|---|---|
| 17 | VIN | Bypass-Kondensator zu SGND, nah am Pin; max. 60 V Betrieb | Schutzkonzept (1) |
| 14 | INTVCC | ≥ 2,2 µF Keramik zu PGND (+ 1 µF direkt am Pin), für nichts anderes verwenden | Gate-Ladung der FETs (5) |
| 15 | EXTVCC | nie offen, max. 14 V; bei V_OUT = 12 V an V_OUT anschließen (spart Verlust) | V_OUT |
| 12 | BOOST | C_B zu SW, Schottky-Diode von INTVCC nach BOOST | C_ISS des oberen FET (5) |
| 10 / 13 | TG / BG | Gate von Q101 / Q102, kurze Leitungen; Footprint für Gate-Widerstand vorsehen | FETs (5) |
| 11 | SW | Schaltknoten zur Spule, Fläche klein halten (EMV) | Layout |
| 16 | PGND | Source Q102 und Minus von C_IN, Leistungsmasse | Layout |
| 2, 3, 21 | SGND + Exposed Pad | Signalmasse, getrennt geführt, an einem Punkt mit PGND (Minus C_IN); Pad verlöten | Layout |
| 6 / 5 | SENSE+ / SENSE− | Kelvin-Leitungen an R_SENSE, RC-Filter direkt am IC | R_SENSE (4) |
| 18 | ILIM | an SGND, offen oder INTVCC → Stromgrenze | R_SENSE (4) |
| 7 | VFB | Spannungsteiler von V_OUT (0,8 V Referenz) | V_OUT, Widerstände E12 |
| 8 | ITH | Kompensationsnetzwerk (R, C, C) zu SGND | Kompensation (10) |
| 19 | TRACK/SS | Kondensator zu SGND → Soft-Start-Zeit | Einschaltstrom, C_OUT |
| 4 | RUN | Spannungsteiler von V_IN → Einschaltschwelle (Unterspannungsabschaltung) | V_IN-Bereich |
| 20 | FREQ | Widerstand zu SGND → Schaltfrequenz | f (2) |
| 1 | PLLIN/MODE | Betriebsart bei Teillast (Burst / Pulse-Skipping / forced continuous) | B2 |
| 9 | PGOOD | Open-Drain, Pull-up (z. B. 100 kΩ an INTVCC); treibt die Status-LED über einen FET | D6 |

---

## 4 Was brauchen die MOSFETs

| Anforderung | Warum | Woher der Wert |
|---|---|---|
| V_DS ≥ höchste Spannung am Buck-Eingang + Reserve für Überschwinger am SW-Knoten | Durchbruch beim Surge / Hot-Plug / Ringing | Schutzkonzept (1), Layout |
| Logic-Level: R_DS(on) bei **4,5 V** spezifiziert, V_GS(th),max deutlich unter 4,85 V | Gate wird nur mit INTVCC (≈ 5 V) angesteuert | Q01, FET-Datenblatt |
| Dauerstrom und Erwärmung bei **I_LIM,max** (nicht nur bei 3 A) | Überlast ohne Foldback (R13) | R_SENSE/ILIM (4) |
| Oben: kleine Q_GD und C_RSS (Schaltverluste); unten: kleiner R_DS(on) und kleine Q_RR | Oben schaltet hart, unten leitet länger (1 − D) | f (2), D = 0,46–0,55 |
| Gesamte Gate-Ladung Q_G | INTVCC-Strom = Q_G · f; Bootstrap C_B ≥ 100 · C_ISS | f (2) |
| SOA, Avalanche (falls der FET im Surge-Pfad liegt) | Schutz-FETs in C | Schutzkonzept (1) |
| Gehäuse von Hand lötbar, Wärmeableitung über Kupfer | Eigenes Layout, eigene Bestückung | Platine (D03) |
| Bei Bedarf Schottky D102 parallel zum unteren FET | Totzeit-Verluste, Q_RR | A8 |

---

## 5 Was kommt vor dem Controller und was braucht es

Für **jeden** Block vor dem Buck gelten dieselben vier Fragen: **höchste Spannung**, **Dauerstrom** (1,72 A nominal bei 22 V, bis ≈ 3 A bei Überlast – Wert aus Schritt 4), **Pulsenergie/-strom** (Surge 1 kV / 2 Ω ≈ 500 A, Burst), **Verlust im Normalbetrieb**.

| Block | Aufgabe | Braucht |
|---|---|---|
| Buchse J401/J402 | Anschluss Labornetzteil | Strom-Rating, 4-mm-Sperrzone bei THT |
| Verpolschutz (C4) | −26 V darf nichts zerstören | Sperrspannung, Verlust bei 1,72 A, bei FET-Lösung Gate-Zener |
| Überstrom am Eingang (C5) | Kurzschluss im Wandler begrenzen/abschalten | Auslösestrom über max. Eingangsstrom bei I_LIM, I²t gegen Einschaltstrom, Crowbar-Fall des LTC7800 |
| Surge-/Burst-Klemmung (C6, C8) | Überspannung begrenzen | Klemmspannung ≤ Grenze aus Schritt 1, Pulsrating 8/20 µs, bidirektional oder hinter Verpolschutz |
| Hot-Plug (C9) | Überschwingen beim Einstecken (bis ≈ 2 × V_IN) begrenzen | Dämpfungs-Elko oder Einschaltstrombegrenzung |
| EMV-Filter (D4, D5) | Störungen zur Quelle dämpfen | f, C_IN, Dämpfung; Middlebrook: Filter-Ausgangsimpedanz ≪ \|R_IN\| = 12,8 Ω |
| C_IN (A10) | Pulsstrom des Buck liefern | Rippelstrom ≈ 1,5 A_RMS, Nennspannung aus Schritt 1, DC-Bias-Kapazität |

---

## 6 Was kommt nach dem Controller und was braucht es

| Block | Aufgabe | Braucht |
|---|---|---|
| Spule L101 (A5) | Energie speichern, Rippelstrom begrenzen | I_SAT > I_LIM,max, DCR (Verlust), nur Würth |
| R_SENSE (A4) | Strom messen | Leistung bei I_LIM,max, Kelvin-Anschluss, niedrige Induktivität |
| C_OUT (B5) | Rippel und Lastsprung | Kapazität bei 12 V DC-Bias, ESR, Rippelstrom |
| Rückführung VFB (B3) | 12 V einstellen | Teiler E12, Toleranzrechnung, C_FF-Option |
| Ausgangs-Überstromschutz (R13) | Überlast/Kurzschluss | Strombegrenzung + Foldback; Nachweis Dauerlast bei I_LIM,max (`A_Leistungsstufe/README.md`), Frage F7 |
| Buchse J403/J404 | Last anschließen | 3 A Dauer, kurzzeitig I_LIM |
| PGOOD → LED (D6) | Status anzeigen | N-FET mit V_GS(th) ≪ 4,85 V, LED-Strom aus INTVCC oder V_OUT |
| Messpunkte (D7) | Inbetriebnahme | V_IN an Buchse, nach Schutz, Buck-Eingang, SW, V_OUT, ITH, VFB, PGOOD, mehrere GND |

---

## 7 Werkzeuge

- **Simulation: LTspice.** Der LTC7800 und der LTC4364 sind dort als Modell enthalten. Bauteilmodelle aus `02_Modelle/LTspice/` mit relativem Pfad einbinden. Python oder ngspice nur für Hilfsrechnungen (z. B. Parameter-Sweeps), nicht als Nachweis.
- **Schaltplan und PCB: KiCad.** Würth-Bibliotheken in `02_Modelle/KiCad/`. Für den LTC7800 (QFN-20 3 × 4 mm, Exposed Pad) Symbol und Footprint prüfen bzw. selbst anlegen und gegen die Gehäusezeichnung im Datenblatt (Q01) kontrollieren.
- **Gegenprobe (optional):** LTpowerCAD (Q02), Demo-Board DC2736A (Q03) als Plausibilitätscheck – nicht übernehmen.
