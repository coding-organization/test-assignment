import sys
from pathlib import Path
import pytest
import numpy as np

parent_dir = str(Path(__file__).parent.parent)  # Adjust based on your structure
print(parent_dir)
sys.path.insert(0, parent_dir)

from assignment import find_students

@pytest.fixture
def get_results():
    num_arr = np.loadtxt("tests/num_arr.csv", delimiter=",")
    return num_arr

def test_shape(get_results):
    num_arr = get_results
    num_arr = np.int64(num_arr)
    
    for i in num_arr:
        test_table = np.int64(np.loadtxt("tests/test_table"+str(i)+".csv", delimiter=",", skiprows=1))
        true_res = np.int64(np.loadtxt("tests/true_res"+str(i)+".csv", delimiter=","))
        std_res1, std_res2 = find_students(test_table)
        true_res1 = true_res[:-1]
        true_res2 = true_res[-1]

        assert std_res1.shape == true_res1.shape

        
def test_dtype_arr(get_results):
    num_arr = get_results
    num_arr = np.int64(num_arr)
    
    for i in num_arr:
        test_table = np.int64(np.loadtxt("tests/test_table"+str(i)+".csv", delimiter=",", skiprows=1))
        true_res = np.int64(np.loadtxt("tests/true_res"+str(i)+".csv", delimiter=","))
        std_res1, std_res2 = find_students(test_table)
        true_res1 = true_res[:-1]
        true_res2 = true_res[-1]

        assert std_res1.dtype == true_res1.dtype

        
def test_values_arr(get_results):
    num_arr = get_results
    num_arr = np.int64(num_arr)
    
    for i in num_arr:
        test_table = np.int64(np.loadtxt("tests/test_table"+str(i)+".csv", delimiter=",", skiprows=1))
        true_res = np.int64(np.loadtxt("tests/true_res"+str(i)+".csv", delimiter=","))
        std_res1, std_res2 = find_students(test_table)
        true_res1 = true_res[:-1]
        true_res2 = true_res[-1]

        assert std_res1.all() == true_res1.all()


def test_scalar_dtype(get_results):
    num_arr = get_results
    num_arr = np.int64(num_arr)
    
    for i in num_arr:
        test_table = np.int64(np.loadtxt("tests/test_table"+str(i)+".csv", delimiter=",", skiprows=1))
        true_res = np.int64(np.loadtxt("tests/true_res"+str(i)+".csv", delimiter=","))
        std_res1, std_res2 = find_students(test_table)
        true_res1 = true_res[:-1]
        true_res2 = true_res[-1]

        assert type(std_res2) == type(true_res2)


def test_scalar_values(get_results):
    num_arr = get_results
    num_arr = np.int64(num_arr)
    
    for i in num_arr:
        test_table = np.int64(np.loadtxt("tests/test_table"+str(i)+".csv", delimiter=",", skiprows=1))
        true_res = np.int64(np.loadtxt("tests/true_res"+str(i)+".csv", delimiter=","))
        std_res1, std_res2 = find_students(test_table)
        true_res1 = true_res[:-1]
        true_res2 = true_res[-1]

        assert std_res2 == true_res2
        
        
"""        
def test_shapes(get_results):
    r1, r2 = get_results
    assert r1.shape == r2.shape

def test_dtype(get_results):
    r1, r2 = get_results
    assert r1.dtype == r2.dtype
    
def test_values(get_results):
    r1, r2 = get_results
    assert r1.all() == r2.all()
"""
