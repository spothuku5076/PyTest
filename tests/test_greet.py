from source.greet import Greet

def test_greet(monkeypatch):
    def fake_greet(self, name):
        return "Hi, monkey patched!"
    
    # Monkeypatch Greet.greet with fake_greet
    monkeypatch.setattr(Greet, "greet", fake_greet)
    
    g = Greet()
    result = g.greet("Lalitesh")
    assert result == "Hi, monkey patched!"
