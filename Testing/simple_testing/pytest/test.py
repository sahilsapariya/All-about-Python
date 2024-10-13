import main

def test_add_positive():
    assert main.add(1, 3) == 4

def test_add_negative():
    assert main.add(-1, -2) == -3


# Run the test using the following command:
# pytest Testing/simple_testing/pytest/test.py
    
# Output:
    
# ============================================================== test session starts ==============================================================
# platform darwin -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
# rootdir: /Users/sahilsapariya/Documents/projects/all about python
# plugins: anyio-3.5.0
# collected 2 items                                                                                                                               

# Testing/simple_testing/pytest/test.py ..                                                                                                  [100%]

# =============================================================== 2 passed in 0.02s ===============================================================