# from Predict import prediksi as pre
from app import app
import pytest
from PIL import Image
import base64
import io


@pytest.fixture
def client():
    return app.test_client()

def test_index(client):
    res = client.get('/')
    expected = "Software Defect Prediction"
    assert res.status_code == 200
    assert expected in res.get_data(as_text=True)
    
def test_predictPage(client):
    file = "app.py"
    
    data = {
        'predictFile' : (open(file, 'rb'), file)
    }
    res = client.post('/predict', data=data)
    expected = "Buggy"
    assert res.status_code == 200
    assert expected in res.get_data(as_text=True)