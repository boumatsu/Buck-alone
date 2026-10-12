# Bereich A – Leistungsstufe

Für Person A und ihre KI. Vorher `00_Projektkontext.md` lesen (Regeln, Prioritäten §1a, LTC7800-Daten, Randwerte, Schnittstellen). Quellen-Kürzel Q.. siehe `01_Quellen_ApplicationNotes.md`.

## Auftrag
Die Leistungsstufe des Buck auslegen und alle ihre Bauteile festlegen: Schaltfrequenz, Spule, beide MOSFETs, Strommessung, Bootstrap, Eingangs-Keramikkondensatoren. Nach 00 §1a: **zuerst sicher funktionierend** (Reserven bei Spannung, Strom, Temperatur, auch mit unserem selbst gemachten Layout), dann unter den sicheren Lösungen die mit den kleinsten Verlusten. Alle Teile lieferbar.

## Bauteile von A
| Ref | Funktion | LTC7800-Pin |
|---|---|---|
| Q101 | oberer N-MOSFET (Main) | TG 10, SW 11 |
| Q102 | unterer N-MOSFET (Sync) | BG 13, PGND 16 |
| D102 | Schottky parallel zu Q102 (optional) | – |
| L101 | Speicherdrossel (Würth) | zwischen SW und R_SENSE/V_OUT |
| R101 | Strommesswiderstand, oder DCR-Netzwerk R102/R103/C103 | SENSE+ 6 / SENSE− 5 (Filter am IC: B) |
| C101…C10x | C_IN, Keramik zwischen Q101-Drain und Q102-Source | – |
| C110 | kleiner HF-Keramikkondensator direkt in der Schaltschleife (optional, EMV) | – |
| C120, D101, R120 | Bootstrap-Kondensator, -Diode, optionaler Widerstand in Reihe | BOOST 12, SW 11, INTVCC 14 |
| R121, R122 | Gate-Widerstände TG/BG (Bestückungsoption, zunächst 0 Ω) | TG 10, BG 13 |
| R123, C123 | RC-Snubber SW → PGND (Bestückungsoption) | – |

## Wichtigste Quellen für A
| Quelle | Wofür |
|---|---|
| Q01 LTC7800-Datenblatt S. 14–26 | alle Formeln, Grenzen, Referenzschaltungen |
| Q02 LTpowerCAD mit LTC7800-Projekt | Gegenprobe: Bauteilvorschläge, Verluste, Wirkungsgrad |
| Q03 DC2736A (12 V, 500 kHz) / Q04 DC2786A | reale Stücklisten und Layouts zum Vergleichen |
| Q36 REDEXPERT, Q32 ANP031 | Spulenverluste (AC + DC), Erwärmung |
| Q10 ADI Current Sensing Part 3 | R_SENSE gegen DCR-Messung |
| Q40 Vishay AN836, Q41 Vishay AN605, Q42 Nexperia AN11158 | FET-Auswahl im Synchron-Buck, Gütezahl, Datenblatt lesen |
| Q23 TI SLUA887 | Bootstrap-Kondensator, -Diode, -Widerstand |
| Q33 Würth ANP062, Q45 Murata SimSurfing | DC-Bias der Keramikkondensatoren |
| Q08 AN-88 | Hot-Plug mit reinem Keramik-C_IN |
| Q05 AN-136, Q22 TI SLYT682 | kleine Schaltschleife, Überschwinger am SW-Knoten |

## Reihenfolge
```
A1 Vorbereitung → A2 Frequenz (vorläufig) → A3 Rippel und L-Wert → A4 Strommessung → A5 Spule
                                            A6 FET-Spannungsklasse (mit C) → A7 MOSFETs → A8 Schottky → A9 Bootstrap
A10 C_IN → A11 Verluste/Temperatur ──(Frequenz oder FETs neu wählen?)──► zurück zu A2/A7
A12 Stellschrauben → A13 Simulation → A14 Stückliste und Übergabe
```
A2 bleibt vorläufig, bis echte FET- und Spulendaten (A5, A7) vorliegen; dann einmal zurück zu A2 und entscheiden.

---

## A1 Vorbereitung
- Datenblatt Q01 lesen: S. 14–23 (Strommessung, Spule, FETs, C_IN/C_OUT, Verluste), S. 24–25 (Rechenbeispiel), S. 25–27 (Layout-Checkliste, Fig. 9/10), Kurven S. 5–8, Referenzschaltungen Fig. 12, 13, 15, 16.
- LTpowerCAD installieren und das LTC7800-Projekt (Q02) öffnen; auf unsere Daten umstellen (22–26 V, 12 V, 3 A). Nur als Gegenprobe, Rechnung selbst machen.
- REDEXPERT-Zugang (Q36) testen.

## A2 Schaltfrequenz
**Ziel:** Frequenzband festlegen, das Verluste, Spulengröße und Regelbandbreite gut ausbalanciert.

**Optionen** (nur bestimmte Werte mit E12-R_FREQ; interpoliert aus Tabelle S. 4 und Fig. 13–15, mit Fig. 8 prüfen; Toleranz ±15 %):

| Option | Vorteile | Nachteile | Wann |
|---|---|---|---|
| ≈ 370 kHz (27 kΩ) | kleinste Schalt-, Gate- und Q_RR-Verluste; Layout-Parasitics wirken weniger; EMV-Grenzwert bei 370 kHz etwas höher | größte Spule (≈ 19 µH bei 30 % Rippel), Regelbandbreite höchstens ≈ 37 kHz | Wirkungsgrad wichtig, Platz da (keine Höhenbegrenzung) |
| ≈ 510 kHz (33 kΩ) | Mittelweg; Referenzboard DC2736A läuft bei 500 kHz mit 12 V Ausgang | ≈ 110 mW mehr frequenzabhängige Verluste als bei 370 kHz (Beispiel unten) | wenn die Spule bei 370 kHz zu groß oder teuer ist |
| ≈ 635 kHz (39 kΩ) | kleinere Spule und Kondensatoren | noch mehr Verluste | nur bei Platzproblemen |
| ≥ 1 MHz (Fig. 16: 2,1 MHz) | sehr klein | deutlich mehr Schaltverluste | nicht für Gruppe 3 |

**Rechnung je Kandidat:**
1. L für ΔI_L = 0,3 · I_OUT = 0,9 A bei V_IN,max = 26 V: L = V_OUT · (1 − V_OUT/V_IN,max) / (f · ΔI_L) = 6,46 V / (f · 0,9 A).
2. Übergangsverlust Q101 (S. 23): P_TR = 1,7 · V_IN² · I_OUT · C_RSS · f.
3. Gate-Ladung (EXTVCC = V_OUT): P_GATE = f · (Q_G,101 + Q_G,102) · V_EXTVCC.
4. Ausgangskapazitäten (Näherung): P_COSS ≈ ½ · (Q_OSS,101 + Q_OSS,102) · V_IN · f.
5. Totzeit: P_DT ≈ V_F · I_OUT · 2 · t_DT · f, t_DT ≈ 20 ns (S. 3).
6. Sperrverzögerung Body-Diode Q102 (ohne D102): P_RR ≈ Q_RR · V_IN · f.
7. Spulenverluste aus REDEXPERT.

**Größenordnung mit Beispielwerten** (26 V, 3 A; C_RSS = 16 pF aus dem Datenblatt-Beispiel S. 25; angenommen Q_G,ges = 20 nC, Q_RR = 15 nC, V_F = 0,8 V – durch echte FET-Daten ersetzen):

| R_FREQ | f | L (0,9 A) | P_TR | P_GATE | P_RR | P_DT |
|---|---|---|---|---|---|---|
| 27 kΩ | ≈ 370 kHz | 19,4 µH | 20 mW | 89 mW | 145 mW | 36 mW |
| 33 kΩ | ≈ 510 kHz | 14,1 µH | 28 mW | 123 mW | 199 mW | 49 mW |
| 39 kΩ | ≈ 635 kHz | 11,3 µH | 35 mW | 153 mW | 248 mW | 61 mW |

- Mindest-Einschaltzeit (S. 22): t_ON = D_min / f_max = 0,462 / (1,15 · f) ≫ 45 ns – unkritisch, dokumentieren.
- **Ergebnis:** vorläufiges f-Band an B und D; endgültig nach A11.

## A3 Rippelstrom-Ziel und Induktivitätswert
**Optionen:**

| ΔI_L / I_OUT | Vorteile | Nachteile |
|---|---|---|
| ≈ 20 % | kleiner Ausgangsrippel, kleiner Kernverlust | große L → mehr DCR und Größe, langsamere Stromänderung beim Lastsprung |
| ≈ 30 % (Startwert S. 16) | Kompromiss | – |
| ≈ 40–50 % | kleine L, schnelle Dynamik; t_ON(min) ist für ≥ 40 % Rippel spezifiziert (Note 7) | höhere Effektivströme (Leitverluste, C_IN/C_OUT-Belastung), mehr Kernverlust und Rippel |

**Rechnung:**
- L = 6,46 V / (f · ΔI_L) bei 26 V.
- Worst Case: f_min (−15 %) und L_min (Toleranz und Abfall bei 3 A, meist −20 %) erhöhen ΔI_L. Das ΔI_L,max geht in A4, A5 und B (C_OUT) ein.
- I_RMS² = I_OUT² + ΔI_L²/12 (für alle Leitverluste).

## A4 Strommessung und ILIM
**Formel (S. 15):** R_SENSE = V_SENSE(MAX),min / (I_MAX + ΔI_L/2), mit dem **Minimalwert** der Schwelle. I_MAX mit Reserve (Vorschlag 3,5 A), dazu die Kurve „Maximum Current Sense Threshold vs Duty Cycle" (S. 5–8) bei D = 0,545 prüfen.

**Optionen** (I_MAX = 3,5 A, ΔI_L = 0,9 A → Nenner 3,95 A; R_SENSE = nächstkleinerer Normwert; Verlust bei 3 A mit I_RMS² = 9,07 A²):

| Option | R_SENSE | Verlust | Grenze Spitzenstrom | Vorteile | Nachteile |
|---|---|---|---|---|---|
| R_SENSE, ILIM = GND (22/36 mV) | 5 mΩ | 45 mW | 4,4…7,2 A | kleinster Verlust | kleinstes Signal (störempfindlich), breiteste Grenze |
| **R_SENSE, ILIM = INTVCC (43/57 mV) – Empfehlung** | 10 mΩ | 91 mW | 4,3…5,7 A | doppeltes Signal, enge Grenze → Spule, FETs, Eingangsschutz entlastet | ≈ 45 mW mehr (nach 00 §1a gleichwertig) |
| R_SENSE, ILIM offen (64/85 mV) | 15 mΩ | 136 mW | 4,3…5,7 A | größtes Signal | höchster Verlust |
| DCR-Messung (S. 15–16, Fig. 14) | – | ≈ 0 + R1-Verlust | stark temperaturabhängig | kein Shunt | DCR-Toleranz und +0,4 %/K → ungenaue Begrenzung; Abgleich R1/R2/C1 |

- Höchster Strom: I_PK,max = V_SENSE(MAX),max / R_SENSE,min (z. B. 57 mV / 10 mΩ = 5,7 A, R-Toleranz einrechnen) → an A5, A7, C, D.
- Kurzschluss (S. 21): I_SC = 45 % · I_LIM(MAX) − ½ · t_ON(min) · V_IN / L; Verlust Q102: I_SC² · (1 + δ) · R_DS(on).
- **Bauteilgruppen R_SENSE:** Metallstreifen-/Metallfolien-Shunts 1206/2010/2512, 1 %, TK ≤ 100 ppm/K, Leistung ≥ 2 × Verlust; bevorzugt 4-polig oder mit Kelvin-Pads. Suchbeispiele: Vishay WSL/WSK, Bourns CSS/CSS2H, Susumu KRL. Kein E12 nötig.
- Quellen: Q01 S. 14–16, 21; Q10.

## A5 Spule L101 (nur Würth)
**Anforderungen:** L aus A3 bei 3 A Gleichstrom; I_SAT > I_PK,max aus A4 mit Reserve; I_R ≥ 3 A mit Reserve (Würth gibt I_R meist für 40 K Erwärmung an); DCR klein; Kernverlust bei f klein; geschirmt (EMV); 2 Händler.

**Optionen nach Bauart** (Bauart, Kernmaterial und Sättigungsverhalten immer im Datenblatt prüfen):

| Bauart | Vorteile | Nachteile |
|---|---|---|
| geformte Metallpulver-/Composite-Spule | weiche Sättigung (Induktivität fällt langsam ab), gut geschirmt, kompakt, kleine DCR | Kernverluste bei großem ΔI und hoher f oft höher |
| geschirmte Ferritspule | kleine Kernverluste | sättigt hart (S. 16: „Do not allow the core to saturate!") → mehr I_SAT-Reserve |
| Flachdraht-Hochstromspule | sehr kleine DCR | groß und teuer, für 3 A meist überdimensioniert |

- **Würth-Familien zum Durchsuchen:** WE-XHMI, WE-LHMI, WE-MAPI (eher klein), WE-PD, WE-HCI, WE-HCF.
- **Auswahl mit REDEXPERT** (Q36, Verlustmodell Q32): 3–4 Kandidaten bei V_IN 22/24/26 V, V_OUT 12 V, 3 A, f aus A2 vergleichen.
- **Rechnung:** P_DCR = I_RMS² · DCR(T), DCR(T) = DCR_20 °C · (1 + 0,004/K · (T − 20 °C)) (S. 15); P_Kern aus REDEXPERT.
- **Kandidatentabelle:** L bei 3 A, DCR max, I_SAT, I_R, P_DCR, P_Kern, Erwärmung, Maße, Preis, Händler 1/2.
- **Tipp EMV:** Ist der Wickelanfang markiert (Punkt), diesen an den SW-Knoten legen. Dann liegt die äußere Lage auf dem ruhigen Ausgangspotential und schirmt ab.

## A6 FET-Spannungsklasse (zusammen mit C)
| Klasse | Vorteile | Nachteile | Voraussetzung |
|---|---|---|---|
| 40 V | kleinere Schalt- und Leitverluste je Gehäusegröße; Fig. 12 nutzt 40-V-FETs bis 38 V Eingang | wenig Reserve: Klemmung, Hot-Plug und SW-Überschwinger müssen unter ≈ 32 V bleiben | aktiver Schutz (Surge-Stopper/eFuse mit Klemme) von C |
| **60 V** | viel Reserve für eigenes Layout, Hot-Plug (≈ 52 V) und TVS-Klemmung; einfacherer Schutz möglich; Fig. 13 nutzt 60-V-FETs bis 58 V | etwas mehr Verluste (berechnen) | – |
| 80–100 V | – | unnötig: LTC7800 ist ohnehin auf 60 V begrenzt, mehr Verluste | – |

Bei Zweifel die 60-V-Klasse (00 §1a). Mehrverlust gegenüber 40 V berechnen und nach der Entscheidungsregel abwägen.

## A7 MOSFETs Q101 und Q102
**Anforderungen:** N-Kanal, Logic-Level (Gate = INTVCC 4,85…5,35 V → R_DS(on) bei V_GS = 4,5 V spezifiziert), V_DS-Klasse aus A6, lötbar, guter R_thJC, 2 Händler.

**Optionen Aufbau:**

| Option | Vorteile | Nachteile |
|---|---|---|
| gleicher Typ für Q101 und Q102 | einfach, eine Bestellposition | nicht für beide Aufgaben optimal |
| verschiedene Typen (Q101 auf kleines Q_GD/C_RSS, Q102 auf kleines R_DS(on)/Q_RR) | jeweils optimal (S. 17) | zwei Positionen |
| Q102 mit integrierter Schottky (z. B. Infineon „…NSI", Fig. 11: BSZ0503NSI) | spart D102, wirkt besser als eine externe Diode | kleinere Auswahl, etwas mehr Leckstrom |
| Dual-N-MOSFET (Halbbrücke in einem Gehäuse) | sehr kleine Schaltschleife, einfacheres Layout | kleinere Auswahl, gemeinsame Wärme |

**Optionen Gehäuse:**

| Gehäuse | Vorteile | Nachteile |
|---|---|---|
| 3,3 × 3,3 mm (TSDSON-8, PowerPAK 1212-8, LFPAK33, WSON) | klein, kurze Schleife | weniger Wärmeabfuhr |
| 5 × 6 mm (SuperSO8, PowerPAK SO-8, SO-8FL, LFPAK56) | bessere Wärmeabfuhr, große Auswahl | etwas größere Schleife |
| LFPAK (sichtbare Anschlussbeinchen) | Lötstellen sichtbar und von Hand nacharbeitbar | etwas größer |

**FET-Familien zum Durchsuchen** (40/60 V, Logic-Level): Infineon OptiMOS (BSZ…, BSC…), onsemi (NTTFS…, NTMFS…), Nexperia (PSMN…, LFPAK), Toshiba U-MOS (TPN…, TPH…), Vishay TrenchFET (SiS…, SiR…), TI NexFET (CSD18…), Diodes Inc. (DMT…, DMTH…).

**Rechnung (S. 17):**
- P_MAIN = (V_OUT/V_IN) · I_RMS² · (1 + δ) · R_DS(on) + V_IN² · (I_MAX/2) · R_DR · C_MILLER · [1/(V_INTVCC − V_TH,min) + 1/V_TH,min] · f
- P_SYNC = ((V_IN − V_OUT)/V_IN) · I_RMS² · (1 + δ) · R_DS(on)
- δ ≈ 0,005/K, R_DR ≈ 2 Ω; C_MILLER = Breite des flachen Bereichs der Gate-Ladungskurve (≈ Q_GD) / V_DS der Kurve · (V_IN / V_DS der Kurve).
- Dazu P_COSS, P_DT, P_RR aus A2.
- **Hinweis S. 17:** Über 20 V Eingang dominieren die Übergangsverluste → für Q101 zählt C_MILLER oft mehr als R_DS(on).

**Kandidatentabelle:** R_DS(on) bei 4,5 V (25/100 °C), Q_G bei 5 V, Q_GD, C_RSS, Q_OSS, Q_RR, V_GS(th), R_thJC, Gehäuse, Preis, Händler 1/2, Verlustsumme bei 22/24/26 V.

**Prüfungen:**
- INTVCC-Strom f · (Q_G,101 + Q_G,102) ≤ 50 mA (S. 20).
- LTC7800 beim Anlauf (VIN-LDO aktiv): T_J = T_A + V_IN · I_INTVCC · 52 K/W, z. B. 26 V · 10 mA → +13,5 K.
- FET-Temperatur mit R_thJA bei angenommener Kupferfläche (an D melden).

Quellen: Q01 S. 17, Q40, Q41, Q42.

## A8 Schottky D102 parallel zu Q102
| Option | Vorteile | Nachteile |
|---|---|---|
| ohne | kein Bauteil | Body-Diode leitet in der Totzeit: P_DT + P_RR (Beispiel A2: ≈ 150–200 mW) |
| diskrete Schottky (1–3 A, Sperrspannung ≥ FET-Klasse) | laut Datenblatt bis zu 3 % besser bei hoher V_IN (S. 17) | zusätzliche Kapazität; Leitungsinduktivität begrenzt die Wirkung; braucht Platz in der Schleife |
| FET mit integrierter Schottky (A7) | beste Wirkung | Auswahl begrenzt |

- **Bauteilgruppen:** Leistungs-Schottky in SOD-123F, SMA, PowerDI, z. B. Nexperia PMEG, Diodes Inc. PDS/DFLS (Fig. 15: DFLS2100), Vishay SS-Serie, onsemi MBRS.
- Entscheidung mit Rechnung (mit/ohne) und Simulation A13. Footprint in jedem Fall vorsehen (A12).

## A9 Bootstrap C120, D101, R120
| Teil | Optionen | Abwägung |
|---|---|---|
| C_B | 0,1 / 0,22 / 0,47 µF X7R, 25–50 V, ≥ 0603 | Regel C_B ≥ 100 · C_ISS(Q101) (S. 21); deutlich größer bringt keinen Vorteil |
| D_B | Kleinsignal-Schottky (z. B. BAT46, BAT41 – Datenblatt prüfen) oder Si-Schaltdiode (z. B. 1N4148W) | Schottky: kleines V_F → höhere Gate-Spannung, aber mehr Leckstrom bei Wärme; Si: wenig Leckstrom, ≈ 0,7 V weniger Gate-Spannung. Sperrspannung immer > V_IN,max inkl. Klemmung von C (S. 21) |
| R_BOOT | 0 Ω (Platzhalter) oder einige Ω | verlangsamt das Einschalten von Q101, dämpft Überschwinger am SW-Knoten; kostet Schaltverlust |

Prüfen: BOOST − SW ≤ 6 V absolut (S. 2) mit INTVCC,max = 5,35 V. Quellen: Q01 S. 21, Q23.

## A10 Eingangskondensatoren C_IN
**Rechnung:**
- Rippelstrom I_RMS ≈ 1,5 A im ganzen Eingangsbereich (00 §5) → auf mehrere Kondensatoren aufteilen, Strombelastbarkeit/Erwärmung je Teil aus dem Herstellertool.
- Eingangsrippel ΔV_IN ≈ I_OUT · D · (1 − D) / (f · C_IN,eff); Ziel festlegen und begründen.
- Richtwert S. 23: 25 W brauchen 20–40 µF mit ESR ≤ 20–50 mΩ → auf 36 W linear hochgerechnet ≈ 29–58 µF.
- Effektive Kapazität aus der **DC-Bias-Kurve** des konkreten Teils (Q33: bis zu 80 % Verlust möglich; Q45, Q36).
- Nennspannung aus der höchsten Spannung am Buck-Eingang (C) mit Reserve: bei 40-V-Konzept meist 50 V, bei 60-V-Konzept 100 V.

**Optionen:**

| Option | Vorteile | Nachteile |
|---|---|---|
| nur Keramik X7R (1206/1210) | sehr kleine ESR/ESL, klein, langlebig | DC-Bias; ungedämpft → Hot-Plug-Überschwingen (Q08) und Filterresonanz |
| Keramik + Elko/Polymer (Dämpfung, mit D abstimmen) | dämpft Hot-Plug und Filterresonanz | größer; Elko-Lebensdauer temperaturabhängig |

- **Bauteilgruppen:** X7R-MLCC 50/100 V, z. B. Murata GRM/GCM, TDK C/CGA, Würth WCAP-CSGP, Samsung CL, KEMET; Dämpfung: Alu-Elko SMD (z. B. Würth WCAP-ASLI) oder Alu-Polymer/Hybrid.
- Optional C110: ≈ 100 nF direkt zwischen Q101-Drain und Q102-Source (schnelle Stromanteile, EMV, Q22).

## A11 Verlustbilanz und Temperatur
| Verlust | Formel | 22 V | 24 V | 26 V |
|---|---|---|---|---|
| Q101 Leitung | (V_OUT/V_IN) · I_RMS² · (1 + δ) · R_DS(on) | | | |
| Q101 Übergang | S. 17 bzw. S. 23 | | | |
| Q102 Leitung | ((V_IN − V_OUT)/V_IN) · I_RMS² · (1 + δ) · R_DS(on) | | | |
| Gate-Ladung | f · (Q_G,101 + Q_G,102) · V_EXTVCC | | | |
| Ausgangskapazitäten | ½ · (Q_OSS,101 + Q_OSS,102) · V_IN · f | | | |
| Totzeit | V_F · I_OUT · 2 · t_DT · f | | | |
| Sperrverzögerung | Q_RR · V_IN · f (mit D102 weitgehend weg) | | | |
| L101 Kupfer | I_RMS² · DCR(T) | | | |
| L101 Kern | REDEXPERT | | | |
| R101 | I_RMS² · R_SENSE | | | |
| C_IN-ESR | I_CIN,RMS² · ESR_ges | | | |
| **Summe A** | | | | |

- Zusätzlich 0,3 A und 1,5 A (Betriebsart von B beachten).
- Gegenprobe mit LTpowerCAD (Q02).
- Temperaturen: T_J = T_A + P · R_thJA für Q101/Q102; Erwärmung L101 (REDEXPERT); R101. Benötigte Kupferfläche und thermische Vias an D melden.
- **Entscheidung:** Dominieren frequenzabhängige Verluste → zurück zu A2 (niedrigere f). Dominieren Leitverluste → zurück zu A5/A7.

## A12 Stellschrauben für die Inbetriebnahme (Footprints, bei Bedarf bestücken)
- **RC-Snubber R123/C123** vom SW-Knoten nach PGND, erst am Board dimensioniert: Klingelfrequenz f_0 messen; Zusatz-C C_add erhöhen, bis sich die Frequenz halbiert → C_par = C_add / 3; L_par = 1 / ((2π · f_0)² · C_par); R_S ≈ √(L_par / C_par), C_S ≈ 3–4 × C_par.
- **R_BOOT R120** (zunächst 0 Ω), **Gate-Widerstände R121/R122** (zunächst 0 Ω).
- Footprint für **D102**; Platz für **zusätzliche C_IN**.
- **Messpunkt am SW-Knoten** mit kurzer Masse (an D melden).

## A13 Simulation (LTspice, gemeinsames Buck-Modell von B)
- Zweck: Funktion, Ströme, Temperaturen und Reserven nachweisen. Der simulierte Wirkungsgrad ist eine Obergrenze (Layout fehlt) – nicht um einzelne mW feilen.
- LTpowerCAD kann ein LTspice-Modell exportieren (Q02) – als Startpunkt nutzbar.
- Modelle: LTC7800 aus der LTspice-Bibliothek; FET-Modelle vom Hersteller (prüfen, ob sie in LTspice laufen); Würth-Spulenmodell; Keramik mit ESR und DC-Bias-Kapazität.
- **Layout-Einfluss:** Schleifeninduktivität in die Schaltschleife einsetzen (z. B. 2 nH für ein gutes, 10 nH für ein schlechtes Layout), V_DS-Spitzen an Q101/Q102 ansehen → Entscheidung FET-Klasse und Snubber-Bedarf.
- Fälle: Wirkungsgrad bei 22/24/26 V × 0,3/1,5/3 A; Verlust je Bauteil per `.meas` (Mittelwert u · i über ganze Perioden nach dem Einschwingen); mit/ohne D102; Frequenz- und FET-Varianten. Anlauf mit kleinem C_SS verkürzen.
- Vergleich mit A11; Abweichung > 10 % erklären.

## A14 Stückliste und Übergabe
- Zeilen im Format `Stueckliste_Vorlage.csv` (Bereich A, Referenzen 100–199), je Teil 2 Händler mit Datum.
- An B: f, L (Wert, DCR), ILIM, R_SENSE oder DCR-Netzwerk, C_ISS(Q101).
- An C: FET-Klasse und zulässige Spannung am Buck-Eingang, I_PK,max, höchster Eingangsstrom (Nennlast und Überlast).
- An D: f, C_IN (effektiv, ESR), Verluste A, Kupferflächen- und Wärmebedarf, Stellschrauben und Messpunkte.

---

## Fertig, wenn
f, L101, Q101, Q102, (D102), R101 bzw. DCR-Netzwerk, C120, D101 und alle C_IN mit Hersteller-Teilenummer, 2 Händlern, Rechnung, Verlustbilanz und Simulation festgelegt und an B, C, D übergeben sind.

## Typische Fehler
- Mit typischen statt Min/Max-Werten rechnen (V_SENSE, f, R_DS(on) bei Temperatur).
- I_SAT nur gegen den Nennspitzenstrom statt gegen die maximale Strombegrenzung prüfen.
- Keramik-Nennkapazität statt DC-Bias-Kapazität verwenden.
- R_DS(on) bei 10 V statt bei 4,5 V ablesen.
- C_MILLER/Q_GD und Q_RR bei 26 V vernachlässigen.
- E12 auf Spulen oder Kondensatoren anwenden (gilt nur für Widerstände).
- Um einzelne mW optimieren und dabei Reserve verschenken (00 §1a).

## Gegenprobe
Frühere KI: `00_Projekt/altKI_Bauteil_Dimensionierung.md` (Abschnitt 1) – nur zum Vergleichen, nicht übernehmen.

## Startprompt für die KI
> Du hilfst mir bei Bereich A (Leistungsstufe) unseres Studienprojekts: nicht isolierter Buck 22–26 V → 12 V / 3 A mit LTC7800, Gruppenziel höchster Wirkungsgrad, aber sichere Funktion mit Reserven (auch für unser selbst gemachtes Layout) hat Vorrang; Optionen mit weniger als 50 mW Unterschied gelten als gleich (00 §1a). Lies `00_Projektkontext.md`, `01_Quellen_ApplicationNotes.md` und `A_Leistungsstufe.md` vollständig und halte dich an die Regeln (Widerstände E12 außer R_SENSE, Keramik nur X7R/C0G, SMD ≥ 0603, Spulen nur Würth, jedes Teil bei 2 europäischen Händlern mit Datum). Rechne mit vollständigen Herleitungen und Einheiten in jedem Schritt, gib zu jedem Datenblattwert Seite und Revision an, rechne Worst Case mit Min/Max-Werten. Arbeite A1–A14 in der angegebenen Reihenfolge ab; zeig mir bei jedem Schritt die Optionen mit ihren Trade-offs und Zahlen (Verlust in mW, Kosten, Platz, Robustheit) und lass mich entscheiden. Am Ende brauche ich: Wertetabelle, Rechnung, Auswahlbegründung mit Alternativen, Simulationsergebnisse und Stücklistenzeilen im Format `Stueckliste_Vorlage.csv`.
