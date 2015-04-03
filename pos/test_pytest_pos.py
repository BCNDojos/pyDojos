import pytest
from pos import POS

def test_simple_list(mock_store):
    pos = POS()
    pos.scan('293002910392', 2)
    assert len(pos.list()) == 1
    pos.scan('098364849832', 10)
    result = pos.list()
    assert len(result) == 2
    assert result[0][0] == '293002910392'
    assert result[0][1] == 2
    assert result[1][0] == '098364849832'
    assert result[1][1] == 10
    
def test_priced_list(article_prices, mock_store):
    pos = POS(article_prices)
    pos.scan('293002910392', 2)
    assert len(pos.list()) == 1
    pos.scan('098364849832', 10)
    result = pos.list()
    assert len(result) == 2
    assert result[0][0] == '293002910392'
    assert result[0][1] == 2
    assert result[0][2] == 5.0
    assert result[0][3] == 10.0
    assert result[1][0] == '098364849832'
    assert result[1][1] == 10
    assert result[1][2] == 0.95
    assert result[1][3] == 9.5