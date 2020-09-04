c = input("Enter temperature: ")
c = float(c)
f = float(c*9/5)+32.0
f1 = float(c)
f1 = float(f1)
c2 = float(f1-32)*5/9



unit = input("Enter unit in F/f or C/c: ")
if unit == "C" or unit == "c" :
  print(f"{c}° in Celsius is equivalent to {f}° Farenheit. ");
elif unit == "F" or unit == "f" :
  print(f"{f1}° in Farenheit is equivalent to {c2}° Celsius." );
else:
  print(f" Invalid unit ({unit}).")


