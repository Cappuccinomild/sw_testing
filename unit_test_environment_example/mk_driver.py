#coverage 측정에서 gcove(지 코브)를 사용?
#shell script입력을 통해 .c 파일과 .txt파일을 받는다
#testcase 파일에 주석이 있을수도 있다
import sys

testcase_file = sys.argv[1]

entire_code = [
    "#include <stdlib.h>",
    "#include <stdio.h>",
    "#include <string.h>"
    ]

f = open(testcase_file, "r")


#첫줄이 주석인 경우 체크
line = f.readline()
line = line.strip()  # 공백 제거

if line.startswith('//'):  # 한 줄 주석 처리
    line = f.readline()

elif line.startswith('/*'):  # 여러 줄 주석 처리
    while '*/' not in line:  # 주석의 끝을 찾을 때까지 읽기
        line = f.readline().strip()
        
    line = f.readline()
    line = line.strip()  # 공백 제거

function_declare = line

#세미콜론 여부 검사
if function_declare.find(";") == -1:
    function_declare += ";"

#코드에 함수 선언부 추가
entire_code.append(function_declare)

entire_code.append("int main(){\n")

function_name = function_declare.split(" ")[1]

#여는괄호 포함
function_name = function_name[:function_name.find("(") + 1]

line = f.readline()
while line:

    #주석인 경우 체크
    line = line.strip()  # 공백 제거

    if line.startswith('//'):  # 한 줄 주석 처리
        line = f.readline()
        continue

    elif line.startswith('/*'):  # 여러 줄 주석 처리
        while '*/' not in line:  # 주석의 끝을 찾을 때까지 읽기
            line = f.readline().strip()
            
        line = f.readline()
        line = line.strip()  # 공백 제거
    params = line.strip().replace("\n", "").split(" ")
    
    test_no = params[0]
    expected_result = params[-1]

    params = params[1:-1]


    entire_code.append('\tif( ' + function_name + ','.join(params) + ') == '+ expected_result +')  printf("test case '+ test_no +': pass\\n");')
    entire_code.append('\telse printf("test case '+ test_no + ': Fail\\n");')

    line = f.readline()


entire_code.append("\treturn 0;")
entire_code.append("}")

print("\n".join(entire_code))
