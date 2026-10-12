# 00 – Projektkontext: Gruppe 3, DC/DC-Buck mit LTC7800

Zweck: gemeinsame Faktenbasis für die Bereichsdateien A–D und für die KIs der Gruppenmitglieder. **Immer zuerst lesen.** Quellen und Application Notes: `01_Quellen_ApplicationNotes.md`.
Stand: 12.10.2026 · Kennzeichnung: **[fest]** vorgegeben/entschieden · **[Annahme]** vorläufig · **[offen]** zu klären

---

## 1 Aufgabe (Quelle: `WS2026_Aufgabenstellung_V1_2.pdf`)

| ID | Anforderung | Status |
|---|---|---|
| R01 | Nicht isolierter DC/DC-Wandler, V_IN = 22…26 V | [fest] |
| R02 | V_OUT = 12 V | [fest] |
| R03 | I_OUT = 3 A dauerhaft | [fest] |
| R04 | Controller LTC7800 | [fest] |
| R05 | Spulen nur von Würth Elektronik | [fest] |
| R06 | Stecker: Bananenbuchsen (PDF nennt 2,54-mm-Stiftleisten; Prof erlaubt Bananenbuchsen) | [fest] |
| R07 | Platine ≤ 116,8 × 61 mm (Full Brick), ≤ 6 Lagen, ≤ 1 oz Kupfer, keine Höhenbegrenzung | [fest] |
| R08 | 4 mm Sperrabstand THT ↔ SMD | [fest] |
| R09 | Normen EN 60950, UL 508, EN 61000 (EMV), CISPR 16 – so wie im PDF | [fest] |
| R10 | Status-LED zeigt „Ausgang in Ordnung" (PGOOD) | [fest] |
| R11 | Verpolschutz am Eingang | [fest] |
| R12 | Überstromschutz am Eingang | [fest] |
| R13 | Überstromschutz am Ausgang | [fest] |
| R14 | Burst 2 kV am Eingang überstehen; besser: danach ohne Teiletausch weiterbetreibbar | [fest] |
| R15 | Surge 1 kV überstehen; besser: danach ohne Teiletausch weiterbetreibbar | [fest] |
| R16 | Kriech-/Luftstrecken nach https://community.aisler.net/t/4-layer-1-6mm-enig-design-rules/3733 | [fest] |
| R17 | Budget 100 € netto für die komplette Stückliste inkl. Platine; alles wird bezahlt | [fest] |
| R18 | Gruppenziel Gruppe 3: höchster Gesamtwirkungsgrad – **nachrangig zur sicheren Funktion** (siehe §1a) | [fest] |
| R19 | 2–3 funktionierende Muster; Bestellung und Bestückung nach der Abgabe | [fest] |

Abgabe am Semesterende: Schaltplan, Zeit- und Taskplan, Dokumentation der Bauteil-Dimensionierung, Berechnung der Bauteilwerte, KiCad-Übungsunterlagen (vorhanden). Danach schriftliche Prüfung ohne Hilfsmittel (EMV, Schaltungsentwurf, KiCad) → jedes Mitglied muss seine Rechnungen verstehen und erklären können.

---

## 1a Prioritäten [fest]

Der Prof ist zufrieden, wenn die Platine **funktioniert** – auch wenn sie nicht die effizienteste ist. Der echte Wirkungsgrad hängt am Ende stark vom Layout ab, und das macht die Gruppe selbst. Reihenfolge:

1. **Funktioniert sicher und reproduzierbar:** bei 22–26 V und 0–3 A, mit Bauteiltoleranzen, mit unserem eigenen Layout, nach Surge und Burst.
2. **Einfach** aufzubauen, zu löten, in Betrieb zu nehmen und zu messen (Messpunkte, Bestückungsoptionen, siehe §5a).
3. **Budget** ≤ 100 € netto.
4. **Wirkungsgrad** so hoch wie möglich, ohne 1.–3. zu gefährden.

**Entscheidungsregel:** Liegen zwei Optionen beim Verlust weniger als ≈ 50 mW (≈ 0,15 Prozentpunkte) auseinander, gelten sie als gleichwertig → dann gewinnt die robustere, einfachere oder billigere. Simulierte Wirkungsgrade sind Obergrenzen. Nicht um einzelne mW optimieren, lieber Reserven einplanen (Spannung, Strom, Temperatur, Phasenreserve).

---

## 2 Regeln für alle Bauteile

- **Widerstände:** E12-Werte, Ausnahme R_SENSE [fest]. Reihen-/Parallelschaltung zweier E12-Widerstände für Zwischenwerte: [offen], bisher als erlaubt angenommen.
- **Keramikkondensatoren:** nur X7R oder C0G, **kein X5R** [fest]. Für Kondensatoren und Spulen gilt keine E12-Pflicht.
- **SMD-Gehäuse:** nicht kleiner als 0603 [fest].
- **Spannungsreserve:** Die frühere KI notierte „Nennspannung 5–10 × Betriebsspannung" als Prof-Vorgabe – unbestätigt [offen]. Bis zur Klärung: Reserve je Bauteil begründen, Keramik immer mit der **DC-Bias-Kapazität** (Herstellerkurve) rechnen.
- **Bezug:** jedes Teil bei **≥ 2 unabhängigen Händlern in Europa** (z. B. Mouser, Farnell, DigiKey, RS, Distrelec, TME) mit Bestand, Preis und Datum. Würth-Teile ebenfalls bei Händlern nachweisen, nicht nur bei Würth [fest].
- **Datenblatt-Beispielteile** (LTC7800-Datenblatt von 05/2017) sind nur Klassenhinweise. Teile nach Parametern auswählen, Lieferbarkeit selbst prüfen [fest].
- **Bestückung:** Heißluft und Reflowofen vorhanden → QFN/DFN/Power-SMD möglich, Schablone mitbestellen [fest].
- **Platine:** vermutlich JLCPCB, 4 Lagen empfohlen; der Preis entscheidet [Annahme].
- **Werkzeuge:** LTspice, KiCad, MATLAB, PLECS; Würth REDEXPERT (online) für Spulen- und Kondensatorverluste; ADI LTpowerCAD mit fertigem LTC7800-Projekt als Gegenprobe (Q02) [fest].

---

## 3 Lastfälle und EMV-Annahmen

- **Surge** (EN 61000-4-5): 1 kV; Leerlauf 1,2/50 µs, Kurzschluss 8/20 µs; 2 Ω Generatorimpedanz; Einkopplung Leitung–Leitung über 18 µF (Normaufbau – prüfen). Spitzenstrom ≈ 1000 V / 2 Ω = **500 A**. Nur differenziell (+ gegen −) [Annahme: kein Test gegen Erde – beim Prof bestätigen].
- **Burst** (EN 61000-4-4): 2 kV; Einzelimpuls 5/50 ns; 50-Ω-Generator; Impulspakete (5 kHz: 15 ms Paket alle 300 ms; 100 kHz: 0,75 ms); Einkopplung über 33 nF. Differenziell auslegen, Gleichtakt über Layout [Annahme].
- **Verpolung:** −22…−26 V dauerhaft (Labornetzteil falsch angeschlossen).
- **Hot-Plug:** Einstecken an ein laufendes Labornetzteil. Kabelinduktivität und Keramik-C_IN bilden einen Schwingkreis, Überschwingen bis ≈ 2 × V_IN ≈ 52 V möglich (Linear Technology Application Note 88).
- **Fehler hinter dem Schutz** (z. B. durchlegierter oberer FET): Konzept des LTC7800 (S. 21): Ausgangs-Überspannung → unterer FET dauerhaft an („Crowbar") → hoher Strom soll die **Eingangssicherung** auslösen. Bereich C muss festlegen, was bei uns stattdessen auslöst oder begrenzt.
- **Emissionen:** CISPR 16 ist nur das Messverfahren. Als Orientierung: leitungsgebundene Grenzwerte Klasse B (CISPR 32): 0,15–0,5 MHz 66→56 dBµV QP / 56→46 dBµV AV; 0,5–5 MHz 56 dBµV QP / 46 dBµV AV; 5–30 MHz 60 dBµV QP / 50 dBµV AV [Annahme].

---

## 4 LTC7800 – Daten, die alle brauchen (Datenblatt Rev. F, 05/2017)

| Größe | Wert | Seite |
|---|---|---|
| V_IN | 4…60 V Betrieb, 65 V absolut | 2, 3 |
| V_OUT | 0,8…24 V; SENSE± maximal 28 V | 1, 2, 14 |
| V_FB | 0,792 / 0,800 / 0,808 V (−40…85 °C) | 3 |
| I_FB | ±5 nA typ, ±50 nA max | 3 |
| Fehlerverstärker g_m | 2 mS | 3 |
| V_SENSE(MAX) (min/typ/max) | ILIM = GND: **22/30/36 mV** · ILIM = INTVCC: 43/50/57 mV · ILIM offen: 64/75/85 mV | 3, 14 |
| SENSE−-Strom | ±2 µA bei V_SENSE− < INTVCC − 0,5 V; **≈ 700 µA** bei V_SENSE− > INTVCC + 0,5 V (bei uns 12 V → immer 700 µA) | 3, 14 |
| Frequenz über R_FREQ | 320 kHz…2,25 MHz. Tabelle: 25 kΩ → 0,27/0,32/0,36 MHz; 65 kΩ → 1,18 MHz typ; 100 kΩ → 1,75/2,1/2,4 MHz. FREQ an SGND → 0,94 MHz, an INTVCC → 1,44 MHz | 4, 12, 22 (Fig. 8) |
| Weitere Stützpunkte (Referenzschaltungen) | 25,5 kΩ → 320 kHz (Fig. 13, 15); 30,1 kΩ → 450 kHz (Fig. 14) | 29, 30 |
| t_ON(min) | ≈ 45 ns (bis ≈ 70 ns bei kleiner Sense-Spannung) | 4, 22 |
| Max. Tastgrad | 97/98 % | 3 |
| INTVCC | 4,85 / 5,1 / 5,35 V; ≥ 2,2 µF Keramik + 1 µF direkt an INTVCC/PGND; jede LDO ≥ 50 mA | 4, 9, 20 |
| EXTVCC | Umschaltung bei 4,5 / 4,7 / 4,9 V; max. 14 V; nie offen; für 5–14 V Ausgang direkt an V_OUT (höchster Wirkungsgrad) | 2, 4, 9, 20 |
| RUN | Schwelle 1,15 / 1,21 / 1,27 V, Hysterese 50 mV, 7 µA Pull-up; absolut 8 V oder ≤ 100 µA in die interne 11-V-Klemme | 2, 3, 18 |
| TRACK/SS | Ladestrom 7 / 10 / 14 µA; t_SS = C_SS · 0,8 V / 10 µA | 3, 19 |
| PGOOD | Open Drain, ≤ 6 V; Fenster ±10 % (7…13 %); 25 µs Verzögerung; 0,4 V bei 2 mA | 2, 4, 13 |
| Ausgangs-Überspannung | V_FB + 10 % (7…13 %) → oberer FET aus, unterer FET an | 3, 13, 21 |
| Foldback | V_OUT < 70 % → Strombegrenzung sinkt bis auf 45 %; im Soft-Start abgeschaltet | 13, 21 |
| Gate-Treiber | TG 2,5 Ω hoch / 1,5 Ω runter; BG 2,4 Ω / 1,1 Ω; Totzeit ≈ 20 ns je Flanke | 3 |
| Bootstrap | BOOST − SW max. 6 V; C_B ≥ 100 × C_ISS(oberer FET); D_B-Sperrspannung > V_IN,max | 2, 21 |
| Ruhestrom | Sleep 50 µA, Shutdown 14 µA, Pulse-Skip/FCM 2 mA | 3 |
| Gehäuse | QFN-20 3 × 4 mm, Exposed Pad = SGND (verlöten), θ_JA = 52 °C/W, T_J max. 125 °C (E/I) | 2 |
| Betriebsart PLLIN/MODE | SGND = Burst · INTVCC = Forced Continuous · 1,2 V…INTVCC − 1,3 V = Pulse-Skipping · externer Takt = Synchronisation | 12 |
| Kurzschlussstrom | I_SC = 45 % · I_LIM(MAX) − ½ · ΔI_L(SC), ΔI_L(SC) = t_ON(min) · V_IN / L | 21 |

**Referenzschaltungen im Datenblatt** (nur zur Plausibilität – Werte selbst rechnen): Fig. 11–13 (3,3/5 V), Fig. 14 (5 V, 450 kHz, GaN, DCR-Messung), **Fig. 15 (12 V, 320 kHz, 18–60 V, GaN, 10 A)**, **Fig. 16 (12 V, 2,1 MHz, 12,5–28 V, 10 A)**. Gemeinsam: EXTVCC an V_OUT (alle mit V_OUT ≥ 5 V); PGOOD mit 100 kΩ an INTVCC (alle); Sense-Filter bei R_SENSE-Messung 10–100 Ω + 1–2 nF (Fig. 11–13, 15, 16); 10 pF C_FF über dem oberen Teilerwiderstand (Fig. 11–13, 16).
Hinweis: Der Text auf S. 24 verweist für ITH-Startwerte auf „Figure 9" – Fig. 9 ist aber das Layoutbild (S. 27). Gemeint sind offenbar die Referenzschaltungen.

---

## 5 Randwerte (aus der Spezifikation gerechnet)

| Größe | Formel | 22 V | 24 V | 26 V |
|---|---|---|---|---|
| Ausgangsleistung | P_OUT = V_OUT · I_OUT | 36 W | 36 W | 36 W |
| Tastverhältnis (ideal) | D = V_OUT / V_IN | 0,545 | 0,500 | 0,462 |
| Eingangsstrom (η = 95 % angenommen) | I_IN = P_OUT / (η · V_IN) | 1,72 A | 1,58 A | 1,46 A |
| Rippelstrom C_IN (S. 18, Gl. 1) | I_RMS = (I_OUT / V_IN) · √(V_OUT · (V_IN − V_OUT)) | 1,49 A | 1,50 A | 1,50 A |
| Eingangswiderstand des Wandlers (negativ) | R_IN = V_IN² / P_IN, P_IN = 37,9 W | 12,8 Ω | 15,2 Ω | 17,8 Ω |

**Verlustbudget:** P_LOSS = P_OUT · (1/η − 1) → 0,73 W bei 98 %, 1,11 W bei 97 %, 1,50 W bei 96 %. Ein Zehntel Prozentpunkt ≈ 38 mW. **Jedes Bauteil im Strompfad wird mit seinem Verlust in mW bewertet.**
Orientierung für die Bereiche (kein Muss, nur zum Vergleichen von Optionen; Priorität 4 nach §1a): A ≤ 850 mW, B ≤ 50 mW, C ≤ 100 mW, D ≤ 100 mW → gesamt ≈ 1,1 W (η ≈ 97 %).

---

## 5a Layout im Blick (das Layout macht die Gruppe selbst)

Ob die Platine funktioniert, entscheidet zum großen Teil das Layout. Jeder Bereich wählt seine Bauteile deshalb so, dass das Layout einfach wird, und sieht Stellschrauben für die Inbetriebnahme vor.

- **Layout-Checkliste des Datenblatts** (S. 25–27, Fig. 9/10), gilt für alle:
  1. Schaltschleife C_IN – Q101 – Q102 so klein wie möglich (Bauteile direkt nebeneinander, durchgehende Masselage darunter).
  2. C_OUT(−) nah an C_IN(−), aber außerhalb dieser Schleife.
  3. SGND und PGND getrennt, Sternpunkt an C_OUT(−); SGND-Pad des IC, Masse des INTVCC-Kondensators und des Teilers dort anbinden.
  4. Teiler an C_OUT(+), nicht entlang der Eingangsströme; VFB-Leitung weg von SW und Spule.
  5. SENSE+/SENSE− eng parallel als Kelvin-Leitungen, Filter-C direkt am IC.
  6. INTVCC-Kondensator direkt an INTVCC/PGND; SW, TG, BOOST kurz und weg von empfindlichen Knoten.
- **Bauteilwahl fürs Layout:** Gehäuse, die sich eng platzieren und gut löten lassen; nicht mehr Bauteile im Leistungspfad als nötig; THT-Teile (Buchsen, ggf. Varistor oder Sicherungshalter) mit 4 mm Sperrzone einplanen.
- **Reserven wegen Layout:** Schleifeninduktivität verursacht Überschwinger am SW-Knoten → V_DS-Reserve der FETs. Parasitics und Toleranzen → Phasenreserve ≥ 60° anstreben.
- **Bestückungsoptionen** (Footprints, die nur bei Bedarf bestückt werden): RC-Snubber am SW-Knoten, Widerstand in Reihe zum Bootstrap-Kondensator, Gate-Widerstände (0 Ω), C_FF, Platz für zusätzliche C_IN/C_OUT, Injektionswiderstand für die Regelkreismessung, Lötbrücke für die Betriebsart (MODE).
- **Messpunkte** an allen wichtigen Knoten (Liste in D7).
- **Layout-Literatur:** AN-136, AN-139, TI SLYT682, Würth ANP044 und die Layouts der Demo Boards DC2736A/DC2786A (Q03–Q06, Q22, Q31 in `01_Quellen_ApplicationNotes.md`).

---

## 6 Blöcke und Zuständigkeit

```
J401/J402 ─► [C] Verpolung + Überstrom ─► [C] Surge/Burst-Klemmung ─► [D] Eingangsfilter ─►
   ─► [A] C_IN ─► [A] Leistungsstufe Q101/Q102/L101/R101 ─► [B] C_OUT ─► [D] J403/J404, LED, Messpunkte
                         ▲
                 [B] LTC7800 U201 + Beschaltung (FB, ITH, SS, RUN, FREQ, MODE, INTVCC/EXTVCC, Sense-Filter, PGOOD)
```

| Bereich | Inhalt | Referenzen | Datei |
|---|---|---|---|
| **A** | Leistungsstufe: Frequenz, Spule, MOSFETs, Strommessung, Bootstrap, C_IN, Verluste/Thermik der Stufe | 100–199 | `A_Leistungsstufe.md` |
| **B** | Regelung und LTC7800-Beschaltung: C_OUT, Teiler, Kompensation, Soft-Start, RUN, FREQ, MODE, INTVCC/EXTVCC, Sense-Filter, PGOOD; gemeinsames Buck-Simulationsmodell | 200–299 | `B_Regelung_und_IC-Beschaltung.md` |
| **C** | Eingangsschutz: Verpolung, Überstrom Eingang, Surge, Burst-Klemmung, Hot-Plug | 300–399 | `C_Eingangsschutz.md` |
| **D** | Eingangsfilter/EMV, Stecker, Status-LED, Messpunkte, Platinenrahmen, Zusammenführung (Stückliste, Budget, Gesamtwirkungsgrad) | 400–499 | `D_Filter_Anschluesse_Platine_Zusammenfuehrung.md` |

Personenzuordnung: [offen]. Vorschlag: Group Leader übernimmt D (enthält das Zusammenführen).

---

## 7 Schnittstellen zwischen den Bereichen

Mit den Startannahmen können alle sofort parallel anfangen. Wer liefert, ersetzt die Annahme durch den echten Wert und meldet ihn in der Gruppe.

| Größe | liefert → braucht | Startannahme |
|---|---|---|
| Schaltfrequenz f | A → B (R_FREQ, Kompensation), D (Filter) | ≈ 370 kHz (27 kΩ) oder ≈ 510 kHz (33 kΩ) |
| Max. Spannung am Buck-Eingang (Surge, Hot-Plug, nach Schutz) | C → A (FET-Klasse, C_IN), B (VIN-Pin, RUN), D (Filter-C) | A rechnet 40-V- und 60-V-FETs parallel |
| Spannung am Buck-Eingang bei Verpolung | C → A, B, D | muss ≥ −0,3 V bleiben (LTC7800) |
| ILIM, R_SENSE, max. Spitzenstrom I_PK,max | A → B (Pins, Regelstrecke), C (Sicherung/Begrenzung), D (Leiterbahnen) | ILIM = INTVCC, R_SENSE ≈ 10 mΩ, I_PK,max ≈ 5,7 A (Begründung A4) |
| Max. Eingangsstrom (Nennlast / Überlast bis Strombegrenzung) | A → C, D | 1,72 A / ≈ 3,0 A |
| C_IN (effektive Kapazität, ESR) | A → C (Hot-Plug), D (Filter, Stabilität) | ≈ 30 µF effektiv, Keramik |
| L (Wert, DCR) | A → B (Regelstrecke, Kurzschluss) | 15–22 µH |
| C_OUT (effektiv, ESR) | B → A (Rippel) | ≈ 30–50 µF effektiv |
| PGOOD-Signal | B → D (LED) | Open Drain, 100 kΩ an INTVCC (wie Fig. 11–16) |
| Filter/Dämpfungs-Elko vor dem Buck | D → A (Rippelstromaufteilung), C (Hot-Plug) | – |
| Kupferfläche/Wärmeabfuhr für FETs, Spule, R_SENSE | A → D | – |
| Verluste je Bereich (mW bei 22/24/26 V, 3 A) | A, B, C → D (Gesamtwirkungsgrad) | Budget §5 |
| Lagenaufbau, Abstände, Platinengröße | D → alle | 4 Lagen, 1 oz, JLCPCB |

---

## 8 Arbeitsweise

- Jede Person ist für ihren Bereich **komplett** zuständig: rechnen, Bauteile suchen, simulieren, eigene Stücklistenzeilen, eigene Dokumentation.
- **Entscheidungen:** Die zuständige Person entscheidet. Ist ein anderer Bereich betroffen (§7): 1–3 Optionen mit Zahlen (Verlust in mW, Kosten, Platz, Risiko) in die Gruppe, dann entscheidet die zuständige Person oder die Gruppe. Ergebnis als Zeile in §9 eintragen, damit alle KIs den aktuellen Stand kennen.
- **Stückliste:** jede Person im Format `Stueckliste_Vorlage.csv`; der Group Leader führt alles zusammen und prüft das Budget.
- **Referenzbezeichner:** A 100–199, B 200–299, C 300–399, D 400–499 (z. B. Q101, U201, F301, J401) → keine Doppelungen beim Zusammenführen.
- **Rechnungen:** vollständige Herleitung; Einheiten in jedem Schritt; jeder Datenblattwert mit Seite und Revision; Worst Case mit Min/Max-Werten statt nur typisch; Plausibilitätsprüfung am Ende. Verluste immer in mW.
- **Simulation:** vor allem Funktionsnachweis und Reserven (Stabilität, Schutz, Ströme, Temperaturen). Simulierte Wirkungsgrade sind Obergrenzen, kein Feintuning um einzelne mW (§1a).
- **Austausch:** GitHub und WhatsApp; alle Dateitypen erlaubt (.asc, .raw, PDFs, Modelle). Technische Grenze: GitHub lehnt **einzelne Dateien über 100 MB** ab → große .raw weglassen, mit `.save` auf benötigte Knoten verkleinern oder Git LFS benutzen.
- **Ergebnis je Bereich** (wird später direkt zur Abgabe zusammengefügt):
  1. Wertetabelle aller Bauteile des Bereichs.
  2. Rechnung mit Herleitung → „Calculation of the part dimensions".
  3. Auswahlbegründung mit Alternativen und Datenblattwerten → „Documentation of component dimensioning".
  4. Simulationsdateien und Ergebnisse (Vergleich mit Rechnung).
  5. Stücklistenzeilen.

---

## 9 Entscheidungen bisher

| Nr | Entscheidung | Grund |
|---|---|---|
| 1 | Bananenbuchsen statt Stiftleisten | vom Prof erlaubt, passt zum Labornetzteil |
| 2 | Status-LED zeigt PGOOD | Gruppe |
| 3 | EMV-Schutz differenziell auslegen; Gleichtakt nur über Layout | Annahme, beim Prof bestätigen |
| 4 | Vorläufig 4 Lagen, JLCPCB | Masselage für EMV und Schleifen; Preis offen |
| 5 | Ergebnisse der früheren KI (Dateien mit Präfix `altKI_`) nur als Gegenprobe | ungeprüft, teils widersprüchlich |
| 6 | Arbeit in Bereichen A–D, jeder mit voller Zuständigkeit; Zeitplan wird am Ende zusammengestellt | Gruppe |
| 7 | Sichere Funktion vor Wirkungsgrad; Optionen mit < 50 mW Unterschied gelten als gleich (§1a) | Prof bewertet vor allem, dass es funktioniert; der echte Wirkungsgrad hängt am selbst gemachten Layout |
| 8 | Layout macht die Gruppe selbst; die Bereiche liefern Vorgaben, Reserven und Bestückungsoptionen (§5a) | Gruppe |

---

## 10 Offene Fragen

| Nr | Frage | an |
|---|---|---|
| F1 | Surge/Burst nur differenziell, nicht gegen Erde? | Prof |
| F2 | Ist „Spannungsreserve 5–10 ×" wirklich eine Vorgabe? | Prof |
| F3 | Sind Reihen-/Parallelschaltungen von E12-Widerständen erlaubt? | Prof |
| F4 | Grenzwertklasse für Emissionen (Annahme Klasse B) | Prof |
| F5 | Wer übernimmt A, B, C, D? | Gruppe |
| F6 | Semesterende / Abgabetermin | Prof |
| F7 | Reicht die Strombegrenzung des Controllers (cycle-by-cycle mit Foldback) als Überstromschutz am Ausgang (R13), oder ist ein eigenes Schutzbauteil (eFuse, PTC, Sicherung) gefordert? | Prof |

---

## 11 Material im Repository

Ordnerstruktur und Arbeitsregeln: `README.md` und `AGENTS.md` im Hauptordner.
- `01_Quellen/01_Quellen_ApplicationNotes.md` – Application Notes, Tools, Referenzdesigns und Bauteil-Datenblätter (Q01…Q72), PDFs im selben Ordner.
- `00_Projekt/WS2026_Aufgabenstellung_V1_2.pdf` – Aufgabe.
- `01_Quellen/Q01_ADI_LTC7800_Datenblatt_RevF.pdf` – LTC7800-Datenblatt Rev. F.
- `02_Modelle/` – Herstellermodelle (Würth WE-XHMI, WE-CMB, WE-TVSP; FET- und Diodenmodelle), ADI-Referenzschaltungen, KiCad-Bibliotheken.
- Dateien mit Präfix `altKI_` – Arbeit einer früheren KI-Sitzung (Simulationen, Rechnungen, Stückliste), ungeprüft, nur als Gegenprobe.
  - **Bekannte Probleme:** zwei widersprüchliche Stände (z. B. R8 4,7 kΩ gegen 4,32 kΩ); Budget überschritten (≈ 67–125 €); η = 98 % gilt nur für die Buck-Stufe in der Simulation; Lastsprung-Ergebnis ±0,91 V passt nach ΔV ≈ ΔI / (2π · f_c · C_OUT) zu einer Durchtrittsfrequenz von nur ≈ 10 kHz, nicht zu den dort angegebenen 21–48 kHz.
