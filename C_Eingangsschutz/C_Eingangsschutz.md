# Bereich C – Eingangsschutz

Für Person C und ihre KI. Vorher `00_Projektkontext.md` lesen (Regeln, Prioritäten §1a, Lastfälle §3, LTC7800-Grenzen §4, Schnittstellen §7). Quellen-Kürzel Q.. siehe `01_Quellen_ApplicationNotes.md`.

## Auftrag
Die Schutzkette zwischen Eingangsbuchse und Eingangsfilter auslegen: **Verpolung, Überstrom am Eingang, Surge 1 kV, Burst 2 kV (Klemmung), Hot-Plug**. Ziele in dieser Reihenfolge:
1. Der Buck sieht in keinem Lastfall eine unzulässige Spannung.
2. Nach Surge, Burst, Verpolung oder Überstrom ist die Platine möglichst ohne Teiletausch weiterbetreibbar.
3. Einfach: wenige Bauteile, gut lötbar, verständlich.
4. Möglichst kleiner Dauerverlust im Strompfad.

Der Schutz darf selbst keine Fehlerquelle werden (Fehlauslösung, Schwingen, schwer lötbar). Bei gleicher Schutzwirkung gewinnt die einfachere Lösung.

## Bauteile von C (je nach Konzept)
| Ref | Funktion |
|---|---|
| F301 | Sicherung oder PTC (falls gewählt) |
| U301, Q301, Q302, R301 | eFuse-, Surge-Stopper- oder Ideal-Dioden-Controller mit FETs und Sense-Widerstand (falls gewählt) |
| Q303 | Verpol-FET (falls separat) |
| D301 | TVS-Diode |
| RV301 | Varistor (falls gewählt) |
| D302, D303, R3xx, C3xx | Gate-Zener, Beschaltung der Controller |

## Wichtigste Quellen für C
| Quelle | Wofür |
|---|---|
| Q01 LTC7800 S. 2, 21 | Absolutwerte; Fehlerkonzept „Crowbar löst Eingangssicherung aus" |
| Q24 TI „Basics of Ideal Diodes" | Verpolschutz: Schottky, P-FET, N-FET, Controller im Vergleich |
| Q25 TI „Basics of eFuses", Q27 TPS2663, Q17 MAX17613A | integrierte Schutz-ICs |
| Q14, Q15 (LTC4364), Q18 (LTC4380), Q16 (LTC4359) | Surge-Stopper, Ideal-Diode, SOA, Timer |
| Q34 Würth ANP143, Q26 TI SLVA711 | TVS-Auswahl, Burst- und Surge-Prüfaufbau |
| Q43 Littelfuse Fuseology, Q44 Littelfuse DC-Eingang | Sicherungsauswahl, Schutzkette |
| Q08 AN-88, Q09 | Hot-Plug, Fehler am Labornetzteil |
| Q42 Nexperia AN11158 | FET-SOA lesen |

## Reihenfolge
```
C1 Vorbereitung → C2 Grenzen vom Buck (mit A) → C3 Lastfälle als Modelle
C4 Verpolschutz-Optionen ┐
C5 Überstrom-Optionen    ├─► C7 Anordnung, Varianten, Bewertung → Entscheidung in der Gruppe
C6 Klemm-Optionen        ┘
C8 Dimensionierung → C9 Hot-Plug → C10 Simulationen ──(Grenze verletzt?)──► zurück zu C7/C8 → C11 Stückliste und Übergabe
```
C4–C6 sind Optionskataloge. Entschieden wird erst in C7, weil die Teile zusammenpassen müssen (manche ICs decken mehrere Funktionen ab).

---

## C1 Vorbereitung
- LTC7800 S. 2 (VIN 65 V, BOOST 71 V, SW −5…65 V absolut), S. 21 (Crowbar → Eingangssicherung).
- EN 61000-4-5 (Surge) und EN 61000-4-4 (Burst): Generator-Ersatzschaltbild, Einkopplung, Polaritäten (Q26 erklärt beide Prüfaufbauten).
- AN-88 (Q08) und Q09 (Hot-Plug).

## C2 Grenzen, die der Buck vorgibt (mit A)
- **Spannung am Buck-Eingang** ≤ kleinster Wert aus: LTC7800 60 V Betrieb; V_DS der Buck-FETs minus Reserve (Vorschlag ≤ 80 %: ≈ 32 V bei 40-V-FETs, ≈ 48 V bei 60-V-FETs); Nennspannung C_IN; Sperrspannung D101.
- **Verpolung:** am LTC7800-VIN nie unter −0,3 V (S. 2). Ohne Schutz fließt Strom über die Body-Dioden von Q101/Q102.
- **Ströme:** Nennlast I_IN ≈ 1,72 A bei 22 V. Überlast bis zur Buck-Strombegrenzung, Beispiel mit der Startannahme aus 00 §7 (ILIM = INTVCC, R_SENSE = 10 mΩ): I_PK,max = 57 mV / 10 mΩ = 5,7 A → Ausgangsstrom ≈ 5,7 A − 0,45 A = 5,25 A → P_OUT ≈ 63 W → I_IN ≈ 63 W / (0,95 · 22 V) ≈ 3,0 A. Echten Wert von A übernehmen. Dazu der Einschaltstrom (C_IN, Elko von D, Soft-Start von B).

## C3 Lastfälle als LTspice-Modelle
- **Surge:** Kombinationswellen-Generator nach EN 61000-4-5 (Leerlauf 1,2/50 µs, Kurzschluss 8/20 µs, 2 Ω), Einkopplung Leitung–Leitung über 18 µF, Entkopplung zum Netzteil. **Erst den Generator allein prüfen** (Leerlaufspannung und Kurzschlussstrom), dann anschließen. Beide Polaritäten.
- **Burst:** 2 kV, 5/50 ns an 50 Ω, Einkopplung 33 nF; Einzelimpuls und Paket.
- **Verpolung:** −26 V dauerhaft.
- **Hot-Plug:** Netzteil 26 V, Leitung ≈ 1 µH und 50–100 mΩ (Annahme), Schalter schließt; C_IN von A, Elko von D.
- **Überstrom:** Kurzschluss direkt am Buck-Eingang; Crowbar-Fall (Q101 durchlegiert, Q102 dauerhaft an).
- Modelle: Würth TVS/Varistor (teils in `02_Modelle/`), ADI-Controller laufen in LTspice; TI-Modelle sind oft PSpice → prüfen.

## C4 Verpolschutz – Optionen (Verlust bei I_IN = 1,72 A; I² = 2,96 A²)
| Option | Dauerverlust | Vorteile | Nachteile | Beispiele |
|---|---|---|---|---|
| Serien-Schottky (V_F ≈ 0,45 V) | ≈ 770 mW (≈ 2 Prozentpunkte) | einfach, sperrt sicher | für Gruppe 3 ungeeignet | – |
| Sicherung + Diode quer („Crowbar") | nur Sicherung | billig | Verpolung zerstört die Sicherung → nicht wiederverwendbar | – |
| P-FET in der Plusleitung | ≈ 30 mW (10 mΩ) | einfach, kein IC | Gate-Zener nötig (V_GS meist max. ±20 V); P-FETs haben mehr R_DS(on) je Fläche; Surge liegt am FET | 60-V-P-FETs in Power-SMD |
| N-FET in der Minusleitung | ≈ 15–30 mW | billigste verlustarme Lösung | Eingangs-Minus ist nicht mehr Platinenmasse (Messung, EMV) | 60-V-N-FET |
| Ideal-Dioden-Controller + N-FET | ≈ I² · R_DS(on) | sehr kleiner Verlust, sperrt auch Rückstrom | IC mit Ladungspumpe | LTC4359 (4–80 V, bis −40 V, Q16), TI LM74700-Q1 |
| Schutz-IC mit eingebautem Verpolschutz | siehe C5 | kombiniert mehrere Funktionen | Kosten, Komplexität | LTC4380 (bis −60 V), LTC4364, MAX17613A (bis −65 V), TPS2663 (mit externem N-FET) |

Quelle Q24 vergleicht genau diese Möglichkeiten.

## C5 Überstromschutz am Eingang – Optionen
| Option | Dauerverlust bei 1,72 A | Nach Fehler | Vorteile | Nachteile | Beispiele |
|---|---|---|---|---|---|
| Schmelzsicherung SMD | 30–60 mW (10–20 mΩ) | tauschen | einfach, billig, passt zum Crowbar-Konzept des LTC7800 | nicht wiederverwendbar; I²t gegen Einschaltstrom prüfen | Littelfuse NANO2, Schurter, Bel Fuse |
| PTC (rückstellend) | 90–150 mW (30–50 mΩ kalt) | erholt sich | wiederverwendbar, billig | träge; Widerstand nach Auslösung erhöht; Haltestrom temperaturabhängig | Littelfuse PolySwitch, Bourns Multifuse |
| eFuse mit integriertem FET | TPS2663 (31 mΩ): ≈ 92 mW · MAX17613A (130 mΩ): ≈ 385 mW | Auto-Retry | genau und schnell; dazu OV/UV, oft Verpolschutz; TPS2663 laut TI für IEC 61000-4-5 ausgelegt | Kosten; Verlust je nach R_ON; MAX17613A max. 3 A Grenze | TPS2663 (Q27), MAX17613A (Q17) |
| Controller + externer FET + Sense-Widerstand | ≈ 45–60 mW (FET 5–10 mΩ + 10 mΩ Shunt) | Auto-Retry | sehr kleiner Verlust, FET frei wählbar | mehr Bauteile; FET-SOA prüfen | LTC4380 (Q18), LTC4364 (Q14, Q15) |

Quellen: Q43 (Sicherung), Q25 (eFuse).

## C6 Surge- und Burst-Klemmung – Optionen
Surge-Strom grob: I_peak ≈ (1000 V − V_C) / 2 Ω, z. B. V_C = 45 V → ≈ 480 A (8/20 µs).

| Option | Vorteile | Nachteile | Beispiele |
|---|---|---|---|
| große TVS allein (SMC/SMD-Klasse, 1,5–5 kW) | ein Bauteil, kein Dauerverlust, schnell | muss ≈ 480 A bei 8/20 µs können (Rating im Datenblatt prüfen); V_C bei hohem Strom deutlich über V_BR | Littelfuse SMCJ/SMDJ/5.0SMDJ, Würth WE-TVS, Vishay/Bourns SMCJ |
| Varistor + Längsimpedanz + TVS (zweistufig) | Varistor nimmt die Energie, TVS klemmt fein | Varistor altert und ist groß (THT-Scheibe → 4-mm-Sperrzone); mehr Teile | Würth WE-VD, TDK SIOV, Littelfuse |
| Surge-Stopper (FET regelt ab) + TVS davor | Buck sieht nur die Klemme (LTC4380 z. B. 31,5 V) → 40-V-Buck-FETs möglich | FET-SOA, mehr Teile | LTC4380, LTC4364 |
| eFuse mit Überspannungsklemme + TVS davor | ein IC für Überstrom, Klemme, Verpolung | Kosten; TVS vor dem IC trotzdem nötig (TPS2663: 67 V absolut) | TPS2663 (35/39-V-Varianten) |

- **Burst:** TVS + kleine Keramik direkt an der Buchse + Filter (D). Der Burst ist energiearm, entscheidend sind kurze Wege und HF-taugliche Kondensatoren (Q26, Q34).
- Quellen: Q34, Q26, Q14, Q15.

## C7 Anordnung, Varianten, Bewertung
**Regeln für die Anordnung:**
- Sicherung (falls vorhanden) ganz vorne: TVS fallen meist niederohmig aus → die Sicherung verhindert Überhitzung.
- TVS so nah wie möglich an der Buchse, vor allen Halbleitern, die sie schützen soll.
- Unidirektionale TVS vor dem Verpolschutz leitet bei Verpolung und schließt das Netzteil kurz → bidirektional wählen oder hinter den Verpolschutz setzen (dann sieht der Verpol-FET den Surge).

**Varianten:**

| Variante | Kette | Buck-FETs | Charakter |
|---|---|---|---|
| A – passiv | Sicherung/PTC → TVS (bidirektional) → Verpol-FET → Filter (D) → Buck | 60 V | einfach, wenige ICs; Sicherung muss evtl. getauscht werden |
| B – aktiv | TVS → Surge-Stopper mit Verpolung und Überstrom (LTC4380/LTC4364) → Filter → Buck | 40 oder 60 V | robust und wiederverwendbar; mehr Teile |
| C – eFuse | TVS → eFuse (TPS2663 + Verpol-FET oder MAX17613A) → Filter → Buck | 60 V | ein IC, wiederverwendbar; Verlust hängt am R_ON |

Je Variante: höchste Spannung am Buck-Eingang in jedem Lastfall (Abschätzung, dann C10); Dauerverlust Schutzkette plus Auswirkung auf die Buck-FETs (A6); Kosten; Fläche (THT → 4-mm-Sperrzone); Wiederverwendbarkeit; Lötbarkeit.

**Bewertungsmatrix** (Gewichte legt die Gruppe fest; Vorschlag nach 00 §1a): sichere Funktion/Robustheit 35 %, Einfachheit (Bauteilzahl, Löten, Inbetriebnahme) 20 %, Kosten 20 %, Wirkungsgrad 15 %, Platz 10 %. Jede Zelle mit einer Zahl. 1–3 Varianten in die Gruppe, dann entscheiden.

## C8 Gewählte Lösung dimensionieren
- **TVS:** V_RWM ≥ 26 V + Reserve (Netzteil falsch eingestellt?); V_BR,min > V_RWM; V_C beim tatsächlichen Surge-Strom (aus C10) ≤ Grenze aus C2; 8/20-µs-Pulsrating (steht nur 10/1000 µs im Datenblatt: Kurve „Peak Pulse Power vs Pulse Width").
- **Varistor:** Gleichspannung ≥ 26 V + Reserve; Klemmspannung bei Pulsstrom; Energie- und Stromrating (8/20 µs); Alterung (Derating-Kurve).
- **Längsimpedanz** zwischen Varistor und TVS (oft die Filterspule von D): Energieaufteilung; Sättigung beim Surge-Strom (mit D abstimmen, pessimistisch rechnen).
- **Verpol-FET:** V_DS ≥ höchste Spannung an seiner Stelle; Gate-Zener; R_DS(on) bei der tatsächlichen V_GS; SOA bei Surge (Q42).
- **Sicherung:** Nennstrom gegen 1,72 A mit Temperatur-Derating; Schmelz-I²t größer als I²t des Einschaltstroms; Ausschaltvermögen, Nennspannung; löst im Crowbar-Fall sicher aus (Q43).
- **eFuse/Controller:** Grenzstrom zwischen größtem zulässigem Eingangsstrom (Überlast bis zur Buck-Grenze) und dem, was Stecker, Leiterbahnen und FETs aushalten; Klemmspannung über 26 V + Toleranz; Timer/Auto-Retry; FET-SOA (P²t-Methode im Controller-Datenblatt).

## C9 Hot-Plug
| Option | Vorteile | Nachteile |
|---|---|---|
| TVS begrenzt das Überschwingen | ohnehin vorhanden | TVS wird bei jedem Einstecken belastet (meist unkritisch) |
| Dämpfungs-Elko am Eingang (mit D) | verhindert das Überschwingen fast ganz (Q08) | Größe, Lebensdauer |
| eFuse/Stopper mit Einschaltstrombegrenzung | kein Überschwingen, kleiner Einschaltstrom | nur bei Variante B/C |

Ergebnis an A (C_IN-Nennspannung) und D.

## C10 Simulationen
| Fall | Bedingung | Bestanden, wenn |
|---|---|---|
| Surge 1 kV / 2 Ω | auf 24 V, positiv und negativ | Buck-Eingang ≤ Grenze aus C2; alle Bauteile innerhalb ihrer Puls-Ratings (Strom, Energie, SOA) |
| Burst 2 kV | Einzelimpuls und Paket | Buck-Eingang ≤ Grenze; keine Fehlauslösung |
| Verpolung | −26 V dauerhaft | Buck-Eingang ≥ −0,3 V; kein Bauteil überlastet |
| Hot-Plug | Leitung ≈ 1 µH, 26 V | Überschwingen ≤ Grenze |
| Überstrom | Kurzschluss am Buck-Eingang; Crowbar-Fall | Abschaltung oder Begrenzung wie gerechnet |
| Normalbetrieb | 22–26 V, 3 A | Dauerverlust wie gerechnet |

## C11 Stückliste und Übergabe
- Zeilen im Format `Stueckliste_Vorlage.csv` (Bereich C, Referenzen 300–399), je Teil 2 Händler mit Datum.
- An A, B, D: höchste Spannung am Buck-Eingang je Lastfall; Spannung bei Verpolung.
- An D: Verluste C, Platzbedarf, THT-Teile (Sperrzone 4 mm), Knoten mit hohen Transientenspannungen (Abstände im Layout), Längsimpedanz-Bedarf.

---

## Fertig, wenn
Konzept entschieden, alle Bauteile mit Teilenummer und 2 Händlern festgelegt, Rechnungen und alle Simulationen aus C10 dokumentiert, Grenzwerte an A, B, D übergeben.

## Typische Fehler
- 10/1000-µs-Rating der TVS mit 8/20 µs verwechseln.
- Unidirektionale TVS vor dem Verpolschutz.
- Nur eine Surge-Polarität simulieren; Generatormodell nicht allein geprüft.
- Sicherungs-I²t gegen den Einschaltstrom vergessen.
- Gate-Source-Spannung von P-FETs bei Surge überschritten.
- Spulensättigung beim Surge ignoriert.

## Gegenprobe
Frühere KI: `C04_Surge_Burst/altKI_Ergebnisse_Surge.md`, `C04_Surge_Burst/altKI_Ergebnisse_Burst.md`, `C05_Variantenvergleich/altKI_IC_Datenblatt_LTC4364.md` (LTC4364 + Gleichtaktdrossel + Varistor + TVS + zwei 22-µH-Spulen) – nur zum Vergleichen, lag über dem Budget.

## Startprompt für die KI
> Du hilfst mir bei Bereich C (Eingangsschutz) unseres Studienprojekts: nicht isolierter Buck 22–26 V → 12 V / 3 A mit LTC7800, Gruppenziel höchster Wirkungsgrad, aber sichere und einfache Funktion hat Vorrang (00 §1a), Budget 100 € netto für alles. Lies `00_Projektkontext.md`, `01_Quellen_ApplicationNotes.md` und `C_Eingangsschutz.md` vollständig und halte dich an die Regeln (Widerstände E12, Keramik nur X7R/C0G, SMD ≥ 0603, jedes Teil bei 2 europäischen Händlern mit Datum). Rechne mit vollständigen Herleitungen und Einheiten, gib zu jedem Datenblattwert Seite und Revision an, rechne Worst Case. Arbeite C1–C11 in der angegebenen Reihenfolge ab; zeig mir für Verpolung, Überstrom und Klemmung die Optionen mit Trade-offs und Zahlen (Verlust in mW, Kosten, Platz, Robustheit) und hilf mir, daraus 1–3 Varianten für die Gruppe zu machen. Am Ende brauche ich: Konzept mit Begründung, Wertetabelle, Rechnung, Simulationsergebnisse (Surge, Burst, Verpolung, Hot-Plug, Überstrom) und Stücklistenzeilen im Format `Stueckliste_Vorlage.csv`.
