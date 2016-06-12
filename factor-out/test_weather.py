import weather

def test_process_weather(capsys):
    weather.process()
    out, err = capsys.readouterr()
    assert out == "9 32\n"

def test_benchmark_process_weather(benchmark):
    benchmark(weather.process)