# RhythmSync 🥁

This project is a Python-based application for studying **Sensorimotor Synchronization (SMS)** — the ability to tap in time with rhythmic auditory stimuli.  
It is designed to help researchers investigate the effects of tempo, rhythmic complexity, and musical training on tapping accuracy and consistency.

---

## 🎯 Project Objective

- Present rhythmic stimuli (metronomes, polyrhythms, musical excerpts)
- Allow participants to tap along using the keyboard
- Record precise tap timestamps
- Analyze tapping behavior (mean Inter-Tap Interval, variability)
- Store anonymized participant data
- Enable future analysis of synchronization strength

This project aligns with research interests in **music cognition** and **sensorimotor synchronization**, inspired by the work of Professor Lauren K. Fink.

---

## 🛠 Features

- ✅ Flexible stimuli selection (any `.wav` files)
- ✅ Real-time tapping recording via keyboard (Spacebar)
- ✅ Precise timestamp logging
- ✅ Automatic CSV data export per participant
- ✅ Basic tap analysis (Mean ITI, ITI Variability)
- ✅ Clean, modular Python project structure
- ✅ Easy extension to support practice trials, asynchrony analysis, GUI upgrades

---
---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sms-tapping-app.git
cd sms-tapping-app

python -m venv venv
venv\Scripts\activate   # On Windows

pip install -r requirements.txt

python -m app.main

```
📈 Example Analysis Output

```
--- Tap Analysis ---
Number of Taps        : 30
Mean ITI (seconds)    : 0.9985
ITI Standard Deviation: 0.0521
----------------------
```




