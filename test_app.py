from application import app

# def test_quick():
#   a = "jeff"
#   greeting = greet(a)
#   assert greeting == "Hi jeff"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
# def test_fast():
#   b = "Bobby"
#   new_greeting = greet(b)
#   assert new_greeting == "Good Evening Bobby"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
