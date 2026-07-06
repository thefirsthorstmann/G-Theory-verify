"""test_color.py — the triad-circuit color object, pinned."""

from fractions import Fraction as F

from color import (ARC, VERTICES, anti, charge_sum_with_legs, circuit,
                   colored_set, gluons)


def test_the_plate_circuit_is_spin_one():
    c = circuit("u", "u", "d")               # (+2/3)+(+2/3)+(-1/3)
    assert c["net"] == 1 and c["degrees"] == 360 and c["closed"]


def test_two_closure_modes():
    assert circuit("u", "u", "d")["net"] == 1     # proton -> 360 face
    assert circuit("u", "d", "d")["net"] == 0     # neutron -> 0 face
    assert circuit("u", "d", "d")["closed"]       # both observable


def test_confinement_no_open_arcs():
    assert not circuit("u")["observable"]         # a lone quark is open
    assert not circuit("u", "u")["observable"]
    assert circuit("u", anti("u"))["observable"]  # meson: arc + counter-arc


def test_gluon_count_is_eight():
    g = gluons()
    assert g["count"] == 3 * 3 - 1 == 8


def test_colored_set_is_derived():
    assert colored_set() == {"Q", "g"}            # was [input]; now supplied


def test_anomaly_closure_via_three_legs():
    assert charge_sum_with_legs() == 0            # 3(2/3 - 1/3) - 1 + 0


def test_vertices_are_the_triad():
    assert VERTICES == (3, 6, 9)
    assert all(ARC[q] == F(2, 3) for q in ("u", "c", "t"))
    assert all(ARC[q] == F(-1, 3) for q in ("d", "s", "b"))
