import math

from pifs.proportion import (
    CellRange,
    contained_cells,
    decimal_medium_resonance,
    decimal_zero_certifying_cells,
    exact_binary_quaternary_cell,
    intersecting_cells,
    logarithmic_resonance_pairs,
    required_depth_cover,
    transform_sector,
)


def test_binary_quaternary_exact_identity():
    for L in range(1, 8):
        for a in range(4**L):
            assert exact_binary_quaternary_cell(a, L) == a
            t = transform_sector(a, 4, L, 2, 2 * L)
            assert t.intersect == CellRange(a, a)
            assert t.contained == CellRange(a, a)
            assert t.boundary == 0


def test_decimal_1000_zeros_to_quaternary_cert_cell():
    assert required_depth_cover(10, 1000, 4) == 1661
    t = decimal_zero_certifying_cells(1000, target_base=4)
    assert t.target_depth == 1661
    assert t.contained == CellRange(0, 0)
    assert t.intersect == CellRange(0, 1)
    assert t.boundary == 1


def test_decimal_small_zero_blocks():
    cases = {
        1: (2, CellRange(0, 0), CellRange(0, 1)),
        2: (4, CellRange(0, 1), CellRange(0, 2)),
        3: (5, CellRange(0, 0), CellRange(0, 1)),
        4: (7, CellRange(0, 0), CellRange(0, 1)),
        5: (9, CellRange(0, 1), CellRange(0, 2)),
        6: (10, CellRange(0, 0), CellRange(0, 1)),
    }
    for D, (L4, contained, intersect) in cases.items():
        t = decimal_zero_certifying_cells(D, target_base=4)
        assert t.target_depth == L4
        assert t.contained == contained
        assert t.intersect == intersect


def brute_intersections(a, q, l, q2, l2):
    M = q**l
    N = q2**l2
    out = []
    for b in range(N):
        if b * M < (a + 1) * N and (b + 1) * M > a * N:
            out.append(b)
    return out


def brute_contained(a, q, l, q2, l2):
    M = q**l
    N = q2**l2
    out = []
    for b in range(N):
        if b * M >= a * N and (b + 1) * M <= (a + 1) * N:
            out.append(b)
    return out


def test_against_bruteforce_small_grids():
    for q, l, q2, l2 in [
        (3, 2, 4, 3),
        (10, 1, 4, 2),
        (5, 2, 2, 5),
        (4, 3, 10, 2),
    ]:
        for a in range(q**l):
            inter = intersecting_cells(a, q, l, q2, l2).to_list()
            cont = contained_cells(a, q, l, q2, l2).to_list()
            assert inter == brute_intersections(a, q, l, q2, l2)
            assert cont == brute_contained(a, q, l, q2, l2)


def test_medium_decimal_resonance():
    r = decimal_medium_resonance()
    assert r["K"] == 1221
    assert r["N"] == 2456
    assert abs(r["ratio_minus_1_approx"] - 0.0002011206) < 1e-8


def test_logarithmic_resonance_pairs_contains_mediumish_pair():
    pairs = logarithmic_resonance_pairs(math.pi, 10, max_terms=16)
    assert any(p["K"] == 1221 and p["N"] == 2456 for p in pairs)
