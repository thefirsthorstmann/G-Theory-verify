"""stakes.py — Phase E: THE STAKES REGISTRY, executable.

NOTE (2026-10-04): the "today" strings below are a comparison column, and a comparison
column is re-read from the primary sources at every version of the public registry. The
neutrino, W-mass and ordering rows were brought to October 2026 that day (PDG 2026,
NuFIT 6.1, JUNO); until then they had carried PDG 2024 and NuFIT 5.2 values from the day
this file was written, and the public registry's versions 1 and 2 inherited them. The
canonical current column is the published registry's, pinned in test_the_registry_v3.py.

Every live pre-registered bet, at-risk claim, parked item and retired
seat, as data the test spine can audit: every LIVE stake must carry a
kill-band, an adjudicator and a horizon; every PARKED item a wake
condition; every RETIRED item a reason. The exact seats are recomputed
from their constructions in test_stakes.py — the dashboard cannot
drift from the engine. Supersedes PREDICTION-REGISTRY-2026-06-25 as
the operational page (the registry stands as the graded analysis).
"""

from fractions import Fraction as F

PYTHAGOREAN_COMMA = F(3 ** 12, 2 ** 19)

LIVE = [
    {"name": "PMNS theta23 sin^2", "seat": F(4, 7),
     "today": "Oct 2026: PDG 2026 fit 0.533(18), +2.1 sigma; NuFIT 6.1 best fit 0.470, 3-sigma range to 0.584; octant open (0.572(19) was NuFIT 5.2, 2022, without SK-atm)",
     "kill": "converges off 0.5714 (e.g. > 0.60 or < 0.55)",
     "adjudicator": "DUNE / JUNO / Hyper-K", "horizon": "~2030",
     "grade": "the sharpest pending bet"},
    {"name": "PMNS theta13 sin^2", "seat": F(1, 45),
     "today": "Oct 2026: PDG 2026 0.0217(7), +0.75 sigma; NuFIT 6.1 0.02249(57), -0.47 sigma",
     "kill": "precision excludes 0.02222",
     "adjudicator": "reactor + accelerator precision",
     "horizon": "near-threshold now", "grade": "striking, sharpening"},
    {"name": "proton magnetic radius r_M", "seat": "11/3 - r_e (fm)",
     "today": "field split: dispersive 0.846-0.847 | lattice 0.811",
     "kill": "r_M < ~0.83 (low camp wins)",
     "adjudicator": "muonic-H HFS / dispersive consolidation",
     "horizon": "campaigns underway",
     "grade": "side taken: HIGH; confirm 0.845-0.852"},
    {"name": "proton Zemach radius r_Z", "seat": "hat-shell 2|6|4 -> 1.0922 fm",
     "today": "muonic 1.082(37) | scattering 1.086(12) | e-H 1.045(16)",
     "kill": "r_Z < ~1.04 (kills the hat, wounds the vortex read)",
     "adjudicator": "muonic-H HFS campaigns",
     "horizon": "~0.01 fm precision coming",
     "grade": "confirm 1.08-1.10 separates hat from dipole (1.0626)"},
    {"name": "m_W/m_Z seat pair", "seat": (F(62947, 81000), F(1573, 2025)),
     "today": "Oct 2026: PDG 2026 m_W = 80.3625(77): primary +3.1 sigma (80.3863), rival +0.9 sigma (80.3691); on PDG 2024 the primary stood +0.37 cents = +17 MeV = +1.3 sigma",
     "kill": "CDF-side resolution (ratio > ~0.8820) kills BOTH",
     "adjudicator": "future m_W at +-5 MeV (rivals differ 17 MeV)",
     "horizon": "LHC combination, then FCC-ee class",
     "grade": "side taken: PDG; rival pair 13/1000 vs 1/75 registered"},
    {"name": "Kolmogorov dress: SL vs bend", "seat": (F(17, 10),),
     "today": "SL 1.69594 | bend 1.70000; measured ~1.70",
     "kill": "slope pinned to +-0.005 decides; outside both kills both",
     "adjudicator": "high-Re DNS / atmospheric spectra",
     "horizon": "open", "grade": "registered pair (THE-FIVE-THIRDS)"},
    {"name": "nu mass ordering", "seat": "NORMAL — conditional",
     "today": "Oct 2026: NuFIT 6.1 delta chi2 1.5 to 5.9 (1.2-2.4 sigma); JUNO 207 days >= 2.1 sigma",
     "kill": "inverted ordering established kills the CONDITION's read: "
             "the generation-ordered sevenths assignment (banked)",
     "adjudicator": "DUNE / JUNO", "horizon": "~2030",
     "grade": "F6 promotion: conditional-forced — IF the sevenths ride "
              "generation order (banked assignment), ordering is normal; "
              "the bet rides the assignment, stated as such"},
]

AT_RISK = [
    {"name": "proton charge radius 459 alpha", "seat": "0.84131 fm",
     "today": "CODATA-22 0.84075(64): +0.9 sigma",
     "kill": "outside 0.8398-0.8428"},
    {"name": "W-mass tension resolution", "seat": "PDG side",
     "today": "3.9 sigma PDG-CDF split",
     "kill": "confirmed high m_W convicts the EW seats"},
]

PARKED = [
    {"name": "alpha_G = (5/4) 2^-149",
     "wake": "G measured beyond the current 500 ppm spread "
             "(22 ppm claim unadjudicable today)"},
    {"name": "W split ratio 1.0008 (transit 3/2; 9x139)",
     "wake": "the PDG-CDF tension SURVIVES the final LHC combination"},
    {"name": "glueball ratios (2++/0++ ~ 7/5?, 0-+/0++ ~ 3/2?)",
     "wake": "source re-check of lattice values (memory-flagged)"},
    {"name": "CMB wolf-tone multipole",
     "wake": "a FORCED specific multipole (the current 'lowest ell' "
             "reading is a mood, not a bet — demoted from the decisive "
             "class until the ell is derived)"},
    {"name": "LIV CATASTROPHE WATCH (the registered risk)",
     "wake": "the moment X's Lorentz debts are paid, the payment must "
             "be tested FIRST against Fermi-LAT GRB dispersion and "
             "clock-comparison bounds — any accessible-order deviation "
             "kills the program against data already in hand; this is "
             "the one place a vacuum-catastrophe-class failure could "
             "emerge, registered before it can"},
    {"name": "81/80 syntonic hunt",
     "wake": "a CONSTRUCTION-level appearance (pair-scan empty; the "
             "81-register of the EW skeleton is the next place to look)"},
]

RETIRED = [
    {"name": "sin^2 theta_W = 3/13",
     "reason": "scheme-dependent match; superseded by the on-shell "
               "construction (THE-WHOLE-TONE)"},
    {"name": "391/140 landing",
     "reason": "41% chance-cheap; anatomy retained, seat demoted"},
    {"name": "nu splitting ratio 33.9",
     "reason": "never established as a framework prediction"},
]

RETRODICTIONS = [
    ("muon m_mu/m_e", "206.768", "1.37 ppm"),
    ("Koide -> m_tau", "Q = 2/3", "61 ppm"),
    ("alpha^-1 integer", "137 = 2^7+3^2 = 8x17+1", "integer"),
    ("m_p/m_e integer", "1836 = 2^2 3^3 17 = 36x51", "integer"),
    ("mu_p/|mu_n| seat", "2^37/3^23 = (3/2)/comma^2", "+3.6 ppm"),
    ("Higgs lambda", "2^9/(3^4 7^2) = 0.12900", "prediction-first"),
    ("g_A anatomy", "net 1 | gross 5/3 (SU(6) exact)", "structural"),
]
