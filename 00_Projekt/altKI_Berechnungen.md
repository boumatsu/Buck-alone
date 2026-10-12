> **altKI – ungeprüfter Entwurf einer früheren KI-Sitzung.** Nur zur Gegenprobe nach eigener Rechnung, nicht als Vorgabe übernehmen. Pfade im Text beziehen sich auf die alte Ordnerstruktur.

# 03 – Berechnungen (mit Formeln, Zahlen, Einheiten)

> ⚠ **STATUSHINWEIS (gilt für dieses ganze Dokument):** Alle Entscheidungen, Bauteilwahlen, Zahlen und Ergebnisse sind **VORLÄUFIG und nicht fix**. Jede Berechnung muss noch **unabhängig überprüft und simuliert** werden (siehe 03 §3.11 Verifikationsmatrix). Datenblätter sind nur teilweise gelesen (siehe 10). Verfügbarkeit und Preise sind Momentaufnahmen aus Suchtreffern (siehe 06, 13). Alles muss laufend im Entwicklungsprotokoll (11) dokumentiert werden.
> Statusstufen: **S0** Annahme/Schätzung · **S1** gerechnet (Formel) · **S2** durch Simulation bestätigt · **S3** durch Datenblatt UND Simulation/Messung bestätigt.

Alle Zahlen sind Modellrechnungen; Annahmen stehen in 08.

## 3.1 Feedback-Teiler (LTC7800)
V_OUT = V_FB·(1 + R1/R2) + I_FB·R1 (KCL am FB-Knoten). V_FB = 0,8 V (±0,5 %), I_FB = ±5 nA typ / ±50 nA max.
R1/R2 = 12/0,8 − 1 = 14 → R2 = 12 kΩ, R1 = 150 kΩ + 18 kΩ = 168 kΩ (E12, in Reihe) → V_OUT = 0,8·15 = 12,000 V.
Teilerstrom 12 V/180 kΩ = 66,7 µA (P = 0,8 mW); Fehler durch I_FB: 50 nA·168 kΩ = 8,4 mV (0,07 %).
Toleranz (Worst Case): 1 %-Widerstände → ca. +2,4 %/−2,3 % (V_OUT 11,72…12,29 V); 5 % wäre +10 % (zu schlecht); 0,1 % → ca. ±0,3 %. Empfehlung ≥ 1 %, bei Bedarf 0,1 % für R2 und R1.

## 3.2 Tastgrad, Frequenz, Ripple, Spule
D = V_OUT/V_IN = 0,462 (26 V) … 0,545 (22 V); t_on = D/f = 0,92…1,09 µs ≫ t_on,min 45 ns.
R_FREQ: Stützpunkte Datenblatt 25 kΩ→0,32 MHz, 54,9 kΩ→≈1 MHz, 65 kΩ→1,18 MHz, 100 kΩ→2,1 MHz; Interpolation f(33 kΩ) ≈ 502 kHz (±10 % Streuung annehmen).
ΔI_L = V_OUT(1−D)/(f·L) = 12·0,538/(500 k·10 µ) = 1,29 A (26 V, 43 %); 1,09 A bei 22 V (36 %). I_pk = 3 + 1,29/2 = 3,65 A.

## 3.3 Strommessung
R_SENSE = V_SENSE(MAX,min)/I_pk = 22 mV/3,65 A = 6,0 mΩ → 5 mΩ gewählt (≈20 % Reserve). Limit: 22 mV/5 mΩ = 4,4 A (min), 30 mV → 6,0 A (typ), 36 mV → 7,2 A (max). Verlust (3²+1,29²/12)·5 mΩ = 46 mW. Spule: I_sat 35,8 A ≫ 7,2 A.
Annahme für Regelkreis: V_SENSE = (V_ITH − 0,7 V)/10 (aus Datenblattkurve, nicht exakt!).

## 3.4 Kondensatoren (Worst Case mit Derating)
Formel: C_eff = n·C_nenn·(1−Toleranz 0,10)·(1−Temperatur 0,15)·Bias-Faktor·(1−Alterung 0,05). **Bias-Faktoren sind Annahmen** (75 % bei 24 V/100 V-Teil; 90 % bei 12 V/100 V-Teil) → mit Herstellerkurven (REDEXPERT/SimSurfing) prüfen.
- C_IN: 6×4,7 µF/100 V X7R → 15,4 µF; ΔV_IN = I·D(1−D)/(f·C) = 3·0,25/(500 k·15,4 µ) = 98 mV. I_RMS = I·√(D(1−D)) = 1,5 A.
- C_OUT: 9×4,7 µF/100 V X7R → 27,7 µF; ΔV_OUT ≈ ΔI_L·(ESR + 1/(8·f·C)) = 1,29·(2 mΩ + 1/(8·500 k·27,7 µ)) = 14,2 mV.
- Spannungsverhältnisse: C_B 10×, C_INTVCC 10×, C_SS 10× (50 V/≤5 V), C_OUT 8×, C_IN 4×, C_VIN 4×.
- C_B ≥ 100·C_iss(Q1): BSZ097N04LS G hat C_iss ≈ 1,4 nF typ (Infineon-Produktseite), max 1,9 nF (DigiKey) → C_B ≥ 140…190 nF → **0,22 µF (E12), 50 V, X7R, 0805** (frühere Angabe 0,1 µF basierte irrtümlich auf dem 650-pF-Wert des BSZ063 und ist **korrigiert**).

## 3.5 Soft-Start, UVLO
t_SS = C_SS·0,8 V/10 µA = 100 nF·0,8/10 µ = 8 ms.
V_UVLO,rise = 1,21·(1+RB/RA) − 7 µA·RB = 1,21·16 − 2,31 = 17,05 V; fall 1,16·16 − 2,31 = 16,25 V (RB 330 k, RA 22 k); RUN bei 26 V: 1,63 V (< 8 V).

## 3.6 Verlustbilanz Buck (Python-Modell; Datenblattgleichungen LTC7800)
P_top = D·I_rms²·R_DS(on)(1+δ) + V_IN²·(I/2)·R_DR·C_rss·(1/(V_INTVCC−V_plat) + 1/V_plat)·f; P_bot = (1−D)·I_rms²·R; P_DCR = I_rms²·R_DCR·(1+0,0039·55 K); P_RS = I_rms²·R_S; P_gate = V_OUT·f·2Q_g (EXTVCC); P_Coss = Q_oss·V_IN·f; P_Totzeit/Qrr; Kernverlust (Annahme).
Eingangsdaten BSZ097N04LS G (Infineon-Datenblatt): R_DS(on) max 14,2 mΩ @4,5 V, Q_g 8,6 nC @4,5 V, C_rss 16 pF, Q_oss 13 nC, Q_rr 15 nC, V_plateau 3,3 V.
Ergebnis 24 V/3 A (mit Schottky, Kernverlust 0,10 W): P_buck ≈ 0,78 W → η_Buck 97,9 %; mit Schutzkette (Sicherung 14 mΩ, L1/L2 je 13,3 mΩ, Stopper 24 mΩ, CMC ≈ 40 mΩ gesamt geschätzt) η_gesamt 97,1 %. Kernverlust-Bandbreite 0,05…0,30 W → η_gesamt 97,3…96,7 %. Ohne Schottky (Q_rr 15 nC): −0,3…−0,4 Punkte. Realistisch erwartet: 95,5…96,5 % bei 3 A.
Teillast (Modell, CCM): 1 A: 95,5 %; 2 A: 97,0 % (Burst-Mode darunter besser).

## 3.7 Regelkreis (Kleinsignal, Python)
Modulator: G_vc = G_i·R_L/(1+s/ω_p)·(1+s·ESR·C_out)·H_s, G_i = 1/(10·R_S) = 20 A/V (Annahme), ω_p = 1/(R_L·C_out). Fehlerverstärker g_m = 2 mS, β = 0,8/12. Kompensation R_ITH = 2,2 kΩ, C_ITH = 10 nF (f_z = 1/(2π·R·C) = 7,2 kHz), C_ITH2 = 100 pF (f_p ≈ 723 kHz).
Ergebnis: f_c 21…48 kHz, PM 63…75°, GM 8…23 dB (C_out 20…45 µF, Last 0,5…3 A, Q 0,7…2); mit C_ITH ±25 %: PM 63…73° bei C_out_eff 26…45 µF.

## 3.8 LTC4364 (aus Datenblatt-Formeln)
V_REG = 1,25·(1+R7/R8) = 27,85 V; UV/OV: V_UV = 1,25·(R1+R2+R3)/(R2+R3) = 16,4 V; V_OV = 1,25·(R1+R2+R3)/R3 = 29,8 V.
R_SNS = ΔV_SNS/I_LIM = 45 mV/4,5 A → 10 mΩ (5,0 A typ; 25 mV bei V_OUT<1,5 V → 2,5 A).
Timer: t_OC = C_TMR·1,35 V/I_TMR(OC), I_TMR(OC) = 10 µA + 3,36 µA/V·(V_CC−V_OUT−0,5 V); Kurzschluss (26 V): 95,7 µA → 0,66 ms; P_M1 = 26 V·2,5 A = 65 W; P²t = 2,8 W²s.
Überlast 2 V: 120 W, 0,71 ms, P²t 10,3 W²s. Dauer-Überspannung 40 V: P = 36 W, ≈7,1 ms.
Pass-FET FDMS86101: R_θJC = 1,2 K/W, E_AS = 173 mJ. Thermischer Anstieg (Halbunendlich-Modell Silizium, Die ≈ 3×3 mm, **Annahme**): ΔT 11 K (Surge), 13 K (Kurzschluss), 26 K (2 V), 25 K (Überspannung).
Inrush: I = I_HGATE(UP)·C_L/C_HG = 20 µA·160 µF/6,8 nF ≈ 0,47 A.

## 3.9 Eingangsstrom, Sicherung, Filter
I_IN = 36 W/(η·V_IN) = 1,70 A (22 V) … 1,44 A (26 V); bei Ausgangslimit 6 A: bis 3,4 A; 7,2 A: bis 4,1 A → Sicherung 5 A träge (Littelfuse 0452005.MRL, 125 V AC/DC), R ≈ 14 mΩ (aus 454-Serie übernommen, Annahme).
Eingangs-Grundwelle bei 500 kHz: I₁ = (2·I_OUT/π)·sin(πD) = 1,91 A. Middlebrook: Z₀ = √(L/C) = 0,53 Ω ≪ R_in = V²/P = 13,1 Ω (stabil).
Konduktive Emissionen (ngspice-AC-Modell, LISN 50 Ω, RMS am Empfänger): bei 500 kHz 32,3 dBµV (L2 = 22 µH) gegen 46 dBµV (Mittelwert-Grenze, Klasse B angenommen) → 13,7 dB Reserve; bei L2 = 4,7 µH nur 0,3 dB. Reale Parasiten verkleinern die Reserve → Messung nötig.

## 3.10 E12-Prüfung
Widerstände 150k, 18k, 12k, 33k, 2,2k, 330k, 22k, 10Ω, 100k, 4,7k, 220k, 8,2k, 10k – alle E12. Kapazitäten 10 nF, 100 pF, 1 nF, 100 nF, 1 µF, 4,7 µF, 10 µF, 47 nF, 6,8 nF, 47 µF – E12. Induktivitäten 10 µH, 22 µH – E12. **Ausnahmen:** CMC 744841414 = 14 µH (Katalogteil), R_SENSE (laut Vorgabe frei).

## 3.11 Verifikationsmatrix (welche Rechnung wurde wie geprüft?)
Status: S0 Annahme · S1 nur gerechnet · S2 durch Simulation bestätigt · S3 Datenblatt + Simulation/Messung. **Keine einzige Rechnung ist S3.** Alle müssen noch unabhängig nachgerechnet und mit echten Modellen simuliert werden.

| Rechnung | Status | Wie geprüft | Was noch fehlt |
|---|---|---|---|
| Teiler 150k+18k/12k → 12,000 V | S1 | Formel; im Python-Buck-Modell wird V_OUT geregelt (Modell nimmt V_FB = 0,8 V an) | LTspice mit LTC7800-Modell; Toleranzrechnung simulieren (Monte-Carlo) |
| Tastgrad/ΔI_L/I_pk | S2 | Python-Zeitbereichsmodell: ΔI_L 1,02…1,23 A, i_L,max 3,47…3,57 A (Formel 1,09…1,29 A / 3,65 A) | echte Spulenkennlinie (L über I), LTspice |
| R_SENSE 5 mΩ / Limit 4,4–7,2 A | S1 | Formel; Kurzschluss im Modell zeigt 2,7 A Foldback | echte Strom-Limit-Kennlinie (V_SENSE vs. V_ITH) aus LTspice-Modell; Messung |
| Frequenz 500 kHz (R_FREQ 33 kΩ) | S0/S1 | lineare Interpolation Datenblatt Fig. 8 | Fig. 8 genau ablesen / Simulation |
| C_IN/C_OUT Worst-Case | S0/S1 | Formel + Bias-Annahmen; Ripple im Python-Modell (Cout 36 µF eff.) | DC-Bias-Kurven; Simulation mit C(V)-Modell |
| C_B ≥ 100·C_iss | S1 | Datenblattregel | – |
| Soft-Start 100 nF → 8 ms | S2 | Python: 7,6 ms bis 11,4 V | LTspice |
| UVLO 17,05/16,25 V | S1 | Formel | LTspice/Messung |
| Regelkreis PM 63–73° | S1/S2 | Kleinsignalmodell (Python) + Zeitbereich Laststufe (41 µs Beruhigung, 232 mV) – Modell-Annahme V_SENSE=(V_ITH−0,7)/10 | echter LTC7800-Regelkreis, Bode in LTspice, ITH-Messung |
| Verlustbilanz/Wirkungsgrad | S1 | Datenblattformeln, **kein** Schalt-Zeitbereichs-Verlust; Kernverlust S0 | REDEXPERT, LTspice-Verlustsimulation, Messung |
| LTC4364-Klemme/UV/OV/ILIM | S1 | Datenblattformeln | LTspice-Modell; Fehlerfälle |
| Surge/TVS/Varistor | S2 (Verhaltensmodell) | ngspice | echte Modelle (Würth), TVS-Kurve, SOA |
| Pass-FET Temperatur | S0/S1 | grobes Halbunendlich-Modell | SOA-Kurve, ggf. thermische Simulation |
| EMV-Filter (DM) | S1/S2 | AC-Modell ngspice; ohne CMC/Parasiten | Vormessung, Layoutparasiten, CM-Modell |
| Burst CM | – | Simulation unbrauchbar | nach Layout |
| Kosten | S0/S1 | Preise aus Suchtreffern | Warenkorb |
