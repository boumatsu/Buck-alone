> **altKI – ungeprüfter Entwurf einer früheren KI-Sitzung.** Nur zur Gegenprobe nach eigener Rechnung, nicht als Vorgabe übernehmen. Pfade im Text beziehen sich auf die alte Ordnerstruktur.

# LTspice: Pin-Zuordnung LTC7800 (verifiziert)

## Wie ermittelt?
1. Symbol `lib\sym\PowerProducts\LTC7800.asy` ausgelesen: 19 Pins mit `SpiceOrder`-Attributen
   (1,2,5,6,7,19,20,21,…,32).
2. Referenz-Jig `examples\jigs\7800.asc` als `.cir` exakt nachgebaut und in LTspice laufen lassen
   -> Ergebnis: **Vout = 3,2947 V, VFB = 0,8026 V, INTVCC = 5,100 V** (Jig ist 12 V -> 3,3 V).
   Damit ist die Reihenfolge eindeutig bestätigt.

## XU1-Knotenreihenfolge (32 Knoten, so in die Netzliste schreiben)
| Pos | SpiceOrder | Pin | im Entwurf verbunden mit |
|----:|---:|---|---|
| 1 | 1 | Sense- | Ausgangsseite R_SENSE (SENSN) |
| 2 | 2 | Freq | R_FREQ (33 k) nach GND |
| 3 | 3 | (n/a) | GND |
| 4 | 4 | (n/a) | GND |
| 5 | 5 | PLLIN/Mode | GND (= Burst Mode) |
| 6 | 6 | SGND | GND |
| 7 | 7 | Run | Teiler 330 k / 22 k |
| 8–18 | 8–18 | (n/a) | GND |
| 19 | 19 | INTVcc | 10 µF + 1 µF nach GND |
| 20 | 20 | EXTVcc | Vout (12 V) |
| 21 | 21 | PGND | GND |
| 22 | 22 | Vin | Eingang |
| 23 | 23 | BG | Gate Low-Side-FET |
| 24 | 24 | Boost | C_B 0,22 µF + Boot-Diode |
| 25 | 25 | SW | Schaltknoten |
| 26 | 26 | TG | Gate High-Side-FET |
| 27 | 27 | Pgood | offen / Pull-up |
| 28 | 28 | Ilim | GND (= 22/30/36 mV) |
| 29 | 29 | Track/SS | C_SS |
| 30 | 30 | Ith | Kompensationsnetz |
| 31 | 31 | Vfb | Teiler-Mittelpunkt |
| 32 | 32 | Sense+ | Spulenseite R_SENSE (SENSP) |

## Wichtige LTspice-Hinweise (aus dieser Sitzung)
- In einer **reinen `.cir`** wird `standard.mos` **nicht** automatisch geladen -> immer
  `.include "...\lib\cmp\standard.mos"` einbinden, sonst „Unable to find model".
- Modell-Subcircuits (LTC7800, Würth-Spulen) per `.lib`/`.include` einbinden.
- Induktivität aus Würth-Lib **als Subcircuit-Instanz** verwenden:
  `X1 SW SENSP 1510_74439370100_10u` – **nicht** `L1 SW SENSP 1510_…` (Zahl wird sonst fehlgeparst!).
- Batch-Läufe **immer mit `startup`** (`.tran 0 1.5m 0 50n startup`). Ohne `startup` versucht LTspice
  den DC-Arbeitspunkt eines *schaltenden* Reglers zu lösen und hängt praktisch endlos.
- Logs sind UTF-16; zum Lesen per Skript in UTF-8-WS zu ASCII wandeln.
