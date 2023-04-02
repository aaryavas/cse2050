#invariant- something that is salswayss true at a certain point in our algorithim

def bubble(L):
    n = len(L)
    
    for i in range(n-1):
        for j in range(n-1-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1],L[j]

#invarian- at line 6, at the ith biggest items are in their final, osrted positions

#reason that this algo is correct:
