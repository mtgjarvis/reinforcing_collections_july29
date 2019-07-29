digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

transform = {} 
for i in range(len(digits)): 
    transform[i+1] = {'French': fr[i], 'English':en[i] }

print(transform)