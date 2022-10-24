from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazilian_jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    dict_mock = {
        'title': 'Maquinista',
        'salary': '2000',
        'type': 'trainee'
    }

    assert dict_mock in brazilian_jobs
