# G-Theory — verification suite

[![tests](https://github.com/thefirsthorstmann/g-theory-verify/actions/workflows/tests.yml/badge.svg)](https://github.com/thefirsthorstmann/g-theory-verify/actions/workflows/tests.yml)

1,161 machine-checked assertions underlying the G-Theory research program: an
investigation of dimensionless structure in physics from the arithmetic
relation of 2 and 3, developed with zero adjustable parameters.

```bash
pip install -r requirements.txt
pytest
# 1161 passed
```

## What green means

Every exact arithmetic claim in the published papers re-derives itself, from
stated premises, on your machine. The test source is open to inspection on
precisely the question a careful reader should ask: is any measured value
smuggled in as an input? The inputs are integers, primes, and exact rationals;
where a measured value appears, it appears only on the right-hand side of a
comparison, as the thing being tested against.

## What green does not mean

A passing suite does not mean the physical readings are true. Every result
carries a grade, and the grades are kept apart on purpose — see
[GRADES.md](GRADES.md). In particular:

- The **Forced** column is structural arithmetic: results that could not have
  come out otherwise. This is what the suite pins.
- The **Striking** column holds the well-known numerical results. They are
  real and parameter-free, but each involves a selection made in the
  construction, and the grading says so explicitly. Striking is not Forced,
  and nothing here promotes it.
- The framework derives **ratios, not rulers**: by its own Scale Theorem it is
  silent on any quantity that requires a chosen unit. No dimensionful
  magnitude is claimed.

## What is in the box

```
verify/            the suite — each file states its claims in its docstring
catalog/           the paper source a battery pins its text claims against
verify/gtheory.py  the engine: the banked objects and registered choices
verify/stakes.py   pre-registered falsification conditions: every live claim
                   carries a falsification band, an adjudicator, and a horizon;
                   retired claims stay on the record as negatives
GRADES.md          the standing of every result, graded for exactly what it is
```

Docstring `Source:` lines cite the program's internal working documents; the
public statements of these results are the papers below.

## The papers

- **Gravity on Discrete Terms** (August 2026, DOI 10.5281/zenodo.22087600) — gravitation as the tonal
  center of a discrete harmonic system; the anomalies, the coupling, and a
  dimensionless cosmological ratio. The `test_the_*` and `test_gravity_*`
  batteries in this suite are its section-24 claim map, and
  `catalog/GRAVITY-AS-TONAL-CENTER.md` is the paper source they pin.

- **Tonal Function on Discrete Terms** (August 2026) — the diatonic
  functions derived from the arithmetic of the seats: the unique-root
  theorem, the two joints, the mirror, and the cadence's ledger.
  `verify/test_tonal_function.py` is its battery, and
  `catalog/TONAL-FUNCTION-ON-DISCRETE-TERMS.md` is the paper source.

- **Predictions on Discrete Terms, version 2** (August 2026, DOI
  [10.5281/zenodo.22118840](https://doi.org/10.5281/zenodo.22118840)) —
  the registry gains the gravitational sector: three live stakes and five
  exact nulls, added under the registry's additive conduct rules.
  `verify/test_the_registry_v2.py` pins the new rows against
  `catalog/PREDICTIONS-ON-DISCRETE-TERMS.md`.

- **Visible Light on Discrete Terms** (August 2026) — the band that
  spans less than an octave, the circle that closes by mixing, and the
  wheel of hues from the arithmetic of one seventh: complements from the half turn
  (Midy), the additive and subtractive triads as residues and
  non-residues, white by addition and black by subtraction, both exact.
  `verify/test_the_color_wheel.py` is its battery, and
  `catalog/VISIBLE-LIGHT-ON-DISCRETE-TERMS.md` is the paper source.

- **Water on Discrete Terms** (August 2026) — the two-liquid science read
  on discrete terms: the tetrahedral third exact, Faraday's half-frequency
  response pinned by direct integration, the exclusion-zone literature
  engaged with its critical review, and four falsifiable questions offered
  to the laboratory. `verify/test_water_terms.py` is its battery, and
  `catalog/WATER-ON-DISCRETE-TERMS.md` is the paper source.

- **The Origin on Discrete Terms, version 2** (August 2026, DOI
  [10.5281/zenodo.22119129](https://doi.org/10.5281/zenodo.22119129)) —
  the flagship gains an interlude between Volumes IV and V, "The forces,
  in order of appearance": the four interactions dated inside the
  unfolding, gravitation seated as the register's reference level, its
  mechanism imported from the gravity paper by citation.
  `verify/test_the_forces_interlude.py` pins it against
  `catalog/THE-ORIGIN-ON-DISCRETE-TERMS.md`.

- **G-Theory — An Introduction, version 2** (August 2026, DOI
  [10.5281/zenodo.22121665](https://doi.org/10.5281/zenodo.22121665)) —
  the front door notes the gravitational account on the record and the
  shelf grows to fifteen rows. `verify/test_the_introduction_v2.py` pins
  it against `catalog/G-THEORY-AN-INTRODUCTION.md`.

- **The Vacuum on Discrete Terms** (August 2026) — the cosmological term
  as a boundary count: sign and sourcing derived, w = −1 exactly as a
  constant of integration, the fraction at the seat 2/3 with the excess
  as a clock reading. `verify/test_vacuum_campaign.py` is its battery,
  and `catalog/THE-VACUUM-ON-DISCRETE-TERMS.md` is the paper source.

- **Motion on Discrete Terms** (August 2026) — inertia, the speed limit,
  the quadratic form of kinetic energy, and conservation from the
  register's own operations. `verify/test_motion.py`,
  `verify/test_the_orbital_account.py` and `verify/test_two_riders.py`
  are its batteries; `catalog/MOTION-ON-DISCRETE-TERMS.md` is the source.

- **Units on Discrete Terms** (August 2026) — what a unit is, the
  dimensional boundary, the classes of constants, and the placement of
  the one required reference; §12b places the companion's G.
  `verify/test_decimal_wheel.py`, `verify/test_leverage.py`,
  `verify/test_path_length.py`, `verify/test_rotation_quantum.py` and
  `verify/test_semitone_seam.py` are its batteries;
  `catalog/UNITS-ON-DISCRETE-TERMS.md` is the source.

- **Yang–Mills: Existence on Discrete Terms** (July 2026, posted August
  2026) — the second prosecution: instantiation as a supertask on three
  meters, the gap graded (theorem, measurement, supplied ruler), and the
  13b mechanism addendum; the paper's own fifty-finding adversarial
  review ledger ships beside it
  (`catalog/YM-REVIEW-LEDGER-2026-07-12.json`).
  `verify/test_yang_mills_gap.py` and `verify/test_ym_gap.py` are its
  batteries; `catalog/YANG-MILLS-ON-DISCRETE-TERMS.md` is the source.

- **QED on Discrete Terms** (August 2026) — renormalization with a
  deepest reachable cell: the running as count with depth, bare and
  dressed as the two-tier reading, the integer 137 derived and the
  placement honestly open, 137.036 excluded by measurement and stated
  so. `verify/test_qed_on_discrete_terms.py` is its battery;
  `catalog/QED-ON-DISCRETE-TERMS.md` is the source.

- **The Falsification Schedule** (August 2026) — every standing exposure
  of the series with the instrument and the date; the registry
  (Predictions v2) canonical wherever a number is staked.
  `catalog/THE-FALSIFICATION-SCHEDULE.md` is the source.

In the intended reading order:

| # | work | DOI |
|---|------|-----|
| 1 | *G-Theory — An Introduction* | [10.5281/zenodo.22121665](https://doi.org/10.5281/zenodo.22121665) |
| 2 | *Schrödinger's Piano* — the thought experiment | [10.5281/zenodo.21270357](https://doi.org/10.5281/zenodo.21270357) |
| 3 | *G-Theory: The Origin on Discrete Terms* — the theory, in twelve volumes | [10.5281/zenodo.22119129](https://doi.org/10.5281/zenodo.22119129) |
| 4 | *The Fine-Structure Constant on Discrete Terms* | [10.5281/zenodo.21211051](https://doi.org/10.5281/zenodo.21211051) |
| 5 | *Navier–Stokes: A Solution on Discrete Terms* | [10.5281/zenodo.21197045](https://doi.org/10.5281/zenodo.21197045) |
| 6 | *π on Discrete Terms* | [10.5281/zenodo.21205369](https://doi.org/10.5281/zenodo.21205369) |
| 7 | *Sevenths — A Constant Hidden in Plain Sight* | [10.5281/zenodo.21432733](https://doi.org/10.5281/zenodo.21432733) |
| 8 | *The Enneagram Is a Theorem* | [10.5281/zenodo.21270991](https://doi.org/10.5281/zenodo.21270991) |
| 9 | *Zero and Infinity on Discrete Terms* | [10.5281/zenodo.21209364](https://doi.org/10.5281/zenodo.21209364) |
| 10 | *The Vanishing Point on Discrete Terms* | [10.5281/zenodo.21209421](https://doi.org/10.5281/zenodo.21209421) |
| 11 | *Predictions on Discrete Terms* — the registered predictions | [10.5281/zenodo.22118840](https://doi.org/10.5281/zenodo.22118840) |
| 12 | *Gravity on Discrete Terms* | [10.5281/zenodo.22087600](https://doi.org/10.5281/zenodo.22087600) |
| 13 | *Tonal Function on Discrete Terms* | [10.5281/zenodo.22119147](https://doi.org/10.5281/zenodo.22119147) |
| 14 | *Visible Light on Discrete Terms* | [10.5281/zenodo.22119205](https://doi.org/10.5281/zenodo.22119205) |
| 15 | *Water on Discrete Terms* | [10.5281/zenodo.22119259](https://doi.org/10.5281/zenodo.22119259) |
| 16 | *The Vacuum on Discrete Terms* | [10.5281/zenodo.22119288](https://doi.org/10.5281/zenodo.22119288) |
| 17 | *Motion on Discrete Terms* | [10.5281/zenodo.22119337](https://doi.org/10.5281/zenodo.22119337) |
| 18 | *Units on Discrete Terms* | [10.5281/zenodo.22119361](https://doi.org/10.5281/zenodo.22119361) |
| 19 | *Yang–Mills: Existence on Discrete Terms* | [10.5281/zenodo.22119378](https://doi.org/10.5281/zenodo.22119378) |
| 20 | *QED on Discrete Terms* | [10.5281/zenodo.22119529](https://doi.org/10.5281/zenodo.22119529) |
| 21 | *G-Theory — The Falsification Schedule* | [10.5281/zenodo.22119550](https://doi.org/10.5281/zenodo.22119550) |

Begin at the piano; it asks nothing but a moment's listening.

## Method note

This suite was developed with AI assistance (Anthropic's Claude). Every
assertion is machine-checked, and the author holds sole responsibility for
all claims.

## License

The code in this repository is released under the [MIT License](LICENSE).
The papers listed above are separate works and remain all rights reserved.

---

Christian Horstmann · [ORCID 0009-0006-8623-9937](https://orcid.org/0009-0006-8623-9937) · thefirsthorstmann@gmail.com
