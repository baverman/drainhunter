from drainhunter import snapshot, get_new_objects, group_by_class

class AAA: pass
class BBB: pass

def test_snapshot_must_memorize_new_objects():
    snapshot()

    a = AAA()
    b = BBB()
    result = list(get_new_objects())
    assert a in result
    assert b in result

    c = BBB()
    result = list(get_new_objects())
    assert a in result
    assert b in result
    assert c in result

def test_group_by_class():
    snapshot()
    a = AAA()
    b = BBB()
    c = BBB()

    result = group_by_class()
    assert result['tests.test_drainhunter.BBB'] == [b, c]
    assert result['tests.test_drainhunter.AAA'] == [a]