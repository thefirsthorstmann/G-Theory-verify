#!/usr/bin/env python3
"""watch.py — the standing watch condition on the magnitude chain.

The chain says, with no unit anywhere and no free parameter:

    frozen comoving horizon diameter / one nucleon's room  =  10^42

which fixes the cell at 8/7 fm, the saturation density at 3*7^3/(2^11 pi),
and the expansion rate at 70.05 km/s/Mpc. Any one of the three decides the
other two. This tool takes a published number and returns the verdict.

    python3 tools/watch.py                      # current state and thresholds
    python3 tools/watch.py --n0 0.164 --bar 0.007
    python3 tools/watch.py --h0 73.17 --bar 0.86
    python3 tools/watch.py --cell 1.1427 --bar 0.023

Verdicts are two-sided: a number can refute the claim by landing far, or
support it by landing close with a tight bar. Both are reported.

The standing comparisons are re-read from their sources at each version of the
gravity record. October 2026: the local-ladder value is SH0ES 2024, 73.17 +/- 0.86
(Breuval et al., Astrophys. J. 973, 30), where the tool quoted 73.04 +/- 1.04.
"""

import argparse
import math

C = 2.99792458e8
MPC = 3.0856775814913673e22
I_SEATS = 4.327363498                       # frozen comoving horizon at the rest values
DEPTH = 1e42

CELL = 8 / 7                             # fm, declared

# The two determinations of the expansion rate that bound the present corridor.
CMB = ("Planck 2018", 67.36, 0.54)
LADDER = ("SH0ES 2024", 73.17, 0.86)
N0 = 3 * 7 ** 3 / (2 ** 11 * math.pi)    # 0.1599321 fm^-3
H0 = 2 * C * I_SEATS / (DEPTH * CELL * 1e-15) * MPC / 1000   # 70.0540


def _from_n0(n0):
    return (3 / (4 * math.pi * n0)) ** (1 / 3)


def _h0_from_cell(cell):
    return 2 * C * I_SEATS / (DEPTH * cell * 1e-15) * MPC / 1000


def corridor(value, bar):
    """The verdict for an expansion rate. The registered condition is not the distance of one
    determination: the microwave-background value and the local ladder disagree with each
    other, so the chain is refuted when the two ladders agree on either end of the corridor
    (the gravity record, section 23, condition 5; the registry, commitment 10)."""
    sigma = abs(value - H0) / bar
    apart = abs(LADDER[1] - CMB[1]) / math.hypot(LADDER[2], CMB[2])
    print("  measured H0 = %.6g +/- %.3g km/s/Mpc" % (value, bar))
    print("  ideal    H0 = %.6g km/s/Mpc   (measured sits %+.2f%% away)" % (H0, (value - H0) / H0 * 100))
    print("  separation: %.2f sigma" % sigma)
    if sigma >= 3:
        print("  VERDICT: this determination alone excludes the chain's value at three sigma.")
    elif sigma >= 2:
        print("  VERDICT: IN TENSION at two sigma with this determination.")
    else:
        print("  VERDICT: consistent with this determination.")
    print("           The registered condition is the convergence of the two ladders:")
    for nm, v, b in (CMB, LADDER):
        print("             %-12s %.2f +/- %.2f stands %.2f sigma from the chain's value" % (nm, v, b, abs(v - H0) / b))
    print("           and the two stand %.2f sigma from each other. The chain is refuted when" % apart)
    print("           the ladders agree on either end of that corridor.")


def verdict(name, value, bar, ideal, unit):
    """Two-sided report against the ideal."""
    sigma = abs(value - ideal) / bar if bar else float("inf")
    frac = (value - ideal) / ideal * 100
    print("  measured %s = %.6g +/- %.3g %s" % (name, value, bar, unit))
    print("  ideal    %s = %.6g %s   (measured sits %+.2f%% away)" % (name, ideal, unit, frac))
    print("  separation: %.2f sigma" % sigma)
    if sigma >= 5:
        print("  VERDICT: REFUTED. The cell at 8/7 is excluded at five sigma.")
    elif sigma >= 3:
        print("  VERDICT: REFUTED at three sigma.")
    elif sigma >= 2:
        print("  VERDICT: IN TENSION at two sigma. One more tightening of the bar decides it.")
    elif bar / ideal < 0.01:
        print("  VERDICT: PASSES A SHARP TEST. The bar is under one percent and the")
        print("           claim stands. This is the outcome that counts.")
    else:
        print("  VERDICT: consistent, but the bar is %.1f%%: too loose to be a test."
              % (bar / ideal * 100))
        need = abs(value - ideal) / 3
        if need > 0:
            print("           A bar of %.4g (%.2f%%) at this centre would be a three-sigma refutation."
                  % (need, need / ideal * 100))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--n0", type=float, help="saturation density, fm^-3")
    p.add_argument("--h0", type=float, help="expansion rate, km/s/Mpc")
    p.add_argument("--cell", type=float, help="packing radius, fm")
    p.add_argument("--bar", type=float, help="one-sigma uncertainty on the value")
    a = p.parse_args()

    if a.n0 is None and a.h0 is None and a.cell is None:
        print("THE CHAIN, with no unit in it and no free parameter:")
        print("    frozen horizon diameter / one nucleon's room = 10^42")
        print()
        print("  cell = 8/7 fm exactly            = %.9f" % CELL)
        print("  n0   = 3 x 7^3 / (2^11 pi)       = %.7f fm^-3" % N0)
        print("       = 3 x 7^4 / 45040 in the rest-pi register (exactly rational)")
        print("  H0                                = %.4f km/s/Mpc" % H0)
        print()
        print("STANDING COMPARISONS:")
        for nm, v, b, kind in (("chiral EFT (Drischler+ 2019)", 0.164, 0.007, "n0"),
                               ("Skyrme EDF survey", 0.160, 0.010, "n0"),
                               CMB + ("h0",), LADDER + ("h0",)):
            ideal = N0 if kind == "n0" else H0
            print("  %-30s %8.4f +/- %-7.4f -> %.1f sigma"
                  % (nm, v, b, abs(v - ideal) / b))
        print()
        print("REFUTATION THRESHOLDS on the saturation density (three sigma):")
        for bar in (0.007, 0.005, 0.003, 0.002, 0.0016, 0.0013):
            print("  bar +/-%.4f (%.1f%%) -> refuted if the centre is outside %.4f - %.4f"
                  % (bar, bar / N0 * 100, N0 - 3 * bar, N0 + 3 * bar))
        print()
        print("  The sentence that refutes it: \"we obtain n0 = 0.164 +/- 0.0013\".")
        print("  At today's centre a 0.8% bar is a three-sigma refutation, and 0.8% is")
        print("  inside what the next chiral order is aiming at.")
        return

    bar = a.bar
    print()
    if a.n0 is not None:
        if bar is None:
            bar = 0.007
        verdict("n0", a.n0, bar, N0, "fm^-3")
        print()
        print("  translated: this density puts the cell at %.4f fm and demands H0 = %.2f"
              % (_from_n0(a.n0), _h0_from_cell(_from_n0(a.n0))))
    elif a.cell is not None:
        if bar is None:
            bar = 0.02
        verdict("cell", a.cell, bar, CELL, "fm")
        print()
        print("  translated: this cell demands H0 = %.2f and n0 = %.5f"
              % (_h0_from_cell(a.cell), 3 / (4 * math.pi * a.cell ** 3)))
    else:
        if bar is None:
            bar = 1.0
        corridor(a.h0, bar)
        cell = 2 * C * I_SEATS / (DEPTH * 1e-15) * MPC / 1000 / a.h0
        print()
        print("  translated: this rate demands a cell of %.4f fm and n0 = %.5f fm^-3"
              % (cell, 3 / (4 * math.pi * cell ** 3)))
        print("  (the accepted saturation range 0.150-0.170 spans H0 = 68.6 to 71.5)")
    print()


if __name__ == "__main__":
    main()
