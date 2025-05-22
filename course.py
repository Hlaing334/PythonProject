weight = int(input ("Weight:"))
unit = input ("(K)g or (L)bs:")
if unit== "K":
    converted = weight / 0.45
    print(str(converted))
elif unit == "L":
    converted = weight * 0.45
    print(str(converted))
