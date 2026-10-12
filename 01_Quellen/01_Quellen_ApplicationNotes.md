# 01 – Quellen: Application Notes, Tools, Referenzdesigns

Für alle Bereiche. Die Bereichsdateien verweisen mit den Kürzeln Q01… auf diese Liste. Stand der Links: 12.10.2026.
Hinweis: Viele Application Notes sind für andere ICs geschrieben. Die **Methode** (Formeln, Vorgehen, Layoutregeln) ist übertragbar, die Bauteilwerte nicht.

**Lokale Kopien in diesem Ordner `01_Quellen/`** (Dateiname beginnt mit der ID, z. B. `Q05_ADI_AN-136_PCB_Layout.pdf`):
- Schon vorhanden (umbenannt 12.10.2026): `Q01_…`, `Q02_ADI_LTpowerCAD_Five_Simple_Steps.pdf`, `Q03`–`Q08`, `Q10`, `Q12`, `Q14`, `Q16`–`Q18`, `Q20`–`Q27`, `Q30`–`Q35`, `Q40`–`Q43`, `Q51`–`Q59`, `Q60`–`Q72` (siehe Abschnitte unten).
- Noch nicht lokal: Q15 (LT-Journal-Artikel als PDF, Link in der Tabelle).
- Nur online (Webseiten, Tools, Buch): Q09, Q11, Q13, Q14 (Artikel), Q36, Q44–Q50.

## Analog Devices / Linear Technology (Hersteller des LTC7800)

| ID | Quelle | Wofür | Bereich | Link |
|---|---|---|---|---|
| Q01 | LTC7800-Datenblatt Rev. F (05/2017) | alle Formeln, Grenzwerte, Referenzschaltungen Fig. 11–16, Layout-Checkliste | alle | https://www.analog.com/en/products/ltc7800.html (lokal: `Q01_ADI_LTC7800_Datenblatt_RevF.pdf`) |
| Q02 | LTpowerCAD (Design-Tool) – auf der LTC7800-Seite gibt es ein fertiges Projekt „LTC7800 Project – DC2736A GaN FETs, Rsense, 500kHz" | Bauteilvorschläge, Wirkungsgrad, Regelkreis (Bode), Lastsprung; Export nach LTspice. Gut als Gegenprobe zur Handrechnung | A, B | https://www.analog.com/en/technical-articles/what-is-the-ltpowercad-design-tool-and-how-is-it-different-from-ltspice.html |
| Q03 | Demo Board DC2736A: LTC7800, 30–55 V → **12 V / 20 A, 500 kHz**, GaN-FETs, R_SENSE | nächstliegende 12-V-Referenz: Schaltplan, Stückliste, Layout ansehen (nicht kopieren – andere Spannung, Strom, FETs) | A, B, D | https://www.analog.com/jp/resources/evaluation-hardware-and-software/evaluation-boards-kits/dc2736a.html · Manual: https://www-cce.cldnet.analog.com/media/en/technical-documentation/user-guides/DC2736AF.PDF |
| Q04 | Demo Board DC2786A: LTC7800, 8–40 V → 3,3 V / 10 A | zweite Layout-Referenz mit Si-MOSFETs | A, D | https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/dc2786a.html |
| Q05 | AN-136 „PCB Layout Considerations for Non-Isolated Switching Power Supplies" | Layout: Schaltschleife, Masse, Platzierung | A, D, Layout | https://www.analog.com/en/resources/app-notes/an-136.html |
| Q06 | AN-139 „Power Supply Layout and EMI" | Layout und EMV | D, Layout | https://www.analog.com/en/resources/app-notes/an-139.html |
| Q07 | AN-149 „Modeling and Loop Compensation Design of Switching Mode Power Supplies" | Kleinsignalmodell Strommodus, Kompensation Schritt für Schritt | B | https://www.analog.com/en/resources/app-notes/an-149.html |
| Q08 | AN-88 „Ceramic Input Capacitors Can Cause Overvoltage Transients" | Hot-Plug-Überschwingen mit Keramik-C_IN, Gegenmaßnahmen | A, C, D | https://www-cce.cldnet.analog.com/media/en/technical-documentation/application-notes/an88f.pdf |
| Q09 | Artikel „How NOT to Damage Your Switching Regulator Demo Board" | praktische Fehler beim Einschalten am Labornetzteil | C, Inbetriebnahme | https://www.analog.com/jp/resources/technical-articles/how-not-to-damage-your-switching-regulator-demo-board.html |
| Q10 | Artikel „Switch Mode Power Supply Current Sensing – Part 3: Current Sensing Methods" | R_SENSE gegen DCR-Messung, Vor- und Nachteile | A, B | https://www.analog.com/en/resources/technical-articles/switch-mode-power-supply-current-sensing-part-3-current-sensing-methods.html |
| Q11 | EngineerZone: „How to Generate a Bode Plot for an SMPS in LTspice" | Bode-Diagramm am schaltenden Modell in LTspice | B | https://ez.analog.com/design-tools-and-calculators/ltspice/a/faqs-docs/fd549/generate-a-bode-plot-for-an-smps-in-ltspice-17-1 |
| Q12 | Artikel „Control Loop Simulation Done the Easy Way" | Regelkreis-Simulation | B | https://www.analog.com/en/resources/technical-articles/control-loop-simulation-done-the-easy-way.html |
| Q13 | Analog Dialogue RAQ 193 „Three Options to Optimize the Control Loop of Power Converters" | Wege zur Kompensation (Rechnung, Tool, Messung) | B | https://www.analog.com/en/resources/analog-dialogue/raqs/raq-issue-193.html |
| Q14 | Artikel „Surge Stopper with Ideal Diode Protects Input and Output" (LTC4364) | Surge-Stopper + Verpolschutz, FET-SOA, Timer | C | https://www.analog.com/en/resources/technical-articles/surge-stopper-with-ideal-diode-protects-input-and-output.html |
| Q15 | LT Journal: LTC4364-Artikel (Z. Hou) | Surge-Stopper-Auslegung | C | https://wcm-cce.cldnet.analog.com/media/en/technical-documentation/tech-articles/lt-journal-article/LTJournal-V22N3-03-df-LTC4364-ZhizhongHou.pdf |
| Q16 | Artikel „Low IQ Ideal Diode Controller with Reverse Input Protection" (LTC4359: 4–80 V, Verpolung bis −40 V, externer N-FET) | Verpolschutz mit Ideal-Diode | C | https://www.analog.com/en/resources/technical-articles/low-iq-ideal-diode-controller-with-reverse-input-protection.html |
| Q17 | MAX17613A (4,5–60 V, −65 V Eingang, Strombegrenzung 0,15–3 A einstellbar, OV/UV, Verpolschutz, 130 mΩ) | integrierter Eingangsschutz in einem IC | C | https://www.analog.com/en/products/max17613a.html |
| Q18 | LTC4380 (4–72 V, Surge-Stopper mit externem N-FET, Klemme 31,5 V / 50 V / einstellbar, Überstrom, Verpolung bis −60 V, 8 µA) | Surge-Stopper-Variante | C | https://www.mouser.co.uk/new/analog-devices/adi-ltc4380-stoppers |

## Texas Instruments

| ID | Quelle | Wofür | Bereich | Link |
|---|---|---|---|---|
| Q20 | SNVA538 „Input filter design for switching power supplies" | Eingangsfilter: Dämpfungsbedarf, Middlebrook, Dämpfung | D | https://ti.com/lit/snva538 |
| Q21 | SNVA489 / AN-2162 „Simple Success With Conducted EMI From DC-DC Converters" | leitungsgebundene Störungen verstehen und messen | D | https://ti.com/lit/pdf/snva489 |
| Q22 | SLYT682 „Reduce buck-converter EMI and voltage stress by minimizing inductive parasitics" | Schaltschleife, Masselage, SW-Fläche | A, D, Layout | https://www.ti.com/jp/lit/an/slyt682/slyt682.pdf |
| Q23 | SLUA887 „Bootstrap Circuitry Selection for Half-Bridge Configurations" | C_B, D_B, Bootstrap-Widerstand | A | https://ti.com/lit/SLUA887 |
| Q24 | SLVAE57 „Basics of Ideal Diodes" | Verpolschutz: Schottky, P-FET, N-FET, Controller im Vergleich | C | https://ti.com/lit/SLVAE57 |
| Q25 | SLVA862 „Basics of eFuses" | eFuse gegen diskrete Lösung | C | https://ti.com/lit/SLVA862 |
| Q26 | SLVA711 „IEC 61000-4-x Tests for TI's Protection Devices" | Burst- und Surge-Prüfaufbau, TVS-Auswahl nach V_CL und I_PP | C | https://ti.com/lit/pdf/SLVA711 |
| Q27 | TPS2663 (eFuse 4,5–60 V, 0,6–6 A, 31 mΩ, für IEC 61000-4-5 ausgelegt, Verpolschutz mit externem N-FET) | integrierter Eingangsschutz | C | https://www.ti.com/product/TPS2663 |

## Würth Elektronik

| ID | Quelle | Wofür | Bereich | Link |
|---|---|---|---|---|
| Q30 | ANP005 „EMC Filter for DC/DC Switching Controller optimized" | LC-Eingangsfilter: Aufbau, f_0 ≈ f/10, Dämpfung über ESR, Stabilität | D | https://community.element14.com/products/manufacturers/wuerth-elektronik/w/documents/16832/anp005-emc-filter-for-dc-dc-switching-controller-optimized |
| Q31 | ANP044 „Impact of the layout, components, and filters on the EMC of modern DC/DC switching controllers" | Layout schlägt Filter; keine Klasse-2-MLCC im Filter ohne DC-Bias-Prüfung; Schwingneigung mit Keramik-C_IN | D, Layout | https://www.we-online.com/catalog/media/o109026v410%20AppNotes_ANP044_ImpactOfTheLayoutComponentsAndFiltersOnTheEMCOfModernDCDCSwitchingControllers_EN.pdf |
| Q32 | ANP031 „Determination of the Ideal Power Inductor for Energy-efficient Applications" | AC-Wicklungsverluste, REDEXPERT-Verlustmodell | A | https://community.element14.com/products/manufacturers/wuerth-elektronik/w/documents/3549/anp031-determination-of-the-ideal-power-inductor-for-energy-efficient-applications |
| Q33 | ANP062 „LC Filter Design With MLCCs: Why The Applied Voltage Matters" | DC-Bias: bis zu 80 % Kapazitätsverlust | A, B, D | https://www.we-online.com/components/media/o156393v410%20ANP062a%20EN.pdf |
| Q34 | ANP143 „TVS diodes: basics, function and their applications" | TVS-Kennwerte, Auswahl, Surge-/Burst-Beispiele an DC-Eingängen | C | https://community.element14.com/products/manufacturers/wuerth-elektronik/b/blog/posts/anp143-tvs-diodes-basics-function-and-their-applications |
| Q35 | ANP049 „EMC & efficiency optimization of high power DC/DC converters" | Zielkonflikt EMV ↔ Wirkungsgrad | A, D | https://community.element14.com/products/manufacturers/wuerth-elektronik/b/blog/posts/anp049-emc-efficiency-optimization-of-high-power-dc-dc-converters |
| Q36 | REDEXPERT (Online-Tool) | Spulenverluste (AC/DC), Erwärmung, Kondensator-Daten | A, B, D | https://www.we-online.com/en/support/design-tools/redexpert |

## Weitere Hersteller und Werkzeuge

| ID | Quelle | Wofür | Bereich | Link |
|---|---|---|---|---|
| Q40 | Vishay AN836 „Selection of MOSFETs for DC/DC Synchronous Buck Controllers" | oberer/unterer FET nach Effektivstrom, Thermik, R_DS(on), Gate-Ladung, integrierter Schottky | A | https://www.vishay.com/docs/68952/an836.pdf |
| Q41 | Vishay AN605 „Power MOSFET Basics: Understanding MOSFET Characteristics Associated With The Figure of Merit" | Gütezahl Q_G · R_DS(on) und ihre Grenzen | A | https://www.vishay.com/docs/71933/71933.pdf |
| Q42 | Nexperia AN11158 „Understanding power MOSFET data sheet parameters" | FET-Datenblätter richtig lesen (SOA, Bedingungen) | A, C | https://mouser.com/pdfDocs/AN11158.pdf |
| Q43 | Littelfuse „Fuseology Design Guide" | Sicherungsauswahl: Derating, I²t, Einschaltstrom | C | https://info.littelfuse.com/hubfs/Fuseology%20Design%20Guide.pdf |
| Q44 | Littelfuse „OV/OC Protection of DC Input" | Schutzkette am DC-Eingang | C | https://littelfuse.com/technical-resources_old/application-designs/circuits/protection-dc-input.aspx |
| Q45 | Murata SimSurfing / FAQ DC-Bias | DC-Bias-Kurven von MLCCs | A, B, D | https://www.murata.com/en-eu/support/faqs/products/capacitor/mlcc/char/0016 |
| Q46 | Rohde & Schwarz „Conducted emissions in DC-DC converters – simulation versus measurement" | Emissionen simulieren mit LISN | D | https://www.rohde-schwarz.com/uk/_56279-1125376.html |
| Q47 | JLCPCB Fertigungsmöglichkeiten | Leiterbahn/Abstand/Via-Grenzen | D | https://api.jlcpcb.com/capabilities/Capabilities |
| Q48 | Aisler 4-Layer-Designregeln (Vorgabe der Aufgabe) | Kriech-/Luftstrecken | D | https://community.aisler.net/t/4-layer-1-6mm-enig-design-rules/3733 |
| Q49 | Rechner Strombelastbarkeit von Leiterbahnen (Beispiel) | Leiterbahnbreiten | D | https://www.protoexpress.com/resources/current-carrying-capacity-calculator/ |
| Q50 | Fachbuch: Erickson/Maksimović „Fundamentals of Power Electronics", Kapitel Input Filter Design | Middlebrook-Kriterium, optimale Dämpfung | D | (Bibliothek) |

## Ergänzt 12.10.2026: zusätzliche lokale Dateien (Q51–Q59)

| ID | Quelle | Wofür | Bereich | Lokale Datei |
|---|---|---|---|---|
| Q51 | ADI „Switch Mode Power Supply Current Sensing – Part 1: The Basics" | Grundlagen Strommessung im Schaltregler | B | Q51_ADI_Current_Sensing_Part1_Basics.pdf |
| Q52 | ADI „Switch Mode Power Supply Current Sensing – Part 2: Where to Place the Sense Resistor" | Platzierung R_SENSE, welcher Strom gemessen wird | A, B | Q52_ADI_Current_Sensing_Part2_Sense_Resistor.pdf |
| Q53 | TI SLUA618A „Fundamentals of MOSFET and IGBT Gate Driver Circuits" | Gate-Treiber-Auslegung, parasitäre Einflüsse | A | Q53_TI_SLUA618_MOSFET_IGBT_Gate_Driver.pdf |
| Q54 | TI SLUP170 „Estimating MOSFET Parameters from the Data Sheet" (Anhang A) | Ciss/Crss/Qg, Miller-Plateau, dv/dt aus dem Datenblatt ableiten | A | Q54_TI_SLUP170_MOSFET_Parameter_Schaetzung.pdf |
| Q55 | TI SLYT664 „MOSFET power losses and how they affect power-supply efficiency" | Verlustarten des MOSFETs, Wirkungsgrad | A | Q55_TI_SLYT664_MOSFET_Verluste.pdf |
| Q56 | TI SLYT746 „The Essential Collection of DC/DC Buck Switching Regulator Technical Documentation" | Übersicht TI-Buck-Dokumentation (Sammelkatalog, Verweise) | A, B | Q56_TI_SLYT746_Buck_Regler_Ueberblick.pdf |
| Q57 | TI SLYY154 „An Engineer's Guide to Current Sensing" (e-book) | Strommessung: Methoden und Schaltungen | A, B | Q57_TI_SLYY154_Current_Sensing_eBook.pdf |
| Q58 | TI SLYY168 „11 Ways to Protect Your Power Path" | Verpolschutz, Lastschalter, Schutzkonzepte am Eingang | C | Q58_TI_SLYY168_Power_Path_Schutz.pdf |
| Q59 | TI SNVA886 „Reduce Conducted EMI in Automotive Buck Converter Applications" | leitungsgebundene EMV beim Buck, Filter- und Layoutmaßnahmen | D | Q59_TI_SNVA886_Conducted_EMI_Automotive_Buck.pdf |

**Duplikate und Gleichheiten:** `ltc4364-1-4364-2.pdf` war identisch mit Q14 (gleiche MD5) und wurde gelöscht. Von den beiden Versionen von ANP049 blieb die offizielle Würth-Fassung `o148945v410 ANP049a-1 DE` als **Q35** erhalten, die ältere Kopie `anp049a_de_emv__…` wurde gelöscht.

## Ergänzt 12.10.2026: Bauteil-Datenblätter (ursprünglich aus dem Ordner der früheren KI) (Q60–Q72)

Herstellerdatenblätter der Bauteile aus der Stückliste der früheren KI (`03_Stueckliste/altKI_BOM_Stueckliste.csv`, vorläufig, ungeprüft). Abgeglichen mit `02_Bauteilkandidaten.md` am 12.10.2026, alle Q60–Q72 sind dort jetzt mit lokalem Verweis eingetragen.

| ID | Bauteil | Einsatz laut BOM | Bereich | Lokale Datei |
|---|---|---|---|---|
| Q60 | Würth WE-XHMI 1510, 74439370100 – 10,4 µH, 7,04 mΩ max | L3 Buck-Speicherdrossel | A | Q60_WE-XHMI_74439370100_Datenblatt.pdf |
| Q61 | Würth WE-XHMI 1510, 74439370220 – 22 µH, 13,3 mΩ, 8 A | L1 Eingangsdrossel, L2 Drossel nach Stopper | C, D | Q61_WE-XHMI_74439370220_Datenblatt.pdf |
| Q62 | Würth WE-CMB NiZn, 744841414 – 14 µH, 4 A, THT | CMC1 Gleichtaktdrossel | D | Q62_WE-CMB_744841414_Datenblatt.pdf |
| Q63 | Würth WE-VD, 820542501 – 39 V (U_DC 31 V), 1 kA, 9,4 J | RV1 Varistor | C | Q63_WE-VD_820542501_Datenblatt.pdf |
| Q64 | Würth WE-TVSP, 824551281 – 28 V bidirektional, 3 kW, SMC | D_TVS | C | Q64_WE-TVSP_824551281_Datenblatt.pdf |
| Q65 | Würth WCAP-ASLI, 865080543009 – 47 µF, 35 V | C_BULK (4×) | C, D | Q65_WCAP-ASLI_865080543009_Datenblatt.pdf |
| Q66 | Würth WCAP-CSGP, 885012207098 – 100 nF, 50 V, X7R, 0805 | C_SS Soft-Start | B | Q66_WE-MLCC_885012207098_X7R.pdf |
| Q67 | Würth WCAP-CSGP, 885012207103 – 1 µF, 50 V, X7R, 0805 | C_INTVCC2 | B | Q67_WE-MLCC_885012207103_X7R.pdf |
| Q68 | Würth WCAP-CSGP, 885012209073 – 10 µF, 50 V, X7R, 1210 | C_INTVCC1 | B | Q68_WE-MLCC_885012209073_X7R.pdf |
| Q69 | Würth WL-SMCW, 150060GS75000 – LED grün 0603 | D_LED Status-LED | D | Q69_WE_150060GS75000_LED_Datenblatt.pdf |
| Q70 | Infineon BSZ097N04LS G – 40 V OptiMOS 3 | Q1 High-Side und Q2 Low-Side | A | Q70_Infineon_BSZ097N04LSG_MOSFET.pdf |
| Q71 | Nexperia PMEG4030ER – 40 V / 3 A Schottky | D_BOOT Bootstrap, D_SYNC (optional) | A | Q71_Nexperia_PMEG4030ER_Schottky.pdf |
| Q72 | Vishay WSL (Familien-DB) – WSL2512R0100FEA, 10 mΩ 1 % 1 W | RS1/RS2 Buck-R_SENSE (parallel 5 mΩ), RSNS Stopper | A, B, C | Q72_Vishay_WSL_Shunt_Datenblatt.pdf |

**Doppelte Dateien:** Die Datenblätter LTC7800, LTC4364 und 74439370100 lagen mehrfach vor und sind hier nur einmal abgelegt. KiCad- und LTspice-Modelle liegen in `02_Modelle/`.

