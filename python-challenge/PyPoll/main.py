import csv #Import csv module

with open ('election_data.csv') as csvfile: 

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    Ballot_ID=[] 
    County=[] 
    Candidate=[] 
    candidatenames=[] 
    totaleachcan=[] 
    resultprintcan=[] 
    totaleachcanperc=[] 

    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    
    for row in csvreader:
        Voter_ID=row[0] 
        County=row[1]
        Candidate=row[2] 
        Voter_ID.append(Voter_ID) 
        County.append(County) 
        Candidate.append(Candidate) 
    
    line_count= len(Voter_ID)
    

candidatenames.append(Candidate[0]) 


for loop1 in range (line_count-1):
    if Candidate[loop1+1] != Candidate[loop1] and Candidate[loop1+1] not in candidatenames:
        candidatenames.append(Candidate[loop1+1])

n=len(candidatenames)


for loop2 in range (n): 
    totaleachcan.append(Candidate.count(candidatenames[loop2])) 


loservotes=line_count 

for loop3 in range(n): 
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 4)}%') 
    if totaleachcan[loop3]>winnervotes:
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]
    if totaleachcan[loop3]<loservotes: 
        loser=candidatenames[loop3]
        loservotes=totaleachcan[loop3]


for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})')

resultlines='\n'.join(resultprintcan) 


analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
Last: {loser} :(\n\
----------------------------\n'

print(analysis) #Output results on screen

file1=open("pypoll.txt","w") 
file1.writelines(analysis)
file1.close() 