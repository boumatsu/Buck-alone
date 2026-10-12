# Bereich B – Regelung und Beschaltung des LTC7800

Für Person B und ihre KI. Vorher `00_Projektkontext.md` lesen (Regeln, Prioritäten §1a, LTC7800-Daten, Randwerte, Schnittstellen). Quellen-Kürzel Q.. siehe `01_Quellen_ApplicationNotes.md`.

## Auftrag
Alle Bauteile rund um den LTC7800 festlegen, die nicht zur Leistungsstufe gehören: Ausgangskondensatoren, Rückkopplung, Kompensation (Regelkreis), Soft-Start, Einschaltschwelle, Frequenzwiderstand, Betriebsart, INTVCC/EXTVCC, Sense-Filter, PGOOD. Dazu das **gemeinsame LTspice-Modell des Buck** aufbauen, das A, C und D mitbenutzen.
**Priorität (00 §1a):** stabil und robust über alle Arbeitspunkte, Bauteiltoleranzen und mit unserem selbst gemachten Layout – Wirkungsgrad erst danach.

## Was ist hier „Regelung"?
Der LTC7800 hält V_OUT über einen Regelkreis auf 12 V (Q01 S. 10–11):

```
V_OUT ─► Teiler R_B/R_A ─► VFB ─► Fehlerverstärker (g_m = 2 mS, Sollwert 0,8 V) ─► ITH-Spannung
  ▲                                                                                 │ (Kompensation R_C, C_C, C_C2 an ITH)
  │                                                                                 ▼
  └── C_OUT ◄── Spulenstrom ◄── Q101 aus, sobald der Spulenstrom (über R_SENSE gemessen) den ITH-Wert erreicht
```

- **Innerer Kreis (Strommodus):** Q101 wird jeden Takt eingeschaltet und abgeschaltet, sobald der Spulenstrom den von ITH vorgegebenen Wert erreicht.
- **Äußerer Kreis (Spannung):** Sinkt V_OUT bei mehr Last, steigt ITH, der Spitzenstrom steigt, V_OUT kommt zurück.
- Verstärker und Komparatoren sitzen im IC. **B wählt die Bauteile, die Verstärkung und Dynamik bestimmen:** Teiler (Sollwert), R_C/C_C/C_C2 (Regler), C_OUT und R_SENSE (Teil der Regelstrecke).
- Falsch gewählt heißt: Der Ausgang schwingt, oder V_OUT bricht bei Laständerungen stark ein bzw. schießt über.

## Bauteile von B
| Ref | Funktion | Pin |
|---|---|---|
| U201 | LTC7800 (QFN-20 3 × 4 mm, Exposed Pad = SGND) | – |
| R201, R202 (+R203) | Teiler R_B (oben, ggf. 2 in Reihe), R_A (unten) | VFB 7 |
| C201 | C_FF über R_B (Bestückungsoption) | VFB 7 |
| R204, C202, C203 | Kompensation R_C, C_C, C_C2 | ITH 8 |
| C204 | Soft-Start C_SS | TRACK/SS 19 |
| R205, R206 | RUN-Teiler (Einschaltschwelle) | RUN 4 |
| R207 | R_FREQ | FREQ 20 |
| R208, C205 | Sense-Filter (R nur in SENSE+, C zwischen den Pins am IC) | SENSE+ 6, SENSE− 5 |
| C206, C207 | INTVCC ≥ 2,2 µF + 1 µF direkt an INTVCC/PGND | INTVCC 14, PGND 16 |
| R209, C208 | VIN-Pin-Filter ≤ 10 Ω + 0,1–1 µF an SGND | VIN 17 |
| R210 | PGOOD-Pull-up | PGOOD 9 |
| C211…C21x | C_OUT | – |
| JP201 | Lötbrücke Betriebsart (PLLIN/MODE) | 1 |
| – | ILIM (nach A), EXTVCC an V_OUT | 18, 15 |

## Wichtigste Quellen für B
| Quelle | Wofür |
|---|---|
| Q01 LTC7800-Datenblatt S. 8–13, 18–20, 24–27; Fig. 15/16 (12 V Ausgang) | Pins, Formeln, Referenzwerte |
| Q07 AN-149 | Kleinsignalmodell Strommodus, Kompensation Schritt für Schritt |
| Q02 LTpowerCAD (LTC7800-Projekt), Q03 DC2736A (12 V, 500 kHz) | Gegenprobe für Kompensation und C_OUT |
| Q11 LTspice-Bode (EngineerZone), Q12, Q13 | Regelkreis simulieren, Optionen zur Optimierung |
| Q33 Würth ANP062, Q45 Murata SimSurfing | DC-Bias der C_OUT-Keramik |
| Q10 ADI Current Sensing Part 3 | Sense-Leitungen, Filter |

## Reihenfolge
```
B1 Vorbereitung → B2 Betriebsart → B3 Teiler → B4 Ziele Rippel/Lastsprung → B5 C_OUT → B6 Kompensation
B7 Soft-Start → B8 RUN → B9 FREQ/ILIM/Sense-Filter → B10 INTVCC/EXTVCC/VIN → B11 PGOOD
B12 Stellschrauben → B13 Modell und Simulationen ──(Ziele verfehlt?)──► zurück zu B5/B6 → B14 Stückliste und Übergabe
```
B3, B7, B8, B10, B11 hängen kaum von anderen ab und können sofort gemacht werden. B5/B6 brauchen f, L und R_SENSE von A (bis dahin Startannahmen aus 00 §7).

---

## B1 Vorbereitung
- Datenblatt Q01: S. 8–9 (Pinfunktionen), 10–13 (Funktionsbild, Betriebsarten, Schutz), 18–20, 24 (Lastsprung, OPTI-LOOP), 25–27 (Layout), Kurven S. 5–8 („Maximum Current Sense Voltage vs ITH Voltage", „Regulated Feedback Voltage vs Temperature", „TRACK/SS Pull-Up Current").
- AN-149 (Q07) durcharbeiten – Grundlage für B6 und für die Prüfung.
- LTpowerCAD-Projekt (Q02) öffnen, auf unsere Daten umstellen.
- Hinweis: S. 24 verweist für ITH-Startwerte auf „Figure 9" – das ist aber das Layoutbild. Gemeint sind die Referenzschaltungen.

## B2 Betriebsart (PLLIN/MODE, S. 12)
| Option | Beschaltung | Vorteile | Nachteile |
|---|---|---|---|
| Burst Mode | an SGND | bester Wirkungsgrad bei kleiner Last (50 µA Ruhestrom) | größerer Rippel und wechselnde Frequenz bei kleiner Last |
| Pulse-Skipping | 1,2 V…INTVCC − 1,3 V | feste Frequenz bis ≈ 1 % Last, besser als FCM bei kleiner Last | Teiler nötig; schlechter als Burst |
| Forced Continuous | an INTVCC | feste Frequenz, kleinster Rippel, gut für EMV-Messung | schlechter Wirkungsgrad bei kleiner Last |

Bei 3 A arbeiten alle gleich. **Lötbrücke JP201** (SGND ↔ INTVCC) vorsehen, dann kann man nach dem Aufbau wechseln. Entscheidung mit Wirkungsgrad und Rippel bei 0,1–0,3 A begründen.

## B3 Ausgangsspannung (Teiler R_A, R_B)
- Formel (S. 18): V_OUT = 0,8 V · (1 + R_B/R_A) → R_B/R_A = 12 V / 0,8 V − 1 = 14.

| Option | Ergebnis | Vorteile | Nachteile |
|---|---|---|---|
| ein E12-Paar: 47 kΩ / 3,3 kΩ | 0,8 V · (1 + 14,24) = 12,19 V (+1,6 %) | 2 Bauteile, sicher E12 | Fehler +1,6 % |
| Reihenschaltung: R_A = 12 kΩ, R_B = 150 kΩ + 18 kΩ | 12,000 V | exakt | 3 Bauteile; erlaubt? (00 F3) |
| Reihenschaltung: 8,2 kΩ und 100 kΩ + 15 kΩ | 12,02 V | fast exakt | 3 Bauteile |

| Toleranzklasse | Worst Case 12 k / 168 k mit V_FB = 0,792…0,808 V | Abwägung |
|---|---|---|
| 1 % | 11,66 V … 12,35 V (−2,8 % / +2,9 %) | billig |
| 0,1 % | 11,86 V … 12,14 V (±1,2 %), dann dominiert V_FB | etwas teurer (Dünnfilm) |

- Teilerimpedanz: R_B ≈ 100–500 kΩ üblich. Kleiner → robuster gegen Störungen, mehr Verlust (hier ≈ 67 µA · 12 V = 0,8 mW, vernachlässigbar). Größer → I_FB-Fehler (50 nA · R_B, bei 168 kΩ 8,4 mV) und Störempfindlichkeit steigen.
- **Bauteilgruppen:** Dickschicht 1 % (z. B. Yageo RC, Vishay CRCW, Panasonic ERJ), Dünnschicht 0,1 % (z. B. Vishay TNPW, Panasonic ERA, Susumu RG); 0603/0805.
- Layout: Teiler an C_OUT(+) und SGND, VFB-Leitung kurz und weg von SW (S. 25).

## B4 Ziele für Rippel und Lastsprung
Die Aufgabe nennt keine Werte → B legt sie fest und begründet sie.

| Option | Beispielziele | Folgen |
|---|---|---|
| streng | Rippel ≤ 0,2 % (24 mV), Lastsprung 20 → 80 % ≤ ±2 % | viel C_OUT, hohe f_c → empfindlicher |
| **mittel (Vorschlag)** | Rippel ≤ 50 mV, Lastsprung ≤ ±3 % (±0,36 V) | ausgewogen |
| locker | Rippel ≤ 1 %, Lastsprung ≤ ±5 % | wenige Bauteile, robuster Regelkreis |

Zusätzliche harte Grenze: V_OUT nie über 14 V (EXTVCC hängt an V_OUT, S. 2), auch beim Lastabwurf.

## B5 Ausgangskondensatoren C_OUT
**Rechnung:**
- Rippel (S. 18): ΔV_OUT ≈ ΔI_L · (ESR + 1/(8 · f · C_OUT)), am größten bei V_IN,max. Beispiel ΔI_L = 0,9 A, 500 kHz, C_eff = 20 µF, ESR 5 mΩ: 0,9 A · (5 mΩ + 12,5 mΩ) = 15,8 mV.
- Lastsprung (Abschätzung): ΔV ≈ ΔI_LAST / (2π · f_c · C_OUT). Beispiel 1,8 A: f_c = 30 kHz, 30 µF → 0,32 V; f_c = 50 kHz, 47 µF → 0,12 V. **C_OUT wird meist vom Lastsprung-Ziel bestimmt.**
- Effektive Kapazität aus der DC-Bias-Kurve bei 12 V (Q33, Q45).

**Optionen:**

| Option | Vorteile | Nachteile |
|---|---|---|
| nur Keramik X7R | kleinste ESR, kleinster Rippel, kompakt | starker DC-Bias-Verlust bei 12 V an 16/25-V-Teilen (→ 50-V-Teile oder mehr Stück); keine ESR-Nullstelle, die Kompensation muss die Phase liefern |
| Keramik + Polymer (Tantal- oder Alu-Polymer), wie Fig. 15 | große Kapazität; ESR-Nullstelle hilft der Phasenreserve; dämpft | größer; etwas mehr Rippel durch ESR; Spannungs-Derating bei Tantal-Polymer beachten |
| Keramik + Alu-Elko | billig, große Kapazität | hohe ESR, Lebensdauer, Größe |

- **Bauteilgruppen:** X7R-MLCC 25/50 V in 1206/1210 (Murata GRM, TDK C, Würth WCAP-CSGP, Samsung CL, KEMET); Polymer z. B. KEMET T520/T521 (Fig. 15: T521), Panasonic POSCAP/SP-Cap, Alu-Polymer verschiedener Hersteller; Alu-Elko z. B. Würth WCAP-ASLI.

## B6 Kompensation (Regelkreis)
**Optionen für das Vorgehen:**

| Weg | Vorteile | Nachteile |
|---|---|---|
| Handrechnung nach AN-149 (Q07) + MATLAB | man versteht es (Prüfung!), Parameterstudien möglich | Aufwand; Modellgrenzen |
| LTpowerCAD (Q02) | schnell; Bode und Lastsprung; Export nach LTspice | Black Box → Ergebnis selbst nachrechnen |
| LTspice-Bode am schaltenden Modell (Q11) oder PLECS-AC-Sweep | realistischer, enthält Schaltverhalten | Rechenzeit, Messaufbau im Modell nötig |

**Empfohlen:** Handrechnung → Gegenprobe mit LTpowerCAD → Prüfung mit LTspice (Bode + Lastsprung).

**Schritte (Typ-II-Netzwerk an ITH):**
1. **Regelstrecke:** k = ΔV_SENSE / ΔV_ITH aus der Kurve „Maximum Current Sense Voltage vs ITH Voltage" → G_CS = k / R_SENSE (A/V). Lastpol f_P = 1/(2π · R_LAST · C_OUT); ESR-Nullstelle f_ESR = 1/(2π · ESR · C_OUT).
2. **Durchtrittsfrequenz f_c:**

   | Option | Vorteile | Nachteile |
   |---|---|---|
   | konservativ f_c ≈ f/10…f/15 (bei 370–510 kHz ≈ 25–50 kHz) | robust gegen Layout, Toleranzen, Rauschen | etwas mehr Lastsprung-Abweichung |
   | aggressiv f_c ≈ f/5…f/6 | schnelle Reaktion | wenig Reserve, empfindlich auf Abtasteffekte des Strommodus |

3. **R_C** (Verstärkung bei f_c): R_C = 2π · f_c · C_OUT,eff · V_OUT / (g_m · G_CS · V_FB), g_m = 2 mS. Danach nächster E12-Wert.
4. **C_C** (Nullstelle): f_Z = 1/(2π · R_C · C_C) ≈ f_c/5…f_c/10 → C_C = 1/(2π · R_C · f_Z).
5. **C_C2** (Hochfrequenzpol): f_P2 = 1/(2π · R_C · C_C2) bei der ESR-Nullstelle oder ≈ f/2 (der kleinere Wert) → C_C2 ≪ C_C.
6. **Bode in MATLAB:** T(s) = (V_FB/V_OUT) · g_m · Z_ITH(s) · G_CS · Z_OUT(s), Z_OUT = R_LAST ‖ (ESR + 1/(s · C_OUT)); optional Doppelpol bei f/2. Prüfen bei 22/26 V, 0,3/3 A, C_OUT ±20 % und DC-Bias: **Phasenreserve ≥ 60° anstreben (mindestens 45°), Amplitudenreserve ≥ 10 dB**.
7. **Feinjustieren** (S. 24): R_C größer → mehr Verstärkung/Bandbreite; Nullstelle konstant halten, indem C_C um denselben Faktor kleiner wird.
8. **C_FF (Option, S. 18):** Nullstelle 1/(2π · R_B · C_FF) nahe f_c, Pol bei 1/(2π · (R_A ‖ R_B) · C_FF). Fig. 16: 10 pF an 487 kΩ → Nullstelle ≈ 33 kHz; bei R_B = 168 kΩ bräuchte dieselbe Nullstelle ≈ 29 pF. Nur mit Simulation, Footprint zunächst unbestückt.

- **Plausibilität:** Fig. 16 (12 V, 2,1 MHz): 2 kΩ + 0,47 nF, 82 pF; Fig. 15 (12 V, 320 kHz): 13,7 kΩ + 3,3 nF, 100 pF; DC2736A (Q03, 12 V, 500 kHz). Andere f, C_OUT, R_SENSE → nur Größenordnung vergleichen.
- **Bauteilgruppen:** R_C E12; C_C/C_C2 bevorzugt C0G (stabil über Temperatur, in 0603/0805 bis etwa 10–47 nF erhältlich), sonst X7R.

## B7 Soft-Start C_SS
- t_SS = C_SS · 0,8 V / I_SS, I_SS = 7/10/14 µA (S. 3, 19). Beispiel 47 nF: 3,8 ms (2,7…5,4 ms).

| Option | Vorteile | Nachteile |
|---|---|---|
| kurz (≈ 1–2 ms) | schneller Start | höherer Ladestrom in C_OUT, mehr Einschaltstrom am Eingang |
| **mittel (≈ 3–5 ms)** | Ladestrom klein, Start schnell genug | – |
| lang (≈ 10 ms und mehr) | sehr kleiner Einschaltstrom | langsamer Start |

- Kriterium: I = C_OUT · V_OUT / t_SS plus Last bleibt deutlich unter der Strombegrenzung (Foldback ist im Soft-Start aus, S. 13). Einschaltstrom am Eingang mit C und D abstimmen.
- C_SS: X7R oder C0G, ≥ 0603.

## B8 Einschaltschwelle RUN
| Option | Vorteile | Nachteile |
|---|---|---|
| RUN offen (interner 7-µA-Pull-up, S. 11) | kein Bauteil | Wandler startet schon bei sehr kleiner V_IN, läuft im Dropout mit hohem Eingangsstrom |
| **Teiler als Unterspannungsschwelle** | definierter Start/Stopp | 2 Widerstände |
| Teiler + Lötbrücke/Jumper nach SGND | wie oben, zusätzlich Ausschalten zum Testen | 1 Bauteil mehr |

- V_EIN = 1,21 V · (1 + R_B/R_A) − 7 µA · R_B; V_AUS = 1,16 V · (1 + R_B/R_A) − 7 µA · R_B (S. 19).
- Beispiel 22 kΩ / 330 kΩ: ein 17,05 V, aus 16,25 V; mit Schwelle 1,15…1,27 V ein bei 16,1…18,0 V → bei 22 V sicher an.
- Prüfen: bei der höchsten Eingangsspannung von C (z. B. 60 V → V_RUN ≈ 60 V · 22/352 = 3,75 V) unter 8 V bzw. ≤ 100 µA in die 11-V-Klemme (S. 18).

## B9 FREQ, ILIM und Sense-Filter
- **R_FREQ:** E12-Wert aus A2 (27 k / 33 k / 39 k), mit Fig. 8 prüfen, Toleranzband ±15 % angeben. FREQ nie offen lassen (interner 20-µA-Pull-up, S. 9).
- **ILIM:** nach A4 (Empfehlung INTVCC).
- **Sense-Filter:**

  | Option | Vorteile | Nachteile |
  |---|---|---|
  | ohne Filter | kein Bauteil | störempfindlich, besonders mit eigenem Layout |
  | **RC: 10–100 Ω in SENSE+, 1–2 nF zwischen den Pins (wie Fig. 11–13, 15, 16)** | filtert Schaltspitzen | Zeitkonstante muss ≪ t_ON bleiben (z. B. 20 Ω · 1 nF = 20 ns ≪ 0,9 µs) |
  | DCR-Netzwerk (A4) | – | nur bei DCR-Messung |

- **Wichtig:** Widerstand nur in die SENSE+-Leitung. In SENSE− fließen bei 12 V ≈ 700 µA (S. 3, 14); 20 Ω dort ergäben 14 mV Fehler – bei 43 mV (ILIM = INTVCC) bzw. 22 mV (ILIM = GND) Mindestschwelle.
- SENSE+/SENSE− als Kelvin-Leitungen eng parallel, Kondensator direkt an den IC-Pins (S. 14, 25).

## B10 INTVCC, EXTVCC, VIN-Pin
| Punkt | Optionen | Abwägung |
|---|---|---|
| INTVCC-Kondensator | 2,2 µF / 4,7 µF + 1 µF (S. 20) | X7R 10–25 V, DC-Bias bei 5,1 V beachten; größer puffert Gate-Stromspitzen besser |
| EXTVCC | direkt an V_OUT (S. 20, Variante 2) / an GND | an V_OUT: höchster Wirkungsgrad (VIN-LDO nur beim Anlauf). An GND: einfacher, aber bis zu 10 % Verlust bei hoher V_IN (S. 20) → V_OUT wählen |
| VIN-Pin-Filter | R ≤ 10 Ω + 0,1–1 µF an SGND (S. 18) | Nennspannung aus der Maximalspannung von C |

- SGND/PGND-Sternpunkt an C_OUT(−) (S. 25–26) – Vorgabe an D/Layout.

## B11 PGOOD
| Option | Vorteile | Nachteile |
|---|---|---|
| **100 kΩ an INTVCC (alle Referenzschaltungen Fig. 11–16)** | einfach, ≈ 51 µA | Pinbeschreibung S. 9 sagt „INTVCC für nichts anderes verwenden" – die Referenzen tun es trotzdem für den Pull-up → als zulässig betrachten |
| Teiler von V_OUT (≤ 6 V am Pin) | unabhängig von INTVCC | 2 Widerstände; Pegel hängt an V_OUT |

PGOOD ist Open Drain, ≤ 6 V, Fenster ±10 %, 25 µs Verzögerung (S. 4, 9, 13). Signal an D (LED-Treiber). Die LED selbst nie aus INTVCC versorgen.

## B12 Stellschrauben für die Inbetriebnahme
- Footprint C_FF (unbestückt) und C_C2.
- R_C, C_C, C_C2 so platzieren, dass man sie nach dem Aufbau tauschen kann (nah am IC, aber zugänglich).
- Platz für zusätzliche C_OUT.
- Lötbrücke JP201 (Betriebsart); optional Jumper RUN → SGND.
- Injektionswiderstand im Teiler und Messpunkte V_OUT, VFB, ITH (mit D, D7).

## B13 Gemeinsames Buck-Modell und Simulationen (LTspice)
- Modell aufbauen: LTC7800 aus der LTspice-Bibliothek (Beispiel-Jig `examples/jigs/7800.asc` oder LTpowerCAD-Export als Startpunkt), Bauteile von A, C_OUT und Beschaltung von B. An A, C, D weitergeben.
- Bode am schaltenden Modell: Anleitung Q11.

| Fall | Bedingung | Bestanden, wenn |
|---|---|---|
| Anlauf | 22 und 26 V; 0 A und 3 A | t_SS wie berechnet, Überschwingen ≤ 2 %, keine Strombegrenzung |
| Lastsprung | 0,6 ↔ 2,4 A, Flanke 1–10 µs (S. 24) | Abweichung ≤ Ziel aus B4, ohne Schwingen, V_OUT < 14 V |
| Netzsprung | 22 ↔ 26 V | V_OUT bleibt im Band |
| Kurzschluss | im Betrieb und beim Einschalten | Strom ≈ I_SC aus A4, Foldback wirkt |
| Regelkreis | 22/26 V, 0,3/3 A | Phasenreserve ≥ 60° angestrebt (≥ 45° Minimum), Amplitudenreserve ≥ 10 dB |
| Robustheit | C_OUT −20 %, L −20 %, kalt/warm | weiterhin stabil |
| Teillast | 0,1–0,3 A in der gewählten Betriebsart | Rippel und Wirkungsgrad dokumentiert |
| Toleranzen | Worst Case / Monte Carlo (Teiler, V_FB, C_OUT) | V_OUT-Band wie B3 |

## B14 Stückliste und Übergabe
- Zeilen im Format `Stueckliste_Vorlage.csv` (Bereich B, Referenzen 200–299), je Teil 2 Händler mit Datum.
- An A: C_OUT (effektiv, ESR), Betriebsart. An D: PGOOD-Signal, Sternpunkt-Vorgabe, Messpunkte (V_OUT, VFB, ITH), Stellschrauben. An alle: Buck-Modell.

---

## Fertig, wenn
U201 und alle Bauteile der Tabelle mit Wert, Teilenummer und 2 Händlern festgelegt; Rechnungen B2–B11 dokumentiert; Simulationen B13 bestanden oder Abweichung begründet.

## Typische Fehler
- Widerstand in der SENSE−-Leitung (700 µA Offset).
- FREQ oder EXTVCC offen lassen.
- PGOOD an mehr als 6 V; LED aus INTVCC versorgen.
- V_FB-Toleranz in der V_OUT-Rechnung vergessen.
- C_OUT mit Nennkapazität statt DC-Bias-Kapazität rechnen.
- Kompensation nur bei einem Arbeitspunkt prüfen.

## Gegenprobe
Frühere KI: `00_Projekt/altKI_Bauteil_Dimensionierung.md` (Abschnitte 1.7–1.12) – nur zum Vergleichen. Ihr Lastsprung (±0,91 V) passt zu f_c ≈ 10 kHz, die Kompensation dort ist also nicht so schnell wie angegeben.

## Startprompt für die KI
> Du hilfst mir bei Bereich B (Regelung und Beschaltung des LTC7800) unseres Studienprojekts: nicht isolierter Buck 22–26 V → 12 V / 3 A mit LTC7800, Gruppenziel höchster Wirkungsgrad, aber ein stabiler, robuster Regelkreis hat Vorrang (00 §1a). Lies `00_Projektkontext.md`, `01_Quellen_ApplicationNotes.md` und `B_Regelung_und_IC-Beschaltung.md` vollständig und halte dich an die Regeln (Widerstände E12 außer R_SENSE, Keramik nur X7R/C0G, SMD ≥ 0603, jedes Teil bei 2 europäischen Händlern mit Datum). Erkläre mir den Regelkreis so, dass ich ihn in der Prüfung ohne Hilfsmittel erklären kann (Grundlage AN-149). Rechne mit vollständigen Herleitungen und Einheiten, gib zu jedem Datenblattwert Seite und Revision an, rechne Worst Case mit Min/Max-Werten. Arbeite B1–B14 in der angegebenen Reihenfolge ab; zeig mir bei jedem Schritt die Optionen mit Trade-offs und Zahlen und lass mich entscheiden. Am Ende brauche ich: Wertetabelle, Rechnung, Auswahlbegründung, Bode-Diagramme und Simulationsergebnisse, das LTspice-Modell und Stücklistenzeilen im Format `Stueckliste_Vorlage.csv`.
