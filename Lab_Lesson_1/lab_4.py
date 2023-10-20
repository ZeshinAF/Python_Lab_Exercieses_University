start_year = int(input("Start Year: "))
end_year = int(input("End Year: "))
years = []
for year in range(start_year,end_year+1):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        years += [year]
print(years)
print(f'Total : {len(years)}')
