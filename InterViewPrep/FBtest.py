# Enter your code here. Read input from STDIN. Print output to STDOUT
def how_many_in_same_pos(L1,L2):
    count = 0
    for i in range(len(L1)):
        if L1[i] == L2[i]:
            count += 1
    return count

testcases=input()
for i in range(testcases):
    meta_s=raw_input()
    meta_sa=meta_s.split()
    meta=map(int, meta_sa)
    num_guesses=meta[-1]
    guess={}
    score={}
    for g in range(num_guesses):
        guess[g]=raw_input()
        guess[g]=guess[g].split()
        guess[g]=map(int, guess[g])
        score[g]=guess[g][-1]
        del guess[g][-1]
    scores=0
    reps=0
    for key, val in score.iteritems():
        scores += int(val)

    for i in range(num_guesses-1):
        reps += how_many_in_same_pos(guess[i], guess[i+1])
    if (scores - reps) > meta[0]:
        print "No"
        continue   
    print "Yes"

    