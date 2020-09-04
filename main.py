c = input("Enter temperature: ")
c = float(c)
f = float(c*9/5)+32.0



unit = input("Enter unit in F/f or C/c")
if unit == "F" or unit == "f" :
  print(f"{c}° in Celsius is equivalent to {f}° Farenheit. ");
elif unit == "C" or unit == "c" :
  print(f"{c}° in Celsius is equivalent to {f}° Farenheit." );
else:
  print(f"  Invalid unit ({unit}).")


