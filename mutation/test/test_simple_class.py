from src.simple_class_exmple import simple_class

class TestSuperCool():
    def test_action(self):
        sc = simple_class("Dennis", 15000)
        assert sc.get_data() == ["Dennis", 15000]
    def test_action_1(self):
        sc = simple_class("Max", 15000)
        sc.change_data("Mark", 222)
        assert sc.get_data() == ["Mark", 222]
    def test_action_2(self):
        sc = simple_class("Dennis", 15000)
        assert sc.get_data() == ["Dennis", 15000]
        sc.remove()
        assert sc.get_data() == [None, None]
    def test_action_3(self):
        sc = simple_class("Dennis", 15000)
        assert sc.get_data() == ["Dennis", 15000]
        assert sc.value_mutation() == "New Patient"

