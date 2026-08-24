# G-Theory — verification suite

[![tests](https://github.com/thefirsthorstmann/g-theory-verify/actions/workflows/tests.yml/badge.svg)](https://github.com/thefirsthorstmann/g-theory-verify/actions/workflows/tests.yml)

1,009 machine-checked assertions underlying the G-Theory research program: an
investigation of dimensionless structure in physics from the arithmetic
relation of 2 and 3, developed with zero adjustable parameters.

```bash
pip install -r requirements.txt
pytest
# 1009 passed
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

- **Gravity on Discrete Terms** (August 2026) — gravitation as the tonal
  center of a discrete harmonic system; the anomalies, the coupling, and a
  dimensionless cosmological ratio. The `test_the_*` and `test_gravity_*`
  batteries in this suite are its section-24 claim map, and
  `catalog/GRAVITY-AS-TONAL-CENTER.md` is the paper source they pin.

In the intended reading order:

| # | work | DOI |
|---|------|-----|
| 1 | *G-Theory — An Introduction* | [10.5281/zenodo.21212293](https://doi.org/10.5281/zenodo.21212293) |
| 2 | *Schrödinger's Piano* — the thought experiment | [10.5281/zenodo.21270357](https://doi.org/10.5281/zenodo.21270357) |
| 3 | *G-Theory: The Origin on Discrete Terms* — the theory, in twelve volumes | [10.5281/zenodo.21432752](https://doi.org/10.5281/zenodo.21432752) |
| 4 | *The Fine-Structure Constant on Discrete Terms* | [10.5281/zenodo.21211051](https://doi.org/10.5281/zenodo.21211051) |
| 5 | *Navier–Stokes: A Solution on Discrete Terms* | [10.5281/zenodo.21197045](https://doi.org/10.5281/zenodo.21197045) |
| 6 | *π on Discrete Terms* | [10.5281/zenodo.21205369](https://doi.org/10.5281/zenodo.21205369) |
| 7 | *Sevenths — A Constant Hidden in Plain Sight* | [10.5281/zenodo.21432733](https://doi.org/10.5281/zenodo.21432733) |
| 8 | *The Enneagram Is a Theorem* | [10.5281/zenodo.21270991](https://doi.org/10.5281/zenodo.21270991) |
| 9 | *Zero and Infinity on Discrete Terms* | [10.5281/zenodo.21209364](https://doi.org/10.5281/zenodo.21209364) |
| 10 | *The Vanishing Point on Discrete Terms* | [10.5281/zenodo.21209421](https://doi.org/10.5281/zenodo.21209421) |
| 11 | *Predictions on Discrete Terms* — the registered predictions | [10.5281/zenodo.21206819](https://doi.org/10.5281/zenodo.21206819) |

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
