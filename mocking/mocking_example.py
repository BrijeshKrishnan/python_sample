class MockSample:
    def sum(self, a, b):
        return a + b
        
    def sum_mock(self, a, b):
        self.keep_waiting()
        return a + b
    def keep_waiting(self):
        import time
        time.sleep(10)