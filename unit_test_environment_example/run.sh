gcc -o a.out triangle.c triangle_driver.c -fprofile-arcs -ftest-coverage 
./a.out
gcov triangle_driver.c -bc