gcc -o a.out -fprofile-arcs -ftest-coverage triangle.c triangle_driver.c
./a.out
gcov triangle_driver.c -bc