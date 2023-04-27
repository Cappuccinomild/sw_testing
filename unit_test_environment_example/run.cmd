python .\mk_driver.py triangle_test_cases.txt > triangle_driver.c
gcc -o a.exe triangle.c triangle_driver.c -fprofile-arcs -ftest-coverage
.\a.exe
gcov -b -c a-triangle_driver.c
gcov -b -c a-triangle.c