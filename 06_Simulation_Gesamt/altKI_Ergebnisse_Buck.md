> **altKI – ungeprüfter Entwurf einer früheren KI-Sitzung.** Nur zur Gegenprobe nach eigener Rechnung, nicht als Vorgabe übernehmen. Pfade im Text beziehen sich auf die alte Ordnerstruktur.

# Ergebnisse: Buck mit echten Modellen (LTspice)

Alle Läufe: **echtes LTC7800-Modell** (LTspice-lib) + **echtes Würth-Spulenmodell**
`1510_74439370100_10u` (10,4 µH, 6,4 mΩ) + **echter Buck-FET `BSZ097N04LS`** (Infineon,
VDMOS-Modell aus `standard.mos`). Aufbau (`ltspice/buck_main_bsz.cir`): VIN 22/24/26 V,
Vout 12 V, Last 4 Ω (~3 A), f ≈ 500 kHz (R_FREQ 33 k), C_IN 16,5 µF, C_OUT 33 µF,
R_SENSE 5 mΩ, C_SS für die Messung auf 10 nF verkürzt (ändert den eingeschwungenen
Wirkungsgrad nicht). Messung 1,2–1,5 ms.

## Ergebnis mit echtem BSZ097N04LS (EXTVCC = Vout)
| VIN | Vout | Ripple (pp) | Pin | Pout | **η** |
|---|---|---|---|---|---|
| 22 V | 11,9961 V | 9,73 mV | 36,765 W | 35,977 W | **97,85 %** |
| 24 V | 11,9962 V | 10,57 mV | 36,725 W | 35,977 W | **97,96 %** |
| 26 V | 11,9962 V | 11,85 mV | 36,657 W | 35,977 W | **98,16 %** |

Der Wirkungsgrad **steigt leicht mit VIN** (kleinerer Eingangsstrom → kleinere Leitverluste,
während EXTVCC = Vout die Gate-Verluste konstant hält).

## Frühere Messung mit Platzhalter-FET BSC028N06LS3 (60 V, ~2,8 mΩ, EXTVCC = Vout)
| VIN | Vout | Ripple (pp) | Pin | Pout | **η** |
|---|---|---|---|---|---|
| 22 V | 11,9962 V | 9,29 mV | 38,414 W | 35,977 W | **93,66 %** |
| 24 V | 11,9961 V | 9,43 mV | 38,480 W | 35,977 W | **93,49 %** |
| 26 V | 11,9961 V | 9,59 mV | 38,536 W | 35,977 W | **93,36 %** |

## Vergleich EXTVCC = GND vs. EXTVCC = Vout (mit Platzhalter-FET BSC028N06LS3)
| VIN | η (GND) | η (EXTVCC=Vout) | Delta |
|---|---|---|---|
| 22 V | 91,97 % | 93,66 % | +1,69 Pkt. |
| 24 V | 91,49 % | 93,49 % | +2,00 Pkt. |
| 26 V | 90,98 % | 93,36 % | +2,38 Pkt. |

**Fazit:** Die Design-Entscheidung „EXTVCC = Vout" ist mit echtem Modell **belegt** und bringt
~1,7…2,4 Prozentpunkte; ohne sie sinkt η mit steigendem VIN (LDO-Verlust).

## Bewertung / offene Punkte
- Mit dem **echten** FET (BSZ097N04LS) ergibt LTspice **η ≈ 97,9–98,2 %** – das **bestätigt** die
  Formelschätzung des ersten Anlaufs (~97,9 % für die Buck-Stufe).
- **Wichtige Lehre:** Ein „falsches" FET-Modell (BSC028N06LS3, 60 V/~2,8 mΩ) lieferte irreführend
  nur **93,5 %** – seine größeren Kapazitäten/Gate-Ladungen erzeugen bei 500 kHz hohe
  Schaltverluste. **Das exakte Bauteilmodell ist entscheidend** – genau deshalb der Neustart.
- **Nächste Schritte Buck:**
  1. Verlustaufschlüsselung je Bauteil aus dem `.raw` auswerten (P_M1, P_M2, P_L, P_Rsen, P_gate).
  2. Laststufen-/Anlauf-/Kurzschlussverhalten und Regelkreis (Bode) in LTspice.
  3. Temperatur (`.temp`) und Monte-Carlo (Teiler-Toleranz).
  4. C_IN/C_OUT mit DC-Bias-Modell (Murata/SimSurfing) verfeinern.
