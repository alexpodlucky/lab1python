c = input("Enter temperature: ")
c = int(c)
f = int(c*9/5)+32



unit = input("Enter unit in F/f or C/c")
if unit == "F" or unit == "f" :
  print(f"{c}° in Celsius is equivalent to {f}° Farenheit. ");
elif unit == "C" or unit == "c" :
  print(f"{c}° in Celsius is equivalent to {f}° Farenheit." );
else:
  print(f"Invalid unit ({unit}).")


