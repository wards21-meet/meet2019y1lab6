def fizzbuzz(n):
  result=[]
  for count in range(1,n):
    if count % 3==0 and count % 5==0:
      result.append("FizzBuzz")
    elif count % 3==0 :
      result.append("Fizz")
    elif count % 5==0 :
      result.append("Buzz")
    else:
      result.append(count)
    if count==n-1:
        return(result)

    





print(fizzbuzz(9))


