Nearest Neighbor Approximation Algorithm and how to run it

This will allow you to run the algorithm with the test cases provided and see the output in the console.
python cs412_tsp_approx.py < ./test_cases/test1/input.txt
python cs412_tsp_approx.py < ./test_cases/test2/input.txt
python cs412_tsp_approx.py < ./test_cases/test3/input.txt
python cs412_tsp_approx.py < ./test_cases/test4/input.txt
python cs412_tsp_approx.py < ./test_cases/test5/input.txt

If you want to run all test cases and see the timing of them (not optimality because mine can vary)
bash run_examples.sh

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