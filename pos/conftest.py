import pytest

@pytest.fixture
def article_prices():
    return {
                '293002910392': 5.0,
                '098364849832': 0.95,
    }

@pytest.fixture
def mock_store(request, monkeypatch):
    locked = [('293002910392', 2), ('098364849832', 10)]
    def mocklock(pos, code, quantity):
        if (code, quantity) not in locked:
            pytest.fail('Locked items not valid')
        return None
    monkeypatch.setattr('store.Store.lock', mocklock)