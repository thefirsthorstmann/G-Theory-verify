#!/usr/bin/env python3
"""watch_w.py — the standing watch on the equation of state.

The account's position is unhedged and dated: the cosmological term is a
constant of integration, so

    w = -1 exactly, at every redshift, with wa = 0

and there is no second register to retreat to — the frozen-horizon branch,
which would have allowed an evolving term, was withdrawn on 2026-08-18.

The kill condition, banked 2026-08-03, is a CONJUNCTION of three things and
not one:

    sustained (w0, wa) != (-1, 0) at >= 5 sigma
    in TWO independent supernova compilations
    with the low-redshift calibration dispute adjudicated

This tool takes a published pair and returns the verdict on the first
condition, and reminds you that the other two are what actually close it.

    python3 tools/watch_w.py                                  # state and thresholds
    python3 tools/watch_w.py --w0 -0.94 --w0bar 0.03 \
                            --wa -0.4  --wabar 0.25 --label "DESI DR2 + PantheonPlus"
    python3 tools/watch_w.py --compilations 2 --adjudicated

Verdicts are two-sided: a pair can kill the claim by landing far, or support
it by landing close with tight bars.
"""

import argparse
import math

W0, WA = -1.0, 0.0          # the account's position, no free parameter
KILL_SIGMA = 5.0            # banked threshold
NEED_COMPILATIONS = 2       # banked
NEED_ADJUDICATED = True     # banked


def separation(w0, w0bar, wa, wabar):
    """Joint separation from (-1, 0) in sigma, treating the two as
    independent — which is conservative, since the real (w0, wa) contour is
    strongly anticorrelated and a correlated fit separates further."""
    a = (w0 - W0) / w0bar if w0bar else float("inf")
    b = (wa - WA) / wabar if wabar else float("inf")
    return math.hypot(a, b), a, b


def report(label, w0, w0bar, wa, wabar, compilations, adjudicated):
    s, a, b = separation(w0, w0bar, wa, wabar)
    print("  measured   w0 = %+.4f +/- %.4f     wa = %+.4f +/- %.4f" %
          (w0, w0bar, wa, wabar))
    print("  account    w0 = %+.4f              wa = %+.4f   (no free parameter)" %
          (W0, WA))
    print("  pulls      w0 : %+.2f sigma        wa : %+.2f sigma" % (a, b))
    print("  joint separation: %.2f sigma" % s)
    if label:
        print("  source: %s" % label)
    print()
    if s >= KILL_SIGMA:
        print("  FIRST CONDITION MET at %.1f sigma." % s)
        print("  The other two decide it:")
        print("    independent compilations : %d of %d %s" %
              (compilations, NEED_COMPILATIONS,
               "-- MET" if compilations >= NEED_COMPILATIONS else "-- NOT YET"))
        print("    calibration adjudicated  : %s" %
              ("yes -- MET" if adjudicated else "no -- NOT YET"))
        if compilations >= NEED_COMPILATIONS and adjudicated:
            print()
            print("  VERDICT: DEAD. All three conditions met. The coordinate rule")
            print("           is refuted, and with it the constant-of-integration")
            print("           reading of the cosmological term. No fallback exists.")
        else:
            print()
            print("  VERDICT: ON NOTICE. The number is fatal but the conjunction is")
            print("           not complete. This is the state to watch, not to act on.")
    elif s >= 3.0:
        print("  VERDICT: IN TROUBLE at %.1f sigma. One tightening reaches the kill." % s)
    elif max(w0bar, wabar) < 0.02:
        print("  VERDICT: SURVIVES A SHARP TEST. Bars under two hundredths and the")
        print("           position still standing. This is the outcome that counts.")
    else:
        print("  VERDICT: survives, but the bars are too loose to be a test")
        print("           (w0 +/- %.3f, wa +/- %.3f)." % (w0bar, wabar))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--w0", type=float)
    p.add_argument("--w0bar", type=float)
    p.add_argument("--wa", type=float, default=0.0)
    p.add_argument("--wabar", type=float, default=0.0)
    p.add_argument("--label", default="")
    p.add_argument("--compilations", type=int, default=0,
                   help="how many independent SN compilations show it")
    p.add_argument("--adjudicated", action="store_true",
                   help="the low-z calibration dispute is settled")
    a = p.parse_args()

    print()
    print("THE POSITION, unhedged and dated:")
    print("    w = -1 exactly, wa = 0, at every redshift.")
    print("    The cosmological term is a constant of integration, so it cannot")
    print("    evolve. The evolving alternative was withdrawn 2026-08-18 and")
    print("    there is no second register.")
    print()
    print("THE KILL, banked 2026-08-03 -- a conjunction of three:")
    print("    (w0, wa) != (-1, 0) at >= %.0f sigma" % KILL_SIGMA)
    print("    in >= %d independent SN compilations" % NEED_COMPILATIONS)
    print("    with the low-z calibration dispute adjudicated")
    print()

    if a.w0 is None:
        print("NO NUMBER SUPPLIED. Pass --w0 and --w0bar (and --wa/--wabar) to")
        print("get a verdict. What to watch, in order of how slowly it moves:")
        print("    1. the low-z SN calibration dispute -- the actual pivot")
        print("    2. a second independent compilation agreeing with the first")
        print("    3. the joint (w0, wa) contour tightening")
        print()
        print("NOTE ON STALENESS: this repository's cosmological ledger carries")
        print("an explicit OWED-LOOKUP beyond January 2026. Neither the ledger")
        print("nor its author is current. Feed this tool a published pair when")
        print("you see one; do not trust either of us to remember.")
        print()
        return
    report(a.label, a.w0, a.w0bar or 1e-9, a.wa, a.wabar or 1e-9,
           a.compilations, a.adjudicated)
    print()


if __name__ == "__main__":
    main()
