data = [[int(level) for level in lines.strip().split()] for lines in open("in.txt","r")]
safe_counter = 0
for report in data:
    
    all_decreasing = all( report[i] > report[i+1] for i in range(len(report)-1))
    all_increasing = all( report[i] < report[i+1] for i in range(len(report)-1))
    correct_difference = all( (abs(report[i] - report[i+1]) >= 1 and abs(report[i] - report[i+1]) <= 3) for i in range(len(report)-1))
    
    if (all_increasing or all_decreasing) and correct_difference:
        safe_counter += 1
       
print(f"{safe_counter} reports are safe")