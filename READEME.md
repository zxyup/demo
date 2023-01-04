# *This is H1*
***
- >As the saying goes "It's never too,
old to study"!

   - > This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,<br> 
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus. <br>
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus. 

      - > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

1.  >As the saying goes "It's never too,
old to study"!

2. > This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,<br>
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.<br>
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

1. > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.


$ X\stackrel{F}{\longrightarrow}Y $

|Python|Matlab|C++|
|:---:|:--:|:---:|
|6|6|6|
 
[![AzQG3.th.jpeg](https://i.328888.xyz/2022/12/22/AzQG3.th.jpeg)](https://imgloc.com/i/AzQG3)
<!-- ![1.jpg](/res/1.jpg "MM") -->
***
```
import taichi as ti
ti.init(arch=ti.gpu)

@ti.func
def is_prime(n:int):
    result = True
    for k in range(2,int(n**0.5)+1):
        if n % k == 0:
            result = False
            break
    return result

@ti.kernel
def count_primes(n:int)->int:
    count=0
    for k in range(2,n):
        if is_prime(k):
            count += 1
    return count
# print(is_prime(125))
print(count_primes(1000000))
```
***
~~##### This is H2~~
##### This is H3
