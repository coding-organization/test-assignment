import sys
from pathlib import Path
import pytest
import numpy as np

parent_dir = str(Path(__file__).parent.parent)  # Adjust based on your structure
print(parent_dir)
sys.path.insert(0, parent_dir)

from assignment import find_students

"""
def csv_gen():
    test_scores = np.int64(np.random.rand(5,4)*100)
    test_ids = np.int64(np.random.rand(5,1)*1000000 + 8999999)
    test_table = np.hstack((test_ids, test_scores))
    header_row = "Student ID,Math,Physics,Chemistry,Selective"
    np.savetxt("test_table.csv", test_table, delimiter=",", header=header_row, comments="", fmt="%d")
"""

@pytest.fixture
def get_results():
    in_arr = np.array([[0,1],[2,3]])
    r1 = find_students(in_arr)
    r2 = in_arr[:,0] + in_arr[:,1]
    return r1, r2

def test_shapes(get_results):
    r1, r2 = get_results
    assert r1.shape == r2.shape

def test_dtype(get_results):
    r1, r2 = get_results
    assert r1.dtype == r2.dtype
    
def test_values(get_results):
    r1, r2 = get_results
    assert r1.all() == r2.all()
