def generate_numbers_1( max_num:int ):
    print("Called generate_numbers_1 function")
    numbers = []
    for i in range(1, max_num+1):
        numbers.append(i)
    return numbers

# Generate 객체를 생성하는 함수
def generate_numbers_2( max_num:int ):
    print("Called generate_numbers_2 function")
    for i in range(1, max_num+1):
        yield i


# !!! ↓ 이 코드도 Generate가 된다!!!
gen1 = (i**2 for i  in [1,2,3,4,5])
#       ↑ ↓ 같은 코드임
def make_numbers():
    for i in [1,2,3,4,5]:
        yield i


numbers_1 = generate_numbers_1(10)
numbers_2 = generate_numbers_2(10)
print(numbers_1)
print(numbers_2)








