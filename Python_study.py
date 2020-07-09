#%%
# List (테크보이 워니)
x = [4, 2, 3, 1]
y = ["hello", "there"]
# 어느 인덱스에 특정값이 있는지
print(x.index(3))
# 어떤 요소 있는지 없는지 확인
print("hello" in y)

#%%
# Tuple : 리스트와 다른점은, tuple은 안에 애들 못바꿈
x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, "hello", "there")

print(x+y)
# 다음 코드는 에러를 만듬
# x[0] = 10
#%%
# 딕셔너리
x= {
    0:"진오",
    "age":30
}
print(x[0])
print(x["age"])
print(x.keys())
print(x.values())
print("------------절취선----------")
for key in x:
    print("키: " + str(key))
    print("벨류: " + str(x[key]))
print("------------절취선----------")
# 딕셔너리는 mutable하다.
x[0] = "jino"
# 새로운키 삽입도 가능
x["school"] = "columbia"
print(x)
#%% 
# create a class (테크보이 워니)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕 너는 " + to_name + "구나. 나는 " + self.name)

    def introduce(self):
        print("안녕 나는 " + self.name + "야 나는 " + str(self.age) + "살이야.")

jino = Person("진오", 31)
jennie = Person("제니", 30)
jino.say_hello("워니")
jennie.introduce()

# %%
# Inheritance (테크보이 워니)
class Police(Person):
    def arrest (self, to_arrest):
        print ("넌 체포됐다, " + to_arrest)

class Programmer(Person):
    def program (self, to_program):
        print ("다음엔 뭘 만들지? 아 이걸 만들어야겠다: " + to_program)

jino = Person("진오", 31)
jennie = Police ("제니", 21)
wonie = Programmer ("워니", 30)

jennie.introduce()

# %%
def caesarCipherEncryptor(string, key):
	
	for w in string:
		w = chr(ord(w)+key%26)
	
	return "".join(string)

print(caesarCipherEncryptor('cde', 3))
print(chr(ord('e')+27%26))

# %%
board = [[' ',' ',' '] for i in range(3)]
print(board)

# %%
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
x
