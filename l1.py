total_marks=1000
cutoff=400
scores=[100,200,300,399,500]
year=0

while scores[year] < cutoff:
        print(f"condition: {scores[year] < cutoff}")
        print(f"your scores for this year is : {scores[year]},cutoff is {cutoff}")
        print("i will attempt next year")
        year=year+1
