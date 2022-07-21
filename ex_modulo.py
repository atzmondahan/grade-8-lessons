
# Understanding Modulo in Python



# Story
# Joe works at an apple farm and he uses his net to carry apples. 
# Joe is paid when his net is full of apples.
# The variable a stands for the number of apples available.
# The variable n stands for the number of apples his net can hold.
# Use the modulo equation to determine how many apples remain.

# Example A
a = 5
n = 2
print (f"The answer to Example {str(a)}%{str(n)}={a % n}")

# Example B
a = 5
n = 3
print (f"The answer to Example {str(a)}%{str(n)}={a % n}")

# Example C
a = 10
n = 3
print (f"The answer to Example {str(a)}%{str(n)}={a % n}")

# Example D
a = 9
n = 3
print (f"The answer to Example {str(a)}%{str(n)}={a % n}")

# Example E
a = 3
n = 0
print (f"The answer to Example {str(a)}%{str(n)} is Zero Division Error")
# This will create an error feel free to remove the hash from the next line.
#pprint (f"The answer to Example {str(a)}%{str(n)}={a % n}")

# Example F
a = 2
n = 10
print (f"The answer to Example {str(a)}%{str(n)}={a % n}")

#apple farm example
# def apple_ex(str,a,n):
# print (f"The answer to Example {str} is ", a % n)

# a=549
# b=5
# mod=a-((a//b)*b)
# print("mod=",{mod})
# print(a%b)


# print(f"20%5={20%5}")
# print(f"21%5={21%5}")
# print(f"22%5={22%5}")
# print(f"23%5={23%5}")
# print(f"24%5={24%5}")
# print(f"25%5={25%5}")
# print(f"26%5={26%5}")
# print(f"27%5={27%5}")
# print(f"28%5={28%5}")
# print(f"29%5={29%5}")
# print(f"30%5={30%5}")
# print(f"31%5={31%5}")
# print(f"32%5={32%5}")
# print(f"33%5={33%5}")
# print(f"34%5={34%5}")
# print(f"35%5={35%5}")

# print(21%5)
# print(22%5)
# print(23%5)
# print(24%5)
# print(25%5)
# print(26%5)
# print(27%5)
# print(28%5)
# print(29%5)
# print(30%5)
# print(31%5)
# print(32%5)
# print(33%5)
# print(34%5)
# print(30%5)

def cycle_f(start,end):
  for i in range (20,35):
    chr=str(i)
    print(f"{chr}%5={i%5}")
  
def formula_mod(a,b):
  c=a//b
  c=c*b
  mod=(a-c)
  print(f"formula result={mod}")
  print(f"modulo result={a%b}")


