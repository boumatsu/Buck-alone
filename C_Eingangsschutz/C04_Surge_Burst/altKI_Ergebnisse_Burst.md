> **altKI – ungeprüfter Entwurf einer früheren KI-Sitzung.** Nur zur Gegenprobe nach eigener Rechnung, nicht als Vorgabe übernehmen. Pfade im Text beziehen sich auf die alte Ordnerstruktur.

# Ergebnisse: Burst 2 kV (EFT) mit echten Modellen

Datei: `ltspice/burst_eft.cir`.
**Quelle:** EFT 2 kV, 5/50 ns, 50 Ω Generator, 33 nF CDN (Differenzialmodus-Worst-Case, EN 61000-4-4).
**Ruhelage:** 24 V DC über eine Versorgungs-Induktivität (im ns-Bereich hochohmig -> entkoppelte
Versorgung, wie real). Kette: CMC (30 mΩ DM) → MOV `820542501` → L1 `74439370220` → TVS `824551281`
→ LTC4364 in Durchlass (als On-Widerstand 2×8,2 mΩ, Workaround 1) → Elkos + L2 → MLCC → Last.
Die MOV/TVS/Würth-Spulen sind **echte Modelle**.

## Ergebnisse
| Größe | Wert |
|---|---|
| V(gen) Spitze | 1999 V (2 kV) |
| MOV-Knoten (a2) | **84,5 V** |
| TVS-Knoten (b, nach L1) | **24,0 V** |
| **Buck-Eingang (c)** | **23,86 – 23,88 V** |
| Ruhewert (a2) | 24,37 V |

**Fazit:** Der 2-kV-EFT-Burst wird von **L1 (22 µH)** praktisch vollständig geblockt – der
Buck-Eingang schwankt nur um **~0,5 V** (keine Gefährdung). Der MOV-Knoten erreicht ~84,5 V.

## Vergleich zum ersten Anlauf (Verhaltensmodelle)
| Größe | erster Anlauf | jetzt (echt) |
|---|---|---|
| MOV-Knoten | 86,8 V | 84,5 V |
| nach L1 | 24,1 V | 24,0 V |
| Buck-Eingang | 23,9–24,0 V | 23,86–23,88 V |

-> Sehr gute Übereinstimmung (Δ < 3 %) **mit echten Modellen**.

## Offene Punkte
1. **Gleichtakt-Burst (CM)** ist ohne Layout/Parasiten **nicht bewertbar** (der CM-Pfad hängt an der
   Masseführung) – nach dem Platinen-Layout / mit Prüfaufbau zu bewerten.
2. Burst-Train (nicht nur Einzelpuls) und Entladungs-/Rückladeverhalten könnten ergänzt werden.
