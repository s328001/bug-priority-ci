from app.priority import get_priority


def test_priority_critical():
    assert get_priority("critical", "always") == "P1"
    assert get_priority("minor", None) == "P3"
