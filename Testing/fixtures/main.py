import pytest
import tempfile


@pytest.fixture
def temp_file():
    with tempfile.NamedTemporaryFile() as temp_file:
        yield temp_file.name


def test_main(temp_file):
    """ Test writing to a temporary file """
    with open(temp_file, 'w') as file:
        file.write('Hello, world!')
    with open(temp_file) as file:
        assert file.read() == 'Hello, word!'

# Output:
        
# ============================================================== test session starts ==============================================================
# platform darwin -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
# rootdir: /Users/sahilsapariya/Documents/projects/all about python
# plugins: anyio-3.5.0
# collected 1 item                                                                                                                                

# Testing/fixtures/main.py F                                                                                                                [100%]

# =================================================================== FAILURES ====================================================================
# ___________________________________________________________________ test_main ___________________________________________________________________

# temp_file = '/var/folders/wf/rnr9jl195td0fzmdv233l13m0000gn/T/tmpb2t3k8wf'

#     def test_main(temp_file):
#         """ Test writing to a temporary file """
#         with open(temp_file, 'w') as file:
#             file.write('Hello, world!')
#         with open(temp_file) as file:
# >           assert file.read() == 'Hello, word!'
# E           AssertionError: assert 'Hello, world!' == 'Hello, word!'
# E             - Hello, word!
# E             + Hello, world!
# E             ?           +

# Testing/fixtures/main.py:16: AssertionError
# ============================================================ short test summary info ============================================================
# FAILED Testing/fixtures/main.py::test_main - AssertionError: assert 'Hello, world!' == 'Hello, word!'
# =============================================================== 1 failed in 0.08s ===============================================================