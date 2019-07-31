from src.simple_class_exmpl import simple_class

class TestSuperCool():
    def test_action(self):
        sc = simple_class("blr", 15000)
        assert sc.get_data() == ["blr", 15000]
    def test_action1(self):
        sc = simple_class("blr", 15000)
        sc.change_data("clt", 222)
        assert sc.get_data() == ["clt", 222]
    def test_action2(self):
        sc = simple_class("blr", 15000)
        assert sc.get_data() == ["blr", 15000]
        sc.remove()
        assert sc.get_data() == [None, None]




        
# if __name__ == "__main__":       
#     y = TestSuperCool()
#     y.test_action()
#     y.test_action1()
#     y.test_action2()