# G-Theory — verification suite

[![tests](https://github.com/thefirsthorstmann/g-theory-verify/actions/workflows/tests.yml/badge.svg)](https://github.com/thefirsthorstmann/g-theory-verify/actions/workflows/tests.yml)

1,410 machine-checked tests, as of 29 October 2026 (one further test reads a laboratory note and skips outside it), underlying the G-Theory research
program: an investigation of dimensionless structure in physics from the arithmetic
relation of 2 and 3, developed with zero adjustable parameters.

```bash
pip install -r requirements.txt
pytest
# 1410 passed, 1 skipped
```

## What green means

Every exact arithmetic claim in the published records re-derives itself, from
stated premises, on your machine. The test source is open to inspection on
precisely the question a careful reader should ask: is any measured value
taken as an input? The inputs are integers, primes, and exact rationals;
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
  silent on any magnitude that requires a chosen unit. One record, *Units on
  Discrete Terms* (§13), states as a hypothesis that a discrete structure names
  the object that carries its one reference, the atomic mass unit; the object's
  magnitude in any outside unit remains the one measurement, and no dimensionful
  magnitude is claimed.

## What is in the box

```
verify/            the suite — each file states its claims in its docstring, in the
                   laboratory's working register, dated
catalog/           the public records' sources, which the batteries pin their text
                   claims against (22 files)
lean/              the forced arithmetic formalized in Lean 4 with Mathlib; `lake build`
                   from `lean/` re-checks it (see lean/README.md)
tools/             the two scripts the batteries call
verify/gtheory.py  the engine: the banked objects and registered choices
verify/stakes.py   pre-registered falsification conditions: every live claim
                   carries a falsification band, an adjudicator, and a horizon;
                   retired claims stay on the record as negatives
GRADES.md          the standing of the results through September 2026; batteries
                   added since carry their grading in their own docstrings
```

Two batteries that the records name read the laboratory's internal ledgers and
run there only: `test_the_lambda_higgs_corollary.py` and `test_the_triad_grading.py`.
Docstring `Source:` lines cite the program's internal working documents; the
public statements of these results are the records below.

## The records

The October 2026 versions, in the intended reading order. Each concept DOI
resolves to the latest version of its record.

| # | work | latest version | concept DOI (resolves to the latest version) |
|---|------|----------------|------------------------------------------------|
| 1 | *G-Theory — An Introduction* | [10.5281/zenodo.23741302](https://doi.org/10.5281/zenodo.23741302) (2026-10-28) | [10.5281/zenodo.21212292](https://doi.org/10.5281/zenodo.21212292) |
| 2 | *Schrödinger's Piano* | [10.5281/zenodo.23740448](https://doi.org/10.5281/zenodo.23740448) (2026-10-28) | [10.5281/zenodo.21211076](https://doi.org/10.5281/zenodo.21211076) |
| 3 | *G-Theory: The Origin on Discrete Terms* | [10.5281/zenodo.23784160](https://doi.org/10.5281/zenodo.23784160) (2026-10-29) | [10.5281/zenodo.21212112](https://doi.org/10.5281/zenodo.21212112) |
| 4 | *The Fine-Structure Constant on Discrete Terms* | [10.5281/zenodo.23740314](https://doi.org/10.5281/zenodo.23740314) (2026-10-28) | [10.5281/zenodo.21211050](https://doi.org/10.5281/zenodo.21211050) |
| 5 | *Navier–Stokes: A Solution on Discrete Terms* | [10.5281/zenodo.21197045](https://doi.org/10.5281/zenodo.21197045) (2026-07-04) | [10.5281/zenodo.21197044](https://doi.org/10.5281/zenodo.21197044) |
| 6 | *π on Discrete Terms* | [10.5281/zenodo.23736568](https://doi.org/10.5281/zenodo.23736568) (2026-10-28) | [10.5281/zenodo.21205368](https://doi.org/10.5281/zenodo.21205368) |
| 7 | *The Seventh — A Constant Hidden in Plain Sight* | [10.5281/zenodo.23740544](https://doi.org/10.5281/zenodo.23740544) (2026-10-28) | [10.5281/zenodo.21206863](https://doi.org/10.5281/zenodo.21206863) |
| 8 | *The Enneagram Is a Theorem* | [10.5281/zenodo.23741392](https://doi.org/10.5281/zenodo.23741392) (2026-10-28) | [10.5281/zenodo.21206948](https://doi.org/10.5281/zenodo.21206948) |
| 9 | *Zero and Infinity on Discrete Terms* | [10.5281/zenodo.23736736](https://doi.org/10.5281/zenodo.23736736) (2026-10-28) | [10.5281/zenodo.21209363](https://doi.org/10.5281/zenodo.21209363) |
| 10 | *The Vanishing Point on Discrete Terms* | [10.5281/zenodo.23740225](https://doi.org/10.5281/zenodo.23740225) (2026-10-28) | [10.5281/zenodo.21209420](https://doi.org/10.5281/zenodo.21209420) |
| 11 | *Predictions on Discrete Terms* | [10.5281/zenodo.23741616](https://doi.org/10.5281/zenodo.23741616) (2026-10-28) | [10.5281/zenodo.21206818](https://doi.org/10.5281/zenodo.21206818) |
| 12 | *Gravity on Discrete Terms* | [10.5281/zenodo.23741462](https://doi.org/10.5281/zenodo.23741462) (2026-10-28) | [10.5281/zenodo.22087599](https://doi.org/10.5281/zenodo.22087599) |
| 13 | *Tonal Function on Discrete Terms* | [10.5281/zenodo.23740755](https://doi.org/10.5281/zenodo.23740755) (2026-10-28) | [10.5281/zenodo.22119146](https://doi.org/10.5281/zenodo.22119146) |
| 14 | *Visible Light on Discrete Terms* | [10.5281/zenodo.23740816](https://doi.org/10.5281/zenodo.23740816) (2026-10-28) | [10.5281/zenodo.22119204](https://doi.org/10.5281/zenodo.22119204) |
| 15 | *Water on Discrete Terms* | [10.5281/zenodo.23740857](https://doi.org/10.5281/zenodo.23740857) (2026-10-28) | [10.5281/zenodo.22119258](https://doi.org/10.5281/zenodo.22119258) |
| 16 | *The Vacuum on Discrete Terms* | [10.5281/zenodo.23740928](https://doi.org/10.5281/zenodo.23740928) (2026-10-28) | [10.5281/zenodo.22119287](https://doi.org/10.5281/zenodo.22119287) |
| 17 | *Motion on Discrete Terms* | [10.5281/zenodo.23741038](https://doi.org/10.5281/zenodo.23741038) (2026-10-28) | [10.5281/zenodo.22119336](https://doi.org/10.5281/zenodo.22119336) |
| 18 | *Units on Discrete Terms* | [10.5281/zenodo.23741718](https://doi.org/10.5281/zenodo.23741718) (2026-10-28) | [10.5281/zenodo.22119360](https://doi.org/10.5281/zenodo.22119360) |
| 19 | *Yang–Mills: Existence on Discrete Terms* | [10.5281/zenodo.23741112](https://doi.org/10.5281/zenodo.23741112) (2026-10-28) | [10.5281/zenodo.22119377](https://doi.org/10.5281/zenodo.22119377) |
| 20 | *QED on Discrete Terms* | [10.5281/zenodo.23741222](https://doi.org/10.5281/zenodo.23741222) (2026-10-28) | [10.5281/zenodo.22119528](https://doi.org/10.5281/zenodo.22119528) |
| 21 | *The Proton and Neutron Masses on Discrete Terms* | [10.5281/zenodo.23785126](https://doi.org/10.5281/zenodo.23785126) (2026-10-29) | [10.5281/zenodo.22217669](https://doi.org/10.5281/zenodo.22217669) |
| 22 | *G-Theory — The Falsification Schedule* | [10.5281/zenodo.23785195](https://doi.org/10.5281/zenodo.23785195) (2026-10-29) | [10.5281/zenodo.22119549](https://doi.org/10.5281/zenodo.22119549) |

Begin at the piano; it asks nothing but a moment's listening.

## Method note

This suite was developed with AI assistance (Anthropic's Claude). Every
assertion is machine-checked, and the author holds sole responsibility for
all claims.

## License

The code in this repository is released under the [MIT License](LICENSE).
The records listed above are separate works and remain all rights reserved.

---

Christian Horstmann · [ORCID 0009-0006-8623-9937](https://orcid.org/0009-0006-8623-9937) · thefirsthorstmann@gmail.com
