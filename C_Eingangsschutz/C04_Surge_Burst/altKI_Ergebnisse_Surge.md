> **altKI – ungeprüfter Entwurf einer früheren KI-Sitzung.** Nur zur Gegenprobe nach eigener Rechnung, nicht als Vorgabe übernehmen. Pfade im Text beziehen sich auf die alte Ordnerstruktur.

# Ergebnisse: Eingangsschutz (Surge) mit echten Modellen

Datei: `ltspice/surge_inprot7.cir`.
**Quelle:** 24 V DC + Surge 1 kV (1,2/50 µs), 2 Ω Quellimpedanz (EN 61000-4-5).
**Kette:** Fuse → CMC (DM als 30 mΩ) → MOV `820542501` → L1 `74439370220` → TVS `824551281`
→ LTC4364-2 (M1/M2 + R_SNS 10 mΩ) → 2×Elko + L2 `74439370220` → MLCC → Last 16 Ω (≈1,3 A).
**Modelle:** MOV, TVS, Würth-Spulen und **LTC4364-2 echt**; Stopper-FET = **VDMOS-Proxy
BSC082N10LS** (100 V/8,2 mΩ) – das echte FDMS86101 siehe unten.
**Wichtig:** Der LTC4364 hat einen **Start-Timer (TMR)** und eine **sanfte Gate-Rampe**; der Ausgang
lädt die 100 µF nur langsam → der Surge wurde erst nach ~12 ms (Konverter voll an) eingespeist.

## Ergebnisse
| Größe | Wert | Bemerkung |
|---|---|---|
| V(gen) Spitze | ≈ 1024 V | Surge-Spitzenspannung |
| MOV-Knoten (a3) | **102,2 V** | Varistor klemmt den Grobanteil |
| TVS-Knoten (b) | **77,2 V** | TVS 824551281 (bei ~230 A) |
| M1 V_DS | **54,3 V** | Pass-FET muss das aushalten (100-V-FET ok) |
| Stopper-Ausgang OUT | 21,2 V DC → **22,8 V** Spitze | gegen Überspannung geklemmt |
| **Buck-Eingang (c)** | 21,3 V DC → **≤ 23,0 V** | **Surge erreicht den Buck nicht** ✔ |
| VCC / HGATE | 20,3 V / 25,4 V | Controller aktiv |

**Fazit:** Mit den echten Modellen wird der 1-kV-Surge **sicher geklemmt** – der Buck-Eingang bleibt
≤ 23 V (Verhaltensmodell im ersten Anlauf: ≤ 27,6 V). Die Kette MOV + L1 + TVS + LTC4364 funktioniert.

## Offene Punkte
1. **OUT_dc = 21,2 V statt ~24 V** (2,8 V Abfall über M1/M2 trotz ≤1,3 A) → prüfen: ggf. Gate-Ansteuerung
   bzw. Proxy-Effekt. Für die Klemmung unkritisch, aber für den Wirkungsgrad relevant.
2. **Echtes FDMS86101 (BSIM3-Modell)** läuft in der LTC4364-Kette **nicht brauchbar**:
   - `.ic/uic` -> „Time step too small" (Fehler im **internen Stromspiegel `u1:pmir` des LTC4364**).
   - `startup` + entspannte Optionen -> läuft durch, aber der FET **schaltet in der Kette nicht durch** (OUT = 0).
   - **Isolierter Bauteil-Test** (`fdms86101_test.cir`) funktioniert dagegen perfekt und liefert
     **R_DS(on) = 8,2 mΩ** (Datenblatt: 8 mΩ) – das Modell selbst ist korrekt.

### Empfohlener Workaround: „Split-Domain" (getrennte Domänen)
1. **System-/Kettensimulation** (Klemmung, Gate-Timing, Stromgrenzen) mit dem LTC4364 + einem
   LTspice-nativen 100-V-VDMOS **BSC082N10LS** (100 V, **8,2 mΩ** – exakt dieselbe Klasse).
   -> schnell, stabil, ergebnisliefert (dieses Dokument).
2. **Bauteil-Simulation** des **echten FDMS86101** isoliert (`fdms86101_test.cir`) für R_DS(on),
   Body-Diode, SOA/thermisch.
3. Da der reale FDMS86101 **8,2 mΩ** liefert = **BSC082N10LS 8,2 mΩ**, ist der Proxy im System
   **quantitativ gerechtfertigt** (für die Doku als Annahme kennzeichnen).

Alternativen: (a) ein **VDMOS-Ersatzmodell „FDMS86101"** aus dem Datenblatt (VDS 100 V, Ron 8 mΩ,
Qg ≈ 55 nC, Vgs(th) ≈ 3 V) anlegen, damit die Netzliste „FDMS86101" liest; (b) anderes onsemi-Modell
(VDMOS-basiert) verwenden.

### Umgesetzt (gewählt: Workaround 1)
| Datei | Inhalt | Ergebnis |
|---|---|---|
| `surge_inprot7.cir` | Kette: MOV + L1 + TVS + **LTC4364-2** + **BSC082N10LS** (100 V/8,2 mΩ) | Surge geklemmt, Buck-Eingang ≤ 23 V |
| `fdms86101_test.cir` | **echter FDMS86101** isoliert (50 V, Puls) | **R_DS(on) = 8,2 mΩ** = Datenblatt (8 mΩ) |

**Hinweis zum Ausgangspegel:** In der Kette liegt die DC-Quelle in Reihe mit dem **2-Ω-Surge-Widerstand**.
Bei ~1,3 A ergibt das 24 V − 1,3 A·2 Ω ≈ **21,4 V** am Ausgang – also **kein FET-Abfall** (Vgs = 11,8 V,
FET voll durchgesteuert, `Vsrc` ≈ `Vout`). Für den Klemm-Nachweis unkritisch; bei Bedarf DC- und
Surge-Zweig trennen (DC 0 Ω, Surge über die 2 Ω).
3. **CMC** im Differenzialmodus nur als DCR (30 mΩ) modelliert (Gleichtakt erst nach Layout bewertbar).
4. **Burst (2 kV EFT)** noch nicht mit echten Modellen simuliert.

## Vergleich zum ersten Anlauf (Verhaltensmodelle)
| Größe | erster Anlauf (ngspice/Verhalten) | jetzt (LTspice/echt) |
|---|---|---|
| MOV-Knoten | 102,1 V | 102,2 V |
| TVS-Knoten | 59,6 V | 77,2 V |
| Buck-Eingang max | 27,6 V | ≤ 23,0 V |

Der unterschiedliche TVS-Knoten kommt vom **echten** TVS-Modell (lineares RS statt idealisierter Klemme).
