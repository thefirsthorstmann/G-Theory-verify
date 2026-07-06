"""test_projection.py — F3 pinned: the grammar validates, and rejects."""

import pytest
from fractions import Fraction as F

from projection import (CANON, MU_RATIO, MW_OVER_MZ, apply_unfolding,
                        validate)


def test_all_canonical_projections_validate():
    """The four corpus templates are well-formed and recompute."""
    for p in CANON:
        assert validate(p)


def test_the_mu_ratio_recomputes_exactly():
    """(3/2) / comma^2 = 2^37/3^23 — exact through the grammar."""
    got = apply_unfolding(MU_RATIO["rest"], MU_RATIO["unfolding"])
    assert got == F(2 ** 37, 3 ** 23)


def test_the_ew_projection_recomputes_through_the_port():
    """(8/9)^2 - 13/1000 then the sqrt port -> 0.8815461..."""
    got = apply_unfolding(MW_OVER_MZ["rest"], MW_OVER_MZ["unfolding"])
    assert abs(got - 0.8815460605040008) < 1e-12


def test_bare_numbers_are_rejected():
    """A claim without an address is not claimable."""
    bare = dict(MW_OVER_MZ)
    bare["address"] = []
    with pytest.raises(AssertionError):
        validate(bare)


def test_off_vocabulary_addresses_are_rejected():
    """'because we say so' fails the grammar."""
    vague = dict(MU_RATIO)
    vague["address"] = ["a nice number we like"]
    with pytest.raises(AssertionError):
        validate(vague)


def test_wrong_face_is_rejected():
    """An operation cannot wear the wrong face (A2 enforced)."""
    wrong = dict(MU_RATIO)
    wrong["unfolding"] = [("dress-mul", F(1, 2), "M", "mislabeled")]
    with pytest.raises(AssertionError):
        validate(wrong)


def test_non_recomputing_unfoldings_are_rejected():
    """The arithmetic must fold from rest to in-system, exactly."""
    broken = dict(MU_RATIO)
    broken["in_system"] = F(3, 2)
    with pytest.raises(AssertionError):
        validate(broken)


def test_missing_least_action_is_rejected():
    """Every selection must stand its trial."""
    lazy = dict(MW_OVER_MZ)
    lazy["least_action"] = ""
    with pytest.raises(AssertionError):
        validate(lazy)


def test_the_crown_jewels_are_well_formed():
    """Worst-case #2 answered: the muon, the 1836, and the 137 rendered as
    well-formed projections — selection QUANTIFIED, not merely acknowledged
    (muon: 1-of-6, p ~ 6.8e-4 with the post-hoc caveat; 1836: the 1800
    rival on the record; 137: additive form weighed as abundant, the block
    load-bearing)."""
    from projection import ALPHA_137, MUON, PROTON_1836, validate
    for p in (MUON, PROTON_1836, ALPHA_137):
        assert validate(p)


def test_the_muon_composite_field():
    """The six wheel composites, exact; the pick is wheel-5; the
    nearest rival composite sits 0.256 away — vs a 0.000283 hit."""
    from gtheory import wheel_scales
    meet = wheel_scales()["meet"]
    comps = {v: d + u / 1000 for v, (d, u) in meet.items()}
    assert len(comps) == 6
    assert abs(comps[5] - 206.768) < 1e-12
    others = sorted(abs(c - 206.768) for v, c in comps.items() if v != 5)
    assert others[0] > 0.25


def test_the_1836_rival_field():
    """Banked-vocabulary products within +-2% of 1836: exactly the
    convergent triple at 1836 and the single clean rival 1800."""
    vocab = [12, 15, 17, 24, 27, 36, 42, 51, 57, 66, 75, 99, 108, 144,
             153, 207]
    hits = {}
    for i, a in enumerate(vocab):
        for b in vocab[i:]:
            if abs(a * b - 1836) / 1836 < 0.02:
                hits.setdefault(a * b, []).append((a, b))
    assert set(hits) == {1800, 1836}
    assert len(hits[1836]) == 3 and len(hits[1800]) == 1


def test_the_137_cheap_and_strong():
    """The additive class is abundant by chance (five hits in [120,155]); the block
    is exact — the audit separates decoration from load-bearer."""
    from gtheory import expansion_digits
    adds = sorted(2 ** a + 3 ** b for a in range(2, 9)
                  for b in range(0, 6) if 120 <= 2 ** a + 3 ** b <= 155)
    assert len(adds) == 5 and 137 in adds
    assert expansion_digits(1, 137, 8) == "00729927"
