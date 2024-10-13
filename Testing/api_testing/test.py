from app import app
import pytest 
import mock
import uuid

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def generate_unique_username(base_name):
    return f"{base_name}_{uuid.uuid4()}"


# test for the welcome route '/'
def test_client(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to the API!"}


# test for the add route '/add' (success)
def test_add_numbers(client):
    response = client.post('/add', json={ "num1": 3, "num2": 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 8

# test for the add route '/add/ (failure)
def test_add_numbers_failure(client):
    repsonse = client.post('/add', json={"num1": 5})
    assert repsonse.status_code == 400
    assert repsonse.get_json()['error'] == "Please provide two numbers"



# =========================== route '/register' ===========================
username = generate_unique_username("testing")

def test_register_success(client):
    response = client.post('/register', json={"username": username, "password": "123"})
    assert response.status_code == 201
    assert response.get_json()['message'] == "User added successfully"


def test_register_failure(client):
    response = client.post('/register', json={"password": "123"})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Please provide username"
    
    response = client.post('/register', json={"username": "pranjal"})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Please provide password"

    response = client.post('/register', json={"username": username, "password": "123"})
    assert response.status_code == 409
    assert response.get_json()['error'] == "Username already exist"


# =========================== route '/login' ===========================

def test_login_success(client):
    response = client.post('/login', json={"username": username, "password": "123"})
    assert response.status_code == 200
    assert response.get_json()['message'] == "Login success"

def test_login_failure(client):
    response = client.post('/login', json={"password": "123"})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Please provide username"
    
    response = client.post('/login', json={"username": "pranjal"})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Please provide password"

    response = client.post('/login', json={"username": generate_unique_username("test2"), "password": "123"})
    assert response.status_code == 404
    assert response.get_json()['error'] == "User not found"

    response = client.post('/login', json={"username": username, "password": "1234"})
    assert response.status_code == 401
    assert response.get_json()['error'] == "Invalid credentials"


# =========================== route '/users' ===========================

import warnings

# Suppress specific DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning, module='crypt')


def test_users(client):
    """
        Test the GET /users endpoint 
    """

    # Mock the database connection and cursor
    mock_users = [
        {"id": "1e109300-bca0-4254-ae49-1b6ae1f67dd2", "username": "sahil"},
        {"id": "1e109300-bca0-4254-ae49-1b6ae1f67ge2", "username": "pranjal"}
    ]
    
    def mock_get_db_connection():
            # Mock the connection and cursor behavior
            mock_conn = mock.Mock()
            mock_cursor = mock.Mock()
            mock_cursor.fetchall.return_value = mock_users
            mock_conn.cursor.return_value = mock_cursor

             # Make the mock_conn a context manager
            mock_conn.__enter__ = mock.Mock(return_value=mock_conn)
            mock_conn.__exit__ = mock.Mock(return_value=None)

            return mock_conn

    with mock.patch('app.get_db_connection', mock_get_db_connection):
        response = client.get('/users')

        assert response.status_code == 200

        data = response.json
        assert isinstance(data, dict)
        assert data.get('data') is not None

        # Ensure the response matches the mocked data
        assert data['data'] == mock_users