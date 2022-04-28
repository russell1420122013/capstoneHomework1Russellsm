from main import *
import pytest

good_records_list = [Record("hat", 10.25, "clothing"), Record("shirt", 5.25, "clothing"),
                     Record("shoes", 5.25, "clothing"), Record("pants", 10.25, "clothing")]

not_a_records_list = ["jksdjkhksdljhl", "jdljhddlkhdec", "8ouywrr98yfrwrwoihywcr", "98ywo8yo*&T*it(*YT"]

bad_records_list = [Record("j", 0/500, "clothing"), Record("tuf", -100 % 3, "everything else"),
                    Record("t", -889879.2, "iug")]


def test_total_charge_good_data():
    total, err = total_charge("MA", good_records_list)
    assert total == 32.9375, err is None
    total, err = total_charge("ME", good_records_list)
    assert total == 32.705, err is None
    total, err = total_charge("NH", good_records_list)
    assert total == 31.00, err is None


def test_total_charge_bad_data():
    with pytest.raises(AttributeError):
        total_charge("MA", not_a_records_list)


def test_total_charge_edge_data():
    total, err = total_charge("MA", bad_records_list)
    assert total == 0.0, err is not None
    total, err = total_charge("mass", bad_records_list)
    assert total == 0.0, err is not None
