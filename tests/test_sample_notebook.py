from testbook import testbook
import pytest

@testbook("notebooks/sample_notebook.ipynb", execute=True)
def test_complement(tb):
    # tb is the testbook instance, it provides access to the functions 
    # in the notebook under test
    complement = tb.get("complement")  # Import function
    assert complement('G') == 'C', "Should have found C"  # Check if function works correctly

@testbook("notebooks/sample_notebook.ipynb", execute=True)
def test_complement_invalid_base(tb):
    complement = tb.get("complement")
    with pytest.raises(Exception, match="X"):
        complement('X')

