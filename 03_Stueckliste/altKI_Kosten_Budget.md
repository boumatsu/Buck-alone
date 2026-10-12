> **altKI – ungeprüfter Entwurf einer früheren KI-Sitzung.** Nur zur Gegenprobe nach eigener Rechnung, nicht als Vorgabe übernehmen. Pfade im Text beziehen sich auf die alte Ordnerstruktur.

# 13 – Kosten und Budget (Ziel ≤ 100 € inkl. Ersatzbauteile, besser < 80 €)

> ⚠ **STATUS: VORLÄUFIG (S0/S1).** **Es gibt keine Gratisproben – alles wird bezahlt.** Preise stammen aus Suchtreffern (Umrechnung mit Annahmen: 1 USD ≈ 0,92 EUR, 1 SEK ≈ 0,09 EUR, 1 DKK ≈ 0,134 EUR; Momentaufnahme, Datum unbekannt). Viele Preise sind **Schätzungen** (in der CSV als SCHAETZUNG markiert). **Vor jeder Bestellung im Warenkorb prüfen.** Alle Preise **netto**, Brutto ≈ ×1,19. **Nicht enthalten:** Platine (Aisler: Mindestbestellung 3 Stück, Preis nach Fläche → Preisrechner: https://community.aisler.net/t/get-instant-quotes-with-our-pcb-price-calculator/5539), Versand, Zoll.

Preisliste je Teil: `13_Kosten_Preisliste.csv`.

## Varianten
- **V1 (aktueller Entwurf):** Buck-Spule 74439370100 (10 µH, 6,5 mΩ), L1 = L2 = 74439370220 (22 µH).
- **V2 (kostenoptimiert):** Buck-Spule **744393665100** (WE-XHMI 4540, 10 µH, 15,4 mΩ max, 15,3 A Ir, 18,5 A Isat, 11,3×10×6 mm, Farnell IT 3,32 € (1+), 390 Stk.); L1 = 74439370220 (22 µH), **L2 = 744393665100** (10 µH).
  Folgen (Simulation/Rechnung, S1/S2): Wirkungsgrad **−0,27 Prozentpunkte** (≈ 0,10 W mehr Spulenverlust); EMV-Reserve bei 500 kHz nur noch **6,8 dB** (statt 13,7 dB); **nicht möglich:** L1 = L2 = 10 µH (−0,2 dB, fällt unter die angenommene Grenze). Alternative 74439346100 (6060, 26,5 mΩ, 3,86 € belegt) wäre teurer und schlechter als 744393665100.

## Ergebnis (Bauteile, netto, ohne Platine/Versand)
| Szenario | V1 netto (brutto) | V2 netto (brutto) |
|---|---|---|
| 1 Platine, kein Ersatz | 72,9 € (86,8 €) | **67,5 €** (80,3 €) |
| S1: + Ersatz für billige/empfindliche Teile (FETs, TVS, Varistor, Sicherungen, Kondensatoren, Kleinteile) | 87,8 € (104,4 €) | 82,3 € (98,0 €) |
| S2: + je 1 Ersatz-IC (LTC7800, LTC4364) und je 1 Ersatz-Spule | 125,0 € (148,7 €) | 116,9 € (139,1 €) |

**Bewertung (vorläufig):** Mit diesem Design ist **≤ 100 € inklusive Ersatzteile und Platine nicht erreichbar.** Selbst V2 mit nur S1-Ersatz liegt netto bei 82 € (ohne Platine). **Unter 80 €** geht nur: 1 Platine **ohne** Ersatz, **ohne** Platine und Versand (V2: 67,5 € netto). Die Platine (3 Stück Mindestbestellung) kommt noch dazu und ist die größte Unbekannte.

## Kostentreiber
LTC7800 ≈ 10,8 €, LTC4364 ≈ 11,2 €, Spulen (3 Stück) ≈ 12–18 €, FDMS86101 ×2 ≈ 4 €, Murata-MLCC ×15 ≈ 7,5 € (Schätzung), CMC ≈ 3,2 €, Buchsen ×4 ≈ 4,5 €.

## Hebel (alle bezahlt, alle zu prüfen)
1. **Kleinere Platine** (Full-Brick 116,8×61 mm ist nur das **Maximum**; Aisler-Preis steigt mit der Fläche).
2. **V2-Spulen** (−5,4 € bei −0,27 Pkt. η und weniger EMV-Reserve).
3. **Steckverbinder:** 2,54-mm-Stiftleisten statt 4-mm-Buchsen (laut Aufgabe erlaubt; Preis offen, vermutlich unter 2 € statt 4,5 €; mehrere Pins parallel wegen 3 A je Pin; THT-Abstand beachten).
4. **Widerstände/Kondensatoren als Sortiment** statt Einzelstücke.
5. **Ersatzstrategie:** Ersatz nur für Teile mit hohem Ausfallrisiko (FETs, TVS, Sicherungen). Ersatz-ICs und Ersatz-Spulen nur **gemeinsam in der Gruppe** (eine Reserve für alle Gruppen-Boards).
6. **Weniger Keramik:** Murata-Stückzahl (15) hängt an der Annahme „kein 10×-Teil mit 10 µF/X7R verfügbar" – Alternativen prüfen (Polymer/Elko-Anteil), aber Prof-Regeln (X7R, Derating) beachten.
7. **LTC4364 weglassen** (≈ −16 € mit FETs/Beschaltung) wäre nur mit neuem Schutzkonzept möglich (60-V-Buck-FETs, LTC7800 VIN max 65 V gegen simulierten Knoten bis ≈ 60–70 V, Verpolungsschutz anders) – **nicht empfohlen, ohne Neusimulation**.
8. Versandkosten minimieren (wenige Lieferanten; Mouser/Farnell/RS Mindestbestellwerte beachten).

## Offene Kostenfragen
- Zählen die 100 € **mit oder ohne Platine** (Annahme: mit)? Netto oder brutto?
- Aisler-Preis für die endgültige Plattenfläche (3 Stück).
- Mouser-Preise: Murata-MLCC, Würth-Kondensatoren, Sicherung, LTC4364 im SO-16, Elkos.
- Versand/Zoll je Lieferant.
