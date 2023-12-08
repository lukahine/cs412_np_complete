Nearest Neighbor Approximation Algorithm and how to run it

This will allow you to run the algorithm with the test cases provided and see the output in the console.
python cs412_tsp_approx.py < ./test_cases/test1/input.txt
python cs412_tsp_approx.py < ./test_cases/test2/input.txt
python cs412_tsp_approx.py < ./test_cases/test3/input.txt
python cs412_tsp_approx.py < ./test_cases/test4/input.txt
python cs412_tsp_approx.py < ./test_cases/test5/input.txt

If you want to run all test cases with output then you can do
bash run_examples.sh
This results in output that looks like
Running cs412_tsp_approx.py with input from: test_cases/test1/input.txt
23.0
c a b c
=======================================
Running cs412_tsp_approx.py with input from: test_cases/test2/input.txt
28.0
b d e c a b
=======================================
Running cs412_tsp_approx.py with input from: test_cases/test3/input.txt
26.0
f i j e c b g a d h f
=======================================
Running cs412_tsp_approx.py with input from: test_cases/test4/input.txt
41.0
c k b j i h f d e a l g c
=======================================
Running cs412_tsp_approx.py with input from: test_cases/test5/input.txt
43.0
k l i f g m c j h a e d b k
=======================================

If you want to run all test cases and see the timing of them (not optimality because mine can vary)
bash compute_approx_wallclock.sh

Running that from inside the approx_1 folder in stu results in output like
Test cases:
        test    result  runtime
        test1   failed  .0438618s
        test2   failed  .0413630s
        test3   failed  .0418262s
        test4   failed  .0387306s
        test5   failed  .0383134s
Result is failed because this is testing against exact solution with a specific path, my algorithm may hit the optimal
total weight but may not use the same path to reach that optimal weight, thus failing the test. 
Optimal weights can be reached on Tests 1 and 2. Tests 3, 4, 5 will never hit the optimal weight.

In the Project Description, you have both run_examples.sh and run_test_cases.sh, both do the same thing with doing test cases and showing output.
As such, run_test_cases.sh is simply just run_examples.sh as it does the same thing.