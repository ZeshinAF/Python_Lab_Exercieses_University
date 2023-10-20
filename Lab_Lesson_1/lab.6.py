start_number = int(input("Enter start number: "))
end_number = int(input("Enter end number: "))
even_numbers = []
odd_numbers = []
for number in range(start_number,end_number+1):
    if number % 2 == 0:
        even_numbers += [number]
    else:
        odd_numbers += [number]
print(f"Even numbers: "+str(even_numbers))
print(f"Odd numbers: "+str(odd_numbers))