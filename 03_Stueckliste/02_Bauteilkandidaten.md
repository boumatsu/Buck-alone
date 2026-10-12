# 02 – Bauteilkandidaten je Bereich (mit Datenblatt-Links)

Stand: 12.10.2026. Kennwerte von Hersteller- oder Händlerseiten gelesen (Quelle = Link in der Zeile). **Kandidaten, keine Entscheidung** – die zuständige Person rechnet und wählt (Regeln 00 §1a/§2). Preise/Bestand sind Momentaufnahmen; vor der Bestellung bei 2 Händlern prüfen.
„DB prüfen" = Wert stand nicht auf der Seite, im Datenblatt nachsehen.

---

## Bereich A – Leistungsstufe

### A7 MOSFETs Q101/Q102 – 40-V-Klasse
| Teil | V_DS | R_DS(on) max @4,5 V / @10 V | Q_G (0–4,5 V) | Q_GD | C_RSS | Q_OSS | Q_RR | Gehäuse | Bemerkung | Link |
|---|---|---|---|---|---|---|---|---|---|---|
| Infineon BSZ063N04LS6 | 40 V | 8,8 / 6,3 mΩ | 4,6 nC | 1,3 nC | 12 pF | 10,2 nC | 21 nC | TSDSON-8 FL (3,3 × 3,3) | sehr kleine Gate-Ladung; Lieferbarkeit prüfen (frühere KI: „nicht lieferbar") | [Datenblatt](https://mouser.com/datasheet/2/196/infineon_infn-s-a0008527725-1-1761574.pdf) |
| Infineon BSZ097N04LS G | 40 V | DB prüfen (LTC7800-Beispiel S. 25: 11,4 mΩ, C_MILLER 16 pF) | DB prüfen | – | – | – | – | TSDSON-8 (3,3 × 3,3) | Datenblatt-Beispiel des LTC7800; aktiv, 20 Wochen Herstellerlieferzeit | [Händlerseite](https://www.microchipusa.com/product/infineon-technologies/single-fets-mosfets/BSZ097N04LSGATMA1) · lokal: `01_Quellen/Q70_Infineon_BSZ097N04LSG_MOSFET.pdf` |

### A7 MOSFETs Q101/Q102 – 60-V-Klasse
| Teil | V_DS | R_DS(on) max @4,5 V / @10 V | Q_G (0–4,5 V) | Q_GD | C_RSS | Q_OSS | Q_RR | Gehäuse | Bemerkung | Link |
|---|---|---|---|---|---|---|---|---|---|---|
| Infineon BSZ099N06LS5 | 60 V | 14 / 9,9 mΩ | 6,9 nC typ | 2,0 nC | 15 pF | 13 nC | **6 nC** typ | TSDSON-8 FL (3,3 × 3,3) | kleines Q_RR → guter Kandidat für Q102 | [Datenblatt](https://docs.rs-online.com/540c/A700000007584403.pdf) |
| onsemi NTTFS5C670NL | 60 V | **9,1** / 6,5 mΩ | 9,0 nC | 2,0 nC | 15 pF | DB prüfen | 19 nC | WDFN8 (3,3 × 3,3) | kleinster R_DS(on) bei 4,5 V hier | [Datenblatt](https://www.onsemi.com/pdf/datasheet/nttfs5c670nl-d.pdf) |
| TI CSD18543Q3A | 60 V | 15,6 / 9,9 mΩ | 11,1 nC (Bedingung DB) | 1,7 nC | DB prüfen | DB prüfen | DB prüfen | VSON 3,3 × 3,3 | aktiv | [Datenblatt](https://www.ti.com/lit/gpn/CSD18543Q3A) |
| Nexperia PSMN7R5-60YL | 60 V | DB prüfen (Titel: 7,5 mΩ) | DB prüfen | – | – | – | – | LFPAK56 (sichtbare Beinchen, gut von Hand lötbar) | in Produktion | [Produktseite](https://www.nexperia.com/pip/PSMN7R5-60YL) |
| Infineon BSC100N06LS3 G | 60 V | DB prüfen / 10 mΩ | 45 nC max (0–10 V) | – | – | – | – | SuperSO8 (5 × 6) | Referenz Fig. 13; ältere Generation, große Gate-Ladung, 52 Wochen Lieferzeit → eher nicht | [Datenblatt](https://www.infineon.com/dgdl/BSC100N06LS3_rev2.2.pdf?folderId=db3a30431ddc9372011ebafa04517f8b&fileId=db3a30431ddc9372011ebb0823387fd7) |

### A5 Speicherdrossel L101 (Würth)
| Teil | Serie | L | DCR max | I_R | I_SAT | Maße | Bemerkung | Link |
|---|---|---|---|---|---|---|---|---|
| 74439370150 | WE-XHMI 1510 | 15 µH | 11,55 mΩ | DB prüfen | DB prüfen | 16,4 × 15,4 × 10 mm | SRF 8 MHz; passt zu ≈ 510 kHz | [RS + Datenblatt](https://th.rs-online.com/web/p/surface-mount-inductors/0484749) |
| 78439370150 | WE-XHMA 1510 | 15 µH ±20 % | 10,5 mΩ | 10 A | DB prüfen | 1510 | Automotive-Variante der XHMI | [RS](https://kr.rs-online.com/web/p/surface-mount-inductors/2488309) |
| 744393605150 | WE-XHMI 1010 (Flachdraht) | 15 µH | DB prüfen | 14,9 A | DB prüfen | 11,3 × 10 mm | kleiner | [RS + Datenblatt](https://th.rs-online.com/web/p/surface-mount-inductors/0697709) |
| 744373965150 | WE-LHMI | 15 µH ±20 % | 28 mΩ | 6,8 A | 15 A | 13,5 × 12,5 × 6,2 mm | höhere DCR (≈ 2,5× XHMI) | [Farnell](https://dk.farnell.com/en-DK/wurth-elektronik/744373965150/power-inductor-15uh-shielded-6/dp/3517043) |
| 7447709220 | WE-PD 1210 (Ferrit) | 22 µH ±20 % | 28 mΩ | 5,3 A | **6,5 A** | 12 × 12 × 10 mm | I_SAT knapp über I_PK,max ≈ 5,7 A → eher nicht; günstig (€ 2,48), viel Lager | [Farnell](https://de.farnell.com/en-DE/wurth-elektronik/7447709220/choke-22uh-smd/dp/1635945RL) |
| 74439370220 / 74439370100 | WE-XHMI 1510 | 22 µH / 10 µH | DB prüfen | – | – | 1510 | Kandidaten der früheren KI (für ≈ 370 kHz bzw. höhere f). altKI-Stückliste: 74439370100 = L3 Buck-Drossel (10,4 µH, 7,04 mΩ max, I_SAT,30% 31,2 A); 74439370220 = L1/L2 Eingangsfilter (22 µH, 13,3 mΩ, 8 A) | lokal: `01_Quellen/Q60_WE-XHMI_74439370100_Datenblatt.pdf` · `01_Quellen/Q61_WE-XHMI_74439370220_Datenblatt.pdf` |

### A8 Schottky D102 (parallel zu Q102)
| Teil | V_R | I_F | V_F | Gehäuse | Bemerkung | Link |
|---|---|---|---|---|---|---|
| Nexperia PMEG6030ELP | 60 V | 3 A | 600 mV (Bedingung DB) | SOD128 | für 60-V-Konzept | [Produktseite](https://www.nexperia.com/product/PMEG6030ELP) |
| Diodes DFLS2100 | 100 V | 2 A | DB prüfen | PowerDI123 | in Fig. 15 des LTC7800 verwendet | [Produktseite](https://www.diodes.com/part/view/DFLS2100) |
| Nexperia PMEG4030ER | 40 V | 3 A | DB prüfen | SOD123W | nur für 40-V-Konzept; frühere KI | lokal: `01_Quellen/Q71_Nexperia_PMEG4030ER_Schottky.pdf` |

### A9 Bootstrap-Diode D101
| Teil | V_R | I_F | Gehäuse | Bemerkung | Link |
|---|---|---|---|---|---|
| Vishay BAT46W | 100 V | 150 mA | SOD-123 | Kleinsignal-Schottky | [element14](https://my.element14.com/vishay/bat46w-v-gs08/diode-schottky-0-15a-100v-sod/dp/1612327) |
| 1N4148W (diverse Hersteller) | 100 V | – | SOD-123 | Si-Schaltdiode, wenig Leckstrom, ≈ 0,7 V weniger Gate-Spannung | Hersteller wählen |

### A4 Strommesswiderstand R101
| Teil | R | Toleranz | Leistung | Gehäuse | Link |
|---|---|---|---|---|---|
| Vishay WSL2512R0100FEA | 10 mΩ | 1 % | 1 W | 2512 Metallstreifen | [RS](https://uk.rs-online.com/web/p/surface-mount-resistors/6836559P) · lokal (WSL-Familie): `01_Quellen/Q72_Vishay_WSL_Shunt_Datenblatt.pdf` |
| Vishay WSLT2512R0100FEA | 10 mΩ | 1 % | 1 W | 2512, Hochtemperatur-Variante | [Farnell](https://jp.farnell.com/en-JP/vishay/wslt2512r0100fea/current-sense-res-0r01-1-1-w-2512/dp/2693337) |
| weitere Familien | Bourns CSS/CSS2H, Susumu KRL, Vishay WSK (4-polig) | | | | bei Bedarf suchen |

### A10 Eingangskondensatoren C_IN (X7R)
| Teil | C | U_N | Dielektrikum | Gehäuse | Bemerkung | Link |
|---|---|---|---|---|---|---|
| Murata GRM32ER72A475KE14L | 4,7 µF | 100 V | X7R | 1210 | für 60-V-Konzept | [Murata](https://www.murata.com/en-global/products/productdetail?partno=GRM32ER72A475KE14%23) |
| Murata GRM32ER71K475ME14L | 4,7 µF ±20 % | 80 V | X7R | 1210 | Future: 0 Lager, 30 Wochen | [Future](https://www.futureelectronics.com/p/passives--capacitors--ceramic-capacitors--multilayer-ceramic-capacitors/grm32er71k475me14l-murata-3201810) |
| Murata GRM32ER71H106KA12L | 10 µF ±10 % | 50 V | X7R | 1210 | für 40-V-Konzept | [RS](https://uk.rs-online.com/web/p/mlccs-multilayer-ceramic-capacitors/7236824) |
| Würth WCAP-CSGP 100 V (Familie) | – | 100 V | X7R | diverse | Würth-Alternative | [Würth](https://www.we-online.com/katalog/en/WCAP-CSGP-100VDC) |
Achtung: Murata „…C7…" (z. B. GRM32DC72A475…) ist **X7S** → nicht erlaubt.

---

## Bereich B – Regelung und IC-Beschaltung

| Funktion | Teil | Daten | Link |
|---|---|---|---|
| Controller | ADI LTC7800IUDC#PBF (QFN-20 3 × 4, −40…125 °C) | Datenblatt Rev. F | [Produktseite](https://www.analog.com/en/products/ltc7800.html) · lokal `01_Quellen/Q01_…` |
| C_OUT Keramik | Murata GRM32ER71E226KE15L | 22 µF, 25 V, X7R, 1210 – DC-Bias bei 12 V stark, Kurve prüfen | [Farnell](https://be.farnell.com/en-BE/murata/grm32er71e226ke15l/cap-mlc-22uf-x7r-25v-1210/dp/4540395) |
| C_OUT Keramik | Murata GRM32ER71H106KA12L | 10 µF, 50 V, X7R, 1210 – weniger DC-Bias-Verlust bei 12 V | [RS](https://uk.rs-online.com/web/p/mlccs-multilayer-ceramic-capacitors/7236824) |
| C_OUT Polymer (Option) | KEMET T520/T521, Panasonic POSCAP/SP-Cap | Fig. 15 nutzt KEMET T521 (220 µF, 16 V) | Familie, bei Bedarf suchen |
| Kompensation, Soft-Start | C0G-MLCC 0603/0805 (z. B. Murata GRM/GCM C0G, TDK C0G) | Werte nach B6/B7 | Standardteile |
| C_INTVCC1 | Würth WCAP-CSGP 885012209073 | 10 µF, 50 V, X7R, 1210 (altKI-Stückliste) | lokal `01_Quellen/Q68_WE-MLCC_885012209073_X7R.pdf` |
| C_INTVCC2 | Würth WCAP-CSGP 885012207103 | 1 µF, 50 V, X7R, 0805 (altKI-Stückliste) | lokal `01_Quellen/Q67_WE-MLCC_885012207103_X7R.pdf` |
| C_SS | Würth WCAP-CSGP 885012207098 | 100 nF, 50 V, X7R, 0805 (altKI-Stückliste, t_SS = 8 ms). Laut BOM für C_B zu klein (C_B ≥ 100 · C_iss ≈ 140–190 nF) | lokal `01_Quellen/Q66_WE-MLCC_885012207098_X7R.pdf` |
| Teiler | Dünnschicht 0,1 % (Vishay TNPW, Panasonic ERA, Susumu RG) oder Dickschicht 1 % | E12 | Standardteile |

---

## Bereich C – Eingangsschutz

### C6 TVS-Dioden (bidirektional, SMC)
| Teil | V_R (Standoff) | V_BR | V_C bei I_PP (10/1000 µs) | Leistung | Bemerkung | Link |
|---|---|---|---|---|---|---|
| Würth 824551281 | DB prüfen (28-V-Typ) | 32,75 V min | 45,4 V bei 66,1 A | 3 kW | Kandidat der früheren KI | [RS](https://my.rs-online.com/web/p/tvs-diodes/1624087) · lokal: `01_Quellen/Q64_WE-TVSP_824551281_Datenblatt.pdf` |
| Littelfuse SMDJ33CA | 33 V | 36,7–40,6 V | 53,3 V bei 56,3 A | 3 kW | € 0,79 (50+), 15 Wochen | [Farnell](https://be.farnell.com/littelfuse/smdj33ca/tvs-diode-3kw-33v-bidir-do-214ab/dp/2691616) |
| Littelfuse 5.0SMDJ33CA | 33 V | DB prüfen | DB prüfen | 5 kW | mehr Pulsreserve | [RS](https://kr.rs-online.com/web/p/tvs-diodes/1719461) |
**Wichtig:** Schon bei ≈ 56–66 A klemmen diese TVS auf 45–53 V. Beim Surge (≈ 480 A) liegt die Spannung deutlich höher → **TVS allein reicht für 60-V-FETs (Grenze ≈ 48 V) nicht**; zweistufig (Varistor + Spule + TVS) oder Surge-Stopper/eFuse nötig (C7).

### C6 Varistor
| Teil | U_Varistor | U_DC max | Klemmung | Stoßstrom / Energie | Bauform | Link |
|---|---|---|---|---|---|---|
| Würth 820542501 (WE-VD) | 39 V | 31 V | 77 V bei 10 A | 1 kA / 9,4 J | Scheibe 16,5 mm, THT (4-mm-Sperrzone!) | [RS](https://ie.rs-online.com/web/p/varistors/1633867) · lokal: `01_Quellen/Q63_WE-VD_820542501_Datenblatt.pdf` |

### C5 Überstrom
| Teil | Typ | Daten | Link |
|---|---|---|---|
| Littelfuse 0452004.MRL (NANO2 452) | Sicherung, träge | 4 A, 125 V DC, 50 A Ausschaltvermögen, SMD 2410; weitere Nennströme in der 452-Serie | [element14](https://my.element14.com/littelfuse/0452004-mrl/fuse-smd-4a-slow-blow/dp/2688727) |
| Littelfuse 2920L-Serie, 33-V-Typen (z. B. 2920L260/33) | PTC, rückstellend | Haltestrom/Widerstand im DB prüfen (≥ 1,72 A Halten bei Temperatur) | [Littelfuse](https://www.littelfuse.com/products/fuses-overcurrent-protection/polyswitch-resettable-pptc-devices/surface-mount-polyswitch-resettable-pptc-devices/2920l/2920l260-33) |

### C4–C6 Schutz-ICs
| Teil | Funktion | Kerndaten | Link |
|---|---|---|---|
| ADI LTC4380 | Surge-Stopper | 4–72 V, Klemme 31,5/50 V/einstellbar, Überstrom, Verpolung bis −60 V, externer N-FET | [Mouser](https://www.mouser.co.uk/new/analog-devices/adi-ltc4380-stoppers) |
| ADI LTC4364-2 | Surge-Stopper + Ideal-Diode | Datenblatt lokal | `01_Quellen/Q14_ADI_LTC4364_Datenblatt.pdf` |
| ADI LTC4359 | Ideal-Dioden-Controller | 4–80 V, Verpolung bis −40 V, externer N-FET | [Datenblatt](https://wcm-cce.cldnet.analog.com/media/en/technical-documentation/data-sheets/ltc4359.pdf) |
| ADI MAX17613A | Strombegrenzer mit OV/UV/Verpolung | 4,5–60 V, 0,15–3 A, 130 mΩ, TQFN 4 × 4 | [Datenblatt](https://www-cce.cldnet.analog.com/media/en/technical-documentation/data-sheets/MAX17613A-MAX17613C.pdf) |
| TI TPS2663 | eFuse | 4,5–60 V (67 V abs.), 0,6–6 A, 31 mΩ, IEC 61000-4-5 ausgelegt, Verpolung mit ext. FET | [Datenblatt](https://www.ti.com/lit/gpn/tps2663) |
| TI LM74700-Q1 | Ideal-Dioden-Controller | Daten im DB prüfen | [Produktseite](https://www.ti.com/product/LM74700-Q1) |
| Verpol-/Stopper-FET | 60-V-N-FETs wie in A7 (z. B. BSZ099N06LS5, NTTFS5C670NL) | SOA im DB prüfen | siehe A7 |

---

## Bereich D – Filter, Anschlüsse, LED

### D5 Filterspule L401 (Würth)
| Teil | Serie | L | DCR max | I_R | I_SAT | Maße | Verlust bei 1,72 A | Link |
|---|---|---|---|---|---|---|---|---|
| 74439344022 | WE-XHMI | 2,2 µH ±20 % | 10,5 mΩ | 8 A | 16 A | 6,65 × 6,45 × 2,4 mm | ≈ 31 mW | [Farnell](https://de.farnell.com/en-DE/wurth-elektronik/74439344022/inductor-2-2uh-8a-20-shielded/dp/2666751) |
| 74439324033 | WE-XHMI | 3,3 µH ±20 % | 25,5 mΩ | 7,1 A | 8,2 A | 4,3 × 4,3 × 3 mm | ≈ 75 mW | [Farnell](https://it.farnell.com/en-IT/wurth-elektronik/74439324033/power-inductor-3-3uh-shielded/dp/4413304) |

### D5 Dämpfungs-Elko
| Teil | C | U_N | Typ | Link |
|---|---|---|---|---|
| Würth 865080645012 (WCAP-ASLI) | 47 µF | 50 V | Alu-Elko SMD; ESR/Rippelstrom im DB | [RS](https://uk.rs-online.com/web/p/aluminium-capacitors/1635737) |
| Würth 865080649013 (WCAP-ASLI) | 47 µF | 50 V | andere Baugröße | [RS](https://uk.rs-online.com/web/p/aluminium-capacitors/1635739) |
| Würth 865080543009 (WCAP-ASLI) | 47 µF | **35 V** | Alu-Elko SMD 6,3 × 5,4; altKI-Stückliste C_BULK (4×: 2 am Stopper-OUT, 2 am Buck-Eingang); U_N gegen maximale Klemmspannung prüfen | lokal `01_Quellen/Q65_WCAP-ASLI_865080543009_Datenblatt.pdf` |

### D4 Gleichtaktdrossel CMC1 (Würth)
| Teil | Serie | L | DCR | I_R | Bauform | Bemerkung | Link |
|---|---|---|---|---|---|---|---|
| 744841414 | WE-CMB NiZn | 14 µH | 15 mΩ | 4 A | THT | altKI-Stückliste CMC1; laut 08_Dimensionierung DM-Dämpfung, CM erst nach Layout bewertbar; Alternative WE-CMB HC (0,7 mH) | lokal `01_Quellen/Q62_WE-CMB_744841414_Datenblatt.pdf` |

### Prüfvermerk 12.10.2026 – Filterdrossel und Elko-Spannung (Entscheidung offen)
**Filterdrossel:** 22 µH (frühere KI) und 2,2/3,3 µH (D5) gehören zu zwei verschiedenen Konzepten, beide Werte sind in sich stimmig.
- L1 = 22 µH (74439370220) ist bei der früheren KI das **Surge-Längsglied** zwischen Varistor und TVS (Bereich C). Simulation: Buck-Eingang ≤ 23 V. Ohne L1 muss der Surge neu gerechnet werden.
- L2 bzw. L401 = EMV-Filter. AC-Modell DM (gleiches Modell `D_Filter_Platine/D01_Eingangsfilter/altKI_ac.cir`, Ergebnisse 32,3 dBµV / 0,3 dB / 6,8 dB reproduziert), 500 kHz, Grenze 46 dBµV:
  - L2 = 22 µH, Elko-Dämpfung: Reserve 13,7 dB (mit Elko-ESR max. laut Q65: 11,2 dB). DCR 13,3 mΩ → 39 mW bei 1,72 A.
  - L401 = 3,3 µH (74439324033), C_F = 10 µF effektiv Keramik + Dämpfungs-Elko: 9,5 dB; bei nur 5 µF effektiv 3,1 dB. 25,5 mΩ → 75 mW.
  - L401 = 2,2 µH (74439344022), C_F = 10 µF effektiv + Elko: 5,9 dB; bei 5 µF effektiv −0,5 dB → zu knapp. 10,5 mΩ → 31 mW.
  - Ohne Dämpfungs-Elko: |Z_out| bis 41–45 Ω > |R_IN| = 12,8 Ω → instabil (Middlebrook). Mit Elko ≈ 3,3 Ω.
- Grenzen: nur Gegentakt, keine Layout-Parasitics, nur Grundwelle → Messung entscheidet.

**Elko 865080543009 (47 µF / 35 V, Q65):** V_R = 35 V, V_S = 40,25 V, Z ≤ 530 mΩ (100 kHz), I_Rippel 240 mA, 2000 h bei 105 °C.
- Höchste Spannung am Elko = Stopper-Klemme LTC4364: V_REG,max = 1,28 V · (1 + 100 kΩ / 4,32 kΩ) = 30,9 V (R8 = 4,32 kΩ, ohne R-Toleranz) → 88 % von V_R, Abstand 4,1 V. **35 V reicht nur mit Stopper (Variante B).**
- Ohne Stopper (Variante A, nur TVS 824551281: V_C = 45,4 V bei 66 A) oder bei höherer Klemme → **50 V nötig**.
- Rippelstrom am Buck-Eingang grob 46–61 mA je Elko (Elko parallel zur Keramik, 500 kHz) < 240 mA.

### D2/D6/D7 Stecker, LED, Messpunkte
| Funktion | Teil | Daten | Link |
|---|---|---|---|
| Bananenbuchse PCB | Multicomp Pro 24.243.1 (rot) / 24.243.2 (schwarz) | Kandidat der früheren KI; Strom/Spannung im DB prüfen | [Datenblatt (electrokit)](https://electrokit.com/upload/quick/5d/25/3fca_41022868-tds.pdf) |
| LED-Schalter | Nexperia BSS138BK | 60 V, 360 mA, SOT-23, Logic-Level | [RS](https://ie.rs-online.com/web/p/mosfets/1242289) |
| Status-LED | Würth WL-SMCW (z. B. 150060GS75000, grün 0603) | V_F/Strom im DB | [Würth-Familie](https://www.we-online.com/en/components/products/WL-SMCW) · lokal: `01_Quellen/Q69_WE_150060GS75000_LED_Datenblatt.pdf` |
| Messpunkt SMD | Keystone 5015 | SMD-Testpunkt (keine 4-mm-Sperrzone nötig) | [DigiKey](https://www.digikey.com/en/products/detail/keystone-electronics/5015/278886) |
