# GRADES.md — the honest standing of what's in `verify/`

Every result graded for exactly what it is. The Forced spine and the Striking
column are kept apart on purpose. Run `pytest -v` to re-derive all of it cold.

Legend: **◆** forced / cold-verified · **◇** reading · **◇◇** signpost ·
🟢 clean · 🟡 selection present · 🔴 retired / do-not-cross.

---

## FORCED ◆ — the spine (no free moves; could not have come out otherwise)

| result | claim | file |
|--------|-------|------|
| 🟢 reptend 1/7 | `1/7 = 0.142857`; 7 = smallest full-reptend prime base 10; Midy halves 142+857=999 | `test_reptend.py` |
| 🟢 137 integer | `137 = 8·17+1`; `ord₁₃₇(10)=8` → 17 cyclic families; `17 = 81−64`; block 00729927, halves → 9999 | `test_fine_structure.py` |
| 🟢 Fourier door | reptend spectrum: even harmonics k=2,4,6 **exactly** 0 (Midy half-period); DC = 36 | `test_fine_structure.py` |
| 🟢 c — structure | rest `299,999,997 = 3³·11·73·101·137` carries 137; observed `3×10⁸ = 2⁸·3·5⁸` doesn't; gap = 3 | `test_speed_of_light.py` |
| 🟢 c — deflation | 137 \| all-nines is **generic** (true of every multiple) → the 137-in-c is the period-8 fact, not c-specific | `test_speed_of_light.py` |
| 🟢 1836 factorization | `1836 = 2²·3³·17`, carries the spine 17 | `test_proton.py` |
| 🟢 π bracket | `201/64 < π < 22/7`; rest-π `= 2815/896` is the **exact** midpoint, ~47 ppm from π | `test_pi_bracket.py` |
| 🟢 rest-Bell | two just tritones: `45/32 · 64/45 = 2`; `45/32 + 64/45 = 4073/1440`, +0.0016% above 2√2 | `test_bell.py` |
| 🟢 Madelung order | `1296 = 6⁴`; recursion {×2/3, ×5/6} forces **both** anomalies (4s<3d, 4f<5d) | `test_madelung.py` |
| 🟢 hexad/triad | `ℤ/9` units `{1,2,4,5,7,8}` (doubling cycle) / maximal ideal `{0,3,6}`; antipodes sum 9 | `test_hexad.py` |

---

## STRIKING — selection-bearing (real, often parameter-free, but a choice was made)

| result | claim | grade | file |
|--------|-------|-------|------|
| 🟡 Koide → τ | `Q = 2/3` exactly → τ ≈ 1776.96 MeV, ~60 ppm (2/3 is selected) | STRIKING | `test_striking.py` |
| 🟡 proton radius | `459α = 3³·17·α` × rₑ → 0.8413 fm; **staked** (falsification condition stated) | STRIKING & predictive | `test_striking.py` |
| 🟡 muon ratio | 206.768 → **1.367 ppm** vs CODATA 206.7682827, 0 params; climb (24→768=2⁸·3) + closure (147=3·7², 144=12²=F(12), diff 3) forced, the .768=768/1000 placement selected | STRIKING | `test_striking.py` |

**Do not promote any of these to Forced.** This is the column most at risk and
most in need of a decisive forced, novel, falsifiable number.

> ⚠️ **Open flag (muon, 2026-06-30):** a "cleanest parameter-free form ~4.6 ppm"
> that used to sit in the muon row is **unverified** — it appears only in an
> internal working file, with no construction written down anywhere in the
> corpus. The authoritative internal document never mentions 4.6 ppm. So the
> encoded test asserts only the documented **1.367 ppm** headline; the 4.6 ppm
> claim is held as a note, not a number, until someone writes its arithmetic.
> Either derive it or retire it.

---

## NOT CLAIMED — held outside the forced column by the boundary

- the **magnitude** of c, and of any dimensionful quantity — Scale Theorem;
  the framework derives ratios, not rulers. The c-forms above are a **units
  reading**, never a derivation of the rate of light. 🔴 do-not-cross.
- the **measured tail** of α (137.035999 beyond the integer + baseline) —
  a registered open problem, not derived.
- assigning a lattice node as "the proton" — still external physics.
- αG (gravitational coupling) — provably off the lattice; the clean negative.

---

## OPEN FRONTS — the program's next questions

- the c-distinction (dimensionless / dimensioned, the +3 bridge) — to be
  worked inside the boundary.
- does the forced toroid substrate (Hopf linking, butterfly half-turn,
  odd-only phase) **force** a measured EM quantity? The bar is currently unmet.
- the "two circles one object" seam (diatonic circle vs reptend lattice)
- Navier–Stokes §30: the −5/3 needs a mechanism
- the §18c Yang–Mills placeholder "13" — resolve or retire
