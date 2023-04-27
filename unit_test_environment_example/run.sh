python3 mk_driver.py $1 > test_driver.c 
gcc -o a.out $2 test_driver.c -fprofile-arcs -ftest-coverage
./a.out
gcov -b -c a-test_driver.c
gcov -b -c a-$2
