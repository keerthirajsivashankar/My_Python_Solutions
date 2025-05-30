def constructlps(txt,lps):
    
    lps[0] = 0
    i = 1
    j = 0
    m = len(txt)
    
    while i < m:
        if txt[i] == txt[j] :
            j += 1
            lps[i] = j 
            i += 1
            
        else:
            if j != 0 :
                j = j-1
            else:
                lps[i] = 0
                i += 1
def search(txt,pat):
    
    n = len(txt)
    m = len(pat)
    i = 0
    j = 0
    lps = [0] * m 
    res = []
    
    constructlps(pat,lps)
    
    while i < n:
        
        if txt[i] == pat[j] :
            
            i+=1
            j+=1 
            
            if j == m :
                res.append(i-j)
                j = lps[j - 1]
        else:
            if j != 0 :
                j = lps[j-1]
            else:
                i += 1
    
    return res 
    
txt = "aabaacaadaabaaba"
pat = "aaba"
res = search(txt,pat)
for i in range(len(res)):
    print(res[i], end=" ")
                