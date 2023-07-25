def test_hello(app, client):
    response = client.get('/hello')
    expected = {'hello': 'world'}

    assert response.status_code == 200
    assert expected == response.get_json()
