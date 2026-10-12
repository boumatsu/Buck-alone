# Bereich D – Eingangsfilter, Anschlüsse, Status-LED, Platinenrahmen, Zusammenführung

Für Person D (Vorschlag: Group Leader) und ihre KI. Vorher `00_Projektkontext.md` lesen (Regeln, Prioritäten §1a, Lastfälle §3, Randwerte §5, Layout §5a, Schnittstellen §7). Quellen-Kürzel Q.. siehe `01_Quellen_ApplicationNotes.md`.

## Auftrag
1. Eingangsfilter zwischen Schutz (C) und Buck (A): leitungsgebundene Störungen dämpfen, stabil mit dem Wandler zusammenarbeiten, Burst-Anteile abfangen.
2. Stecker, Messpunkte und Status-LED festlegen.
3. Platinenrahmen für das Layout vorbereiten (Lagen, Regeln, Größe, Preis). **Das Layout macht die Gruppe selbst**; D liefert nur den Rahmen.
4. Zusammenführen: Gesamt-Stückliste, Budget, Gesamtwirkungsgrad, Prüfung der Schnittstellen.

## Bauteile von D
| Ref | Funktion |
|---|---|
| L401 | Filterspule (Würth) |
| C401…C40x | Filterkondensatoren, dazu ein kleiner HF-Kondensator direkt an der Buchse |
| C410 (+R410) | Dämpfungszweig: Elko mit passendem ESR oder R-C-Glied |
| L402 (optional) | Gleichtaktdrossel (Würth), ggf. nur als unbestückter Footprint |
| J401, J402 | Eingang: Bananenbuchsen rot/schwarz |
| J403, J404 | Ausgang: Bananenbuchsen rot/schwarz |
| TP401… | Messpunkte |
| Q401, D401, R401… | LED-Schaltung |
| R4xx (optional) | Injektionswiderstand für die Regelkreismessung |
| H401…H404 | Befestigungslöcher |

## Wichtigste Quellen für D
| Quelle | Wofür |
|---|---|
| Q30 Würth ANP005, Q20 TI SNVA538, Q50 Erickson | Eingangsfilter: Aufbau, Dämpfung, Middlebrook-Stabilität |
| Q31 Würth ANP044, Q35 Würth ANP049 | Einfluss von Layout, Bauteilen und Filter auf die EMV |
| Q21 TI AN-2162 (SNVA489), Q46 Rohde & Schwarz | leitungsgebundene Emissionen verstehen und simulieren |
| Q33 Würth ANP062, Q45 Murata SimSurfing | DC-Bias der Filterkondensatoren |
| Q05 AN-136, Q06 AN-139, Q22 TI SLYT682 | Layoutregeln (Rahmen für die Gruppe) |
| Q03/Q04 Demo Boards | Layout-Beispiele des Herstellers |
| Q47 JLCPCB, Q48 Aisler, Q49 Leiterbahn-Rechner | Fertigungsregeln, Abstände, Leiterbahnbreiten |

## Reihenfolge
```
D1 Vorbereitung → D2 Stecker → D3 Platinenrahmen (Lagen, Hersteller, Größe, Preis)
D4 Filterkonzept (braucht f und C_IN von A, Schutzkette von C) → D5 Filterbauteile
D6 Status-LED (braucht PGOOD von B) → D7 Messpunkte und Stellschrauben einsammeln
D8 Zusammenführung (laufend, sobald Stücklisten kommen) → D9 Simulationen → D10 Layout-Vorgaben für KiCad
```
D2, D3 und D6 können sofort beginnen; D4/D5 mit den Startannahmen aus 00 §7.

---

## D1 Vorbereitung
ANP005 (Q30) und SNVA538 (Q20) für das Filter; ANP044 (Q31), AN-136 (Q05), AN-139 (Q06) für Layout und EMV; JLCPCB-Fähigkeiten (Q47) und Aisler-Regeln (Q48).

## D2 Stecker
| Option | Vorteile | Nachteile |
|---|---|---|
| **4-mm-Bananenbuchsen für Leiterplattenmontage (vom Prof erlaubt)** | passt direkt zum Labornetzteil, mechanisch robust, hoher Nennstrom | THT → 4 mm Sperrzone zu SMD; Preis ≈ 1 € je Stück (prüfen) |
| zusätzlich 2,54-mm-Stiftleiste parallel (Originalvorgabe) | flexibel, billig | mehrere Pins parallel für 3 A (Strom je Pin laut Datenblatt); mechanisch empfindlicher; ebenfalls THT |

- Anforderungen Bananenbuchse: Nennstrom ≥ 5 A (Überlast ≈ 3 A plus Reserve), rot/schwarz, verschraubt, Footprint mit Sperrzone. Beispiel zum Prüfen: Multicomp Pro 24.243.x (von der früheren KI gefunden), weitere Hersteller vergleichen; 2 Händler.

## D3 Platinenrahmen: Lagen, Hersteller, Größe, Preis
**Lagenzahl:**

| Option | Vorteile | Nachteile |
|---|---|---|
| 2 Lagen | am billigsten, bekannt | keine durchgehende Masselage → größere Schleifen, schlechtere EMV, schwierigeres Layout |
| **4 Lagen (Empfehlung)** | durchgehende Masse unter der Schaltschleife (Q22, Q05), bessere EMV und Wärmeabfuhr, leichteres Layout | etwas teurer |
| 6 Lagen | noch mehr Freiheit | teurer, für diesen Wandler nicht nötig |

**Hersteller:**

| Option | Vorteile | Nachteile |
|---|---|---|
| JLCPCB | meist am billigsten | Versand aus China, Lieferzeit, ggf. Einfuhrkosten |
| Aisler | in Europa, schnell; Regeln stehen in der Aufgabe | meist teurer |

- **Größe:** ≤ 116,8 × 61 mm; kleiner ist billiger, zu klein erschwert Layout und Handlöten.
- **Preis:** Preisrechner für die geplante Größe (5 Stück, 1,6 mm, 1 oz, Schablone, Versand) bei beiden Herstellern; Datum notieren.
- Schablone mitbestellen (Reflowofen vorhanden).

## D4 Eingangsfilter – Konzept
**Störquelle:** Rechteckstrom des Buck (Höhe ≈ I_OUT, Tastgrad D); Grundwelle Î_1 = (2 · I_OUT / π) · sin(π · D) → bei D = 0,5: 1,91 A (Spitze).

**Grobe Beispielrechnung** (f = 500 kHz, C_IN,eff = 30 µF – Startannahmen, später durch Werte von A ersetzen):
- Ohne Filter liegt die Rippelspannung von C_IN fast ganz an der Netznachbildung (LISN, 50 Ω): V̂_1 ≈ Î_1 / (2π · f · C_IN,eff) = 1,91 A / (2π · 500 kHz · 30 µF) = 20,3 mV → Effektivwert 14,3 mV → 83,1 dBµV.
- Orientierung Klasse B 46 dBµV (Mittelwert, 0,5–5 MHz) + 6 dB Reserve → Dämpfung bei f: 83,1 − 46 + 6 = 43,1 dB.
- LC 2. Ordnung (40 dB/Dekade oberhalb f_0): f_0 ≤ 500 kHz / 10^(43,1/40) ≈ 42 kHz (deckt sich mit der Faustregel f_0 ≈ f/10 aus Q30, Q31).
- Mit C_F = 10 µF (effektiv): L = 1 / ((2π · f_0)² · C_F) ≈ 1,5 µH.
- Nur Abschätzung (ohne Oberwellen, ESL, Kopplung im Layout) → Simulation D9. Bei ≈ 370 kHz liegt der Grenzwert etwas höher (≈ 48,5 dBµV Mittelwert).

**Stabilität (Middlebrook):** Der Wandler wirkt am Eingang wie ein negativer Widerstand, |R_IN| = 12,8 Ω bei 22 V (00 §5). Die Ausgangsimpedanz des Filters (inkl. C_IN von A) muss bei allen Frequenzen deutlich darunter liegen (Faktor 3–10), besonders an der Resonanz f_0 → **Dämpfung nötig** (Q30, Q31, Q20).

**Optionen Filteraufbau:**

| Option | Vorteile | Nachteile |
|---|---|---|
| kein Filter (nur C_IN) | billig, kein Verlust | Grenzwert-Orientierung deutlich überschritten (≈ 83 statt 46 dBµV) |
| **LC einstufig + Dämpfung (Q30, Q20)** | Standardlösung, wenige Teile | Dämpfung nötig, Spulen-DCR kostet etwas Verlust |
| π-Filter (C–L–C) | dämpft in beide Richtungen; Eingangs-C hilft gegen Burst | ein Kondensator mehr |
| LC zweistufig | mehr Dämpfung bei kleineren Bauteilen | mehr Teile, mehr Verlust, mehr Resonanzen |
| zusätzlich Gleichtaktdrossel (optional, ggf. unbestückt) | für Gleichtakt-Burst/HF | Platz, Kosten, DCR; Gleichtaktprüfung nicht angenommen (00 §3) |

**Optionen Dämpfung:**

| Option | Vorteile | Nachteile |
|---|---|---|
| Elko mit passendem ESR parallel zu C_F (Q30) | einfachste Lösung | ESR streut und ändert sich mit Temperatur und Alter |
| R-C-Zweig parallel zu C_F (Startwert C_d ≈ 4 × C_F, R_d in der Größenordnung von Z_0 = √(L/C_F), Q50) | gezielt einstellbar | ein Bauteil mehr |
| Widerstand parallel zur Filterspule | praktisch kein Gleichstromverlust | weniger HF-Dämpfung |

## D5 Filterbauteile auswählen
- **L401 (Würth):** Induktivität bei Gleichstrom; I_R ≥ höchster Eingangsstrom (≈ 3 A bei Überlast, Wert von A) mit Reserve; I_SAT mit Reserve (Surge-Fall mit C klären); DCR klein → Verlust P = I_IN² · DCR (z. B. 10 mΩ → 1,72² A² · 10 mΩ = 30 mW); Eigenresonanzfrequenz hoch (Q30). Familien wie in A5 (WE-PD, WE-LHMI, WE-XHMI …); für HF-Anteile zusätzlich Ferrit möglich.
- **C_F:** X7R (oder C0G für kleine HF-Werte), Nennspannung aus der höchsten Spannung an diesem Knoten (C), DC-Bias-Kapazität (Q33: Klasse-2-MLCC verlieren viel Kapazität; Q31 rät im Filter zur Vorsicht), Gehäuse ≥ 0603.
- **Dämpfungs-Elko:** Kapazität, ESR, Rippelstrom, Nennspannung, Lebensdauer bei Temperatur; z. B. Alu-Elko SMD oder Alu-Polymer.
- **HF-Kondensator an der Buchse:** 1–100 nF X7R/C0G mit kleiner ESL gegen Burst.

## D6 Status-LED
| Option | Vorteile | Nachteile |
|---|---|---|
| **Logic-Level-N-FET (SOT-23), Gate an PGOOD, LED + Vorwiderstand aus V_OUT** | kein Steuerstrom, einfach; LED an = Ausgang in Ordnung | – |
| NPN-Transistor | billig | Basiswiderstand nötig, belastet den PGOOD-Pull-up |
| LED direkt am PGOOD-Pull-up | 1 Bauteil weniger | Pull-up an INTVCC (≈ 51 µA) reicht nicht für eine LED; INTVCC darf keine Last versorgen |

- Strom: I_LED = (V_OUT − V_F) / R_V. Jedes mA kostet 12 V · 1 mA = 12 mW (0,03 %) → hocheffiziente LED mit 0,5–1 mA. Beispiel V_F = 2,0 V (Datenblattwert einsetzen): R_V = (12 V − 2,0 V) / 1 mA = 10 kΩ (E12).
- **Bauteilgruppen:** N-FET mit V_GS(th),max deutlich unter 4,85 V (z. B. BSS138-Klasse); LED 0603/0805 (z. B. Würth WL-SMCW, andere Hersteller vergleichen).

## D7 Messpunkte und Stellschrauben einsammeln
- **Messpunkte:** V_IN direkt an der Buchse, nach dem Schutz, am Buck-Eingang; SW (mit kurzer Masseanbindung für den Tastkopf); V_OUT nah an C_OUT; ITH und VFB (Regelkreis, Q01 S. 24); PGOOD; mehrere GND-Punkte.
- **Bauart Messpunkte:** THT-Messösen lösen die 4-mm-Sperrzone zu SMD aus → **SMD-Testpunkte oder Pads** verwenden.
- **Injektionswiderstand (mit B):** 10–50 Ω zwischen V_OUT und oberem Teilerwiderstand für eine spätere Bode-Messung; Fehler im Betrieb 67 µA · 10 Ω = 0,67 mV (vernachlässigbar).
- **Stellschrauben der anderen Bereiche** sammeln: A12 (Snubber, R_BOOT, Gate-Widerstände, D102, Zusatz-C_IN), B12 (C_FF, Zusatz-C_OUT, Lötbrücke MODE, RUN-Jumper).

## D8 Zusammenführung
- **Stückliste:** CSV-Dateien aller Bereiche zusammenführen. Menge = Platinen (2–3) + Ersatz für gefährdete Teile (FETs, TVS, Sicherung, ggf. IC). Preis bei dieser Menge.
- **Händlerwahl:**

  | Option | Vorteile | Nachteile |
  |---|---|---|
  | ein Hauptlieferant (z. B. Mouser oder Farnell) | wenig Versandkosten, eine Bestellung | nicht jedes Teil am billigsten |
  | pro Teil der billigste Händler | niedrigster Teilepreis | mehrere Versandkosten und Mindestbestellwerte |

- **Budget:** Bauteile + Platine + Schablone + Versand (+ Einfuhrkosten) ≤ 100 € netto, 10 % Reserve. Bei Überschreitung die größten Kostentreiber an die zuständigen Bereiche melden.
- **Gesamtwirkungsgrad:** Verluste A + B + C + D bei 22/24/26 V und 3 A sammeln → η = P_OUT / (P_OUT + ΣP_V); optional 0,3 und 1,5 A. Das ist eine Orientierung; der echte Wert kommt erst mit Layout und Messung.
- **Schnittstellenprüfung:** höchste Spannung an jedem Knoten (von C) gegen die Nennspannung aller Bauteile dort; Ströme (I_PK,max von A, Überlast-Eingangsstrom) gegen Ratings; Regeln 00 §2 (E12, X7R/C0G, ≥ 0603, 2 Händler) für jede Zeile; Referenzbezeichner ohne Doppelungen.

## D9 Simulationen
| Fall | Bedingung | Bestanden, wenn |
|---|---|---|
| Filterdämpfung | AC: Stromquelle auf der Buck-Seite, Spannung an LISN (50 µH ‖ 50 Ω) | Dämpfung bei f und 2f ≥ Bedarf aus D4 |
| Stabilität | AC: Ausgangsimpedanz des Filters inkl. C_IN | deutlich unter 12,8 Ω, besonders an der Resonanz |
| Emission (grob) | Buck-Modell von B + Filter + LISN, FFT der LISN-Spannung (Q46) | unter der Klasse-B-Orientierung mit ≥ 6 dB Reserve |
| Einschwingen | Einstecken und Lastsprung mit Filter | kein Schwingen; Überschwingen unter der Grenze von C |
| LED | V_OUT-Rampe | LED schaltet mit PGOOD |

## D10 Layout-Vorgaben für KiCad vorbereiten (das Layout selbst macht die Gruppe)
- **Fertigungsregeln JLCPCB** (Q47, 4 Lagen, 1 oz außen): Leiterbahn/Abstand min. 0,09 mm, Via-Bohrung min. 0,2 mm, Via-Durchmesser min. 0,45 mm, Abstand zum Platinenrand min. 0,2 mm. Für Ausbeute und Handlöten großzügiger arbeiten (z. B. 0,15–0,2 mm).
- **Kriech-/Luftstrecken** nach dem Aisler-Link (Q48, Vorgabe R16); der strengere Wert gilt. Größere Abstände an Knoten mit Transienten (Info von C).
- **Netzklassen und Leiterbahnbreiten:** Breiten mit einem Rechner (Q49) für ≈ 3 A Eingang und 3 A Ausgang (kurzzeitig I_PK,max), Erwärmung ≤ 10–20 K; besser Kupferflächen.
- **Lagenaufbau** (4 Lagen): L1 Bauteile/Leistung, L2 durchgehende Masse, L3 Masse/Leistung, L4 Signal/Masse.
- **Checkliste und Reserven** aus 00 §5a, Stellschrauben und Messpunkte aus D7, Kupferflächen von A (A11), Sternpunkt von B (B10).
- Layout-Beispiele zum Ansehen: DC2736A (Q03), DC2786A (Q04).

## D11 Stückliste
Zeilen im Format `Stueckliste_Vorlage.csv` (Bereich D, Referenzen 400–499), je Teil 2 Händler mit Datum.

---

## Fertig, wenn
Filter, Stecker, Messpunkte und LED-Schaltung mit Teilenummern und 2 Händlern festgelegt; Platinenrahmen entschieden und Preis bekannt; Gesamt-Stückliste ≤ 100 € netto; Gesamtwirkungsgrad berechnet; Schnittstellenprüfung ohne offene Punkte; Layout-Vorgaben für die Gruppe fertig.

## Typische Fehler
- Ungedämpftes Filter → Schwingung mit dem negativen Eingangswiderstand des Wandlers.
- Eigenresonanz der Filterspule beim Burst ignoriert.
- Filter-Keramik mit Nennkapazität statt DC-Bias-Kapazität gerechnet.
- LED aus INTVCC versorgt oder unnötig hoher LED-Strom.
- THT-Messösen oder -Buchsen ohne 4-mm-Sperrzone.
- Preise ohne Stückzahl und Datum; Versandkosten vergessen.

## Gegenprobe
Frühere KI: `00_Projekt/altKI_Berechnungen.md` (§3.9 Filter/EMV), `D01_Eingangsfilter/altKI_ac.cir` und `03_Stueckliste/altKI_Kosten_Budget.md` – nur zum Vergleichen; ihr Entwurf lag über dem Budget.

## Startprompt für die KI
> Du hilfst mir bei Bereich D (Eingangsfilter, Stecker, Status-LED, Platinenrahmen und Zusammenführung) unseres Studienprojekts: nicht isolierter Buck 22–26 V → 12 V / 3 A mit LTC7800, Gruppenziel höchster Wirkungsgrad, aber sichere Funktion hat Vorrang (00 §1a), Budget 100 € netto inklusive Platine. Das Layout machen wir selbst; du bereitest nur den Rahmen vor. Lies `00_Projektkontext.md`, `01_Quellen_ApplicationNotes.md` und `D_Filter_Anschluesse_Platine_Zusammenfuehrung.md` vollständig und halte dich an die Regeln (Widerstände E12, Keramik nur X7R/C0G, SMD ≥ 0603, Spulen nur Würth, jedes Teil bei 2 europäischen Händlern mit Datum). Rechne mit vollständigen Herleitungen und Einheiten und gib Quellen an. Arbeite D1–D11 in der angegebenen Reihenfolge ab; zeig mir bei jedem Schritt die Optionen mit Trade-offs und Zahlen und lass mich entscheiden. Am Ende brauche ich: Filterauslegung mit Simulation, LED- und Steckerauswahl, Platinenrahmen mit Preis, die zusammengeführte Stückliste mit Budget, den Gesamtwirkungsgrad und die Layout-Vorgaben.
