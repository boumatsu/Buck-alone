# Anleitung für KI-Assistenten

Persönliches Arbeits-Repo: Ein Mensch (der Nutzer) arbeitet hier mit ein bis zwei KI-Assistenten. Diese Datei gilt für jede KI, die hier mitarbeitet – im Moment **Claude** und **DeepSeek**.

**KI mit Repo-Zugriff** (Agenten-Werkzeug, das Dateien lesen, ändern und committen kann): Abschnitt 0 komplett selbst ausführen.

**KI ohne Repo-Zugriff** (reiner Chat): Der Nutzer gibt diese Datei, `STATUS.md`, die README des Bereichs und die nötigen Dateien in den Chat. Die KI
- arbeitet nur mit dem, was im Chat liegt, und sagt, welche Datei ihr fehlt, statt Inhalte zu raten;
- liefert neue oder geänderte Dateien **vollständig**, mit Dateiname nach Abschnitt 3 und Zielordner;
- gibt am Ende einen fertigen Übergabe-Block für `STATUS.md` aus, den der Nutzer einfügt.

## 0 Arbeitsweise mit mehreren KIs
**Vor Beginn**
1. `git pull` – mit dem neuesten Stand arbeiten.
2. `STATUS.md` lesen und sich unter „In Arbeit“ eintragen (KI-Name, Ordner, Ziel). Steht dort schon eine andere KI im selben Ordner: nicht dort arbeiten, sondern den Nutzer fragen.

**Während der Arbeit**
- Eine KI arbeitet in **einem** Themenordner. Gemeinsame Dateien (`00_Projekt/00_Projektkontext.md`, `01_Quellen/01_Quellen_ApplicationNotes.md`, `03_Stueckliste/*`, `STATUS.md`) nur in kleinen Schritten ändern und direkt davor `git pull`.
- Kleine Commits, Nachricht mit Ordnerkürzel: `A03: Verluste BSZ097 gerechnet`.
- Nie `git push --force`, nie die Historie umschreiben, keine Dateien einer anderen Sitzung löschen.
- Entscheidungen trifft der Nutzer: Optionen mit Trade-offs und Zahlen vorlegen, nicht selbst festlegen. Getroffene Entscheidungen in `00_Projekt/00_Projektkontext.md` §9 eintragen, offene Fragen an den Prof in §10.

**Am Ende**
1. Ergebnisse in die Tabelle „Ergebnisse“ der Bereichs-README eintragen.
2. In `STATUS.md` eine Übergabe schreiben (was erledigt, was offen, welche Dateien geändert) und die Zeile unter „In Arbeit“ entfernen.
3. Committen und pushen.

Hinweis: `00_Projektkontext.md` beschreibt das Gruppenprojekt (z. B. F5 „Wer übernimmt A–D?“). In diesem Repo arbeitet der Nutzer alle Bereiche selbst.

## 1 Zuerst lesen
1. `README.md` (Überblick) und `STATUS.md` (Stand, Übergaben)
2. `00_Projekt/00_Projektkontext.md` (Anforderungen, Regeln, Schnittstellen zwischen den Bereichen)
3. `00_Projekt/Designablauf.md` (Reihenfolge des Entwurfs, Abhängigkeiten, was LTC7800, MOSFETs und die Blöcke davor und danach brauchen) – **nicht** an einem Schritt arbeiten, dessen Voraussetzungen dort noch offen sind, ohne den Nutzer darauf hinzuweisen
4. `README.md` des Bereichs, an dem gearbeitet wird, und dessen Arbeitsanleitung (`A_Leistungsstufe.md`, `B_Regelung_und_IC-Beschaltung.md`, `C_Eingangsschutz.md`, `D_Filter_Anschluesse_Platine_Zusammenfuehrung.md`)
5. Bei Bedarf `01_Quellen/01_Quellen_ApplicationNotes.md` (Quellen mit Kürzel Q01…Q72) und `03_Stueckliste/02_Bauteilkandidaten.md`

## 2 Wo liegt was
| Was | Wo |
|---|---|
| Anforderungen, Regeln, Entscheidungen | `00_Projekt/` |
| Datenblätter, Application Notes | `01_Quellen/` (Dateiname beginnt mit der Q-Nummer) |
| LTspice-/KiCad-Modelle | `02_Modelle/` |
| Stückliste, Bauteilkandidaten, Budget | `03_Stueckliste/` (eine gemeinsame Liste) |
| Schaltplan, Layout | `04_Schaltplan_Layout/` |
| Arbeit eines Bereichs | `A_…`, `B_…`, `C_…`, `D_…` → Themenordner (Zuordnung zu den Schritten der Anleitung in der README des Bereichs) |
| Simulation des ganzen Wandlers | `06_Simulation_Gesamt/` |

## 3 Dateinamen
`<Themenordner-Kürzel>_<Art>_<Inhalt>[_<JJJJ-MM-TT>].<Endung>`
- Art: `rechnung`, `sim`, `vergleich`, `notiz`, `messung`
- Keine Namen oder andere persönliche Daten in Dateinamen und Dateien.
- Beispiele: `A03_rechnung_Verluste_BSZ097.md`, `C04_sim_Surge_1kV.asc`, `D01_notiz_Filter_2026-10-14.pdf`

## 4 Regel für `altKI_`-Dateien
Dateien mit Präfix `altKI_` stammen aus einer früheren KI-Sitzung. Sie sind **ungeprüft** und teils widersprüchlich.
- **Nicht** als Ausgangspunkt oder Vorgabe verwenden.
- Erst selbst rechnen bzw. simulieren, danach vergleichen. Abweichungen nennen und begründen.
- Keinen Wert daraus übernehmen, der nicht mit Datenblatt (Seite, Revision) oder eigener Rechnung belegt ist.

## 5 Arbeitsregeln
- Bauteilregeln aus `00_Projektkontext.md` §2: Widerstände E12, Keramik nur X7R/C0G, SMD ≥ 0603, Spulen nur Würth, jedes Teil bei 2 europäischen Händlern mit Datum.
- Rechnungen vollständig herleiten, Einheiten in jedem Schritt, Worst Case mit Min/Max, Datenblattwerte mit Seite und Revision.
- LTspice: Modelle nur mit **relativen** Pfaden einbinden (`..\..\02_Modelle\…`). LTspice-eigene Modelle ohne Pfad (`.lib LTC7800.sub`). Ergebnisdateien (`.raw`, `.log`) werden nicht eingecheckt.
- Ergebnisse in die Tabelle „Ergebnisse“ der Bereichs-README eintragen, Bauteile nur in `03_Stueckliste/`.
- Dateien anderer Bereiche nur ändern, wenn darum gebeten wurde; Schnittstellenwerte (00 §8) mit dem anderen Bereich abstimmen.
- Neue Quellen: nächste freie Q-Nummer, PDF nach `01_Quellen/`, Eintrag in die Quellenliste.

## 6 Werkzeuge
- **Simulation: LTspice.** Alle Simulationsnachweise in LTspice (`.asc` bevorzugt, `.cir` erlaubt). LTC7800 und LTC4364 sind in LTspice enthalten; weitere Modelle aus `02_Modelle/LTspice/`. Python oder ngspice nur für Hilfsrechnungen (z. B. Parameter-Sweeps, Auswertung), **nicht** als Nachweis.
- **Schaltplan und PCB: KiCad.** Projekt in `04_Schaltplan_Layout/`, Bibliotheken in `02_Modelle/KiCad/`. Footprints immer gegen die Gehäusezeichnung im Datenblatt prüfen.
- Andere Programme nur nach Rücksprache mit dem Nutzer.
