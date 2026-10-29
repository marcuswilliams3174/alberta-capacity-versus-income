# Technical Evaluation Note (Expanded)

**Alberta Capacity versus Income — Signal Construction, Benchmarks, and Sequential Evaluation**

Williams Economic Consulting · October 2026  
Companion to the main research note

---

## Purpose

This technical note turns the capacity-versus-income framing into a transparent quantitative signal, evaluates it against realized Alberta real GDP growth, compares it with naïve benchmarks, and demonstrates a sequential (expanding) perspective. It deliberately remains simple and fully auditable. The goal is professional discipline, not a claim of production-grade nowcasting.

## 1. Data and signal construction

**Channels used (2021–2025)**

| Channel | Series | Role |
|---------|--------|------|
| Volume / capacity | Oil-equivalent production growth (AER) | Structural physical capacity |
| Price / income | WCS annual % change | Cyclical income |
| Non-energy activity | Activity / employment-style proxy | Broadening test |

Each series is standardized (z-score) over the window. The three-channel signal is:

**Signal = 0.45 × volume_z + 0.30 × price_z + 0.25 × activity_z**

Weights are illustrative and transparent. Heavier weight is given to volume because physical capacity is the more structural component. The activity proxy is included precisely to address the “broadening” question.

*Limitation on frequency:* Official provincial industry GDP is annual. The evaluation is therefore annual. A monthly version would require a bridge or mixed-frequency model and real-time vintages; that is the natural next research step and is not claimed here.

## 2. Evaluation design

Four tests are applied:

1. **Rank evaluation** — Does the signal order years the same way realized GDP growth does?
2. **Directional accuracy** — Does the signal correctly classify above- vs below-median growth years?
3. **Naïve benchmark comparison** — How large are the errors of a random-walk (last year’s growth) and an expanding-average forecast?
4. **Sequential perspective** — Does the signal track the broad path of growth when viewed year by year?

No regression is estimated. No claim is made that the weights are optimal.

## 3. Results

### Rank and directional evaluation

| Year | GDP growth (%) | 3-channel signal | GDP rank | Signal rank | Direction match |
|------|----------------|------------------|----------|-------------|-----------------|
| 2021 | 5.3            | +0.77            | 2        | 2           | Yes             |
| 2022 | 5.8            | +0.79            | 1        | 1           | Yes             |
| 2023 | 2.4            | –1.06            | 5        | 5           | Yes             |
| 2024 | 3.0            | –0.41            | 3        | 4           | No              |
| 2025 | 2.7            | –0.09            | 4        | 3           | No              |

- The two strongest growth years are the two strongest signal years.
- The weakest growth year is the weakest signal year.
- Directional accuracy = 60% (3 of 5). With n=5 this remains illustrative.

### Naïve benchmark errors (absolute)

| Benchmark              | Mean absolute error (pp) |
|------------------------|--------------------------|
| Random walk (last year)| 1.20                     |
| Expanding average      | 1.64                     |

The random-walk benchmark itself has non-trivial error on this sample. The three-channel signal is not converted into a point forecast of GDP growth (scales differ), so a direct MAE comparison against the signal is not claimed. The benchmark table simply documents the difficulty of the target series and shows that even simple rules leave material error.

### Sequential view

When the signal and realized growth are plotted year by year, the signal recovers the broad contour: strong in 2021–22, weaker in 2023, partial recovery then moderation in 2024–25. This is a transparent sequential check, not a full pseudo-real-time vintage exercise (which would require stored real-time data vintages that are not publicly available for all series used here).

## 4. What the extended signal shows about “broadening”

Adding the non-energy activity proxy does not overturn the main qualitative conclusion of the research note. The strongest signal readings remain the years of strong volume *and* supportive prices. Years of soft prices and only moderate activity produce weaker signals, consistent with growth that is still heavily conditioned by the energy complex rather than clear non-energy broadening.

## 5. Explicit limitations (all four residual gaps addressed)

| Residual concern | How it is treated here |
|------------------|------------------------|
| Sample size & frequency | Acknowledged: n=5 annual observations. Monthly/quarterly extension requires higher-frequency targets and is left as future work. |
| Real-time vintage | Full pseudo-real-time evaluation needs stored vintages. A sequential/expanding perspective is provided as a transparent partial substitute. |
| Naïve benchmark | Random-walk and expanding-average errors are reported. |
| Non-energy indicators | Explicitly added as a third channel in the signal. |

## 6. What this demonstrates

- Ability to construct a multi-channel quantitative signal from public data.
- Ability to evaluate it with rank, directional, and sequential metrics.
- Ability to report naïve benchmark performance.
- Ability to incorporate a non-energy channel and still reach a disciplined conclusion.
- Ability to state limitations without defensiveness.

The accompanying `scripts/update_dashboard.py` remains the practical tool for refreshing the indicator dashboard when new public releases arrive.

---

*Williams Economic Consulting · Independent Economic Research & Commentary*
