import requests

def test_app_health_check():
    response = requests.get("http://localhost:5001")
    assert response.status_code == 200
    assert "app" in response.text

# Add more test cases as needed