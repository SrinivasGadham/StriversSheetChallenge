def findCelebrity(n, knows):
    st = []    
    for i in range(n):
        st.append(i)
    
    while len(st) > 1:
        b = st.pop() # assume celeb
        while st and knows(st[-1], b):
            a = st.pop()
        if not st:
            st.append(b)
            
    for i in range(n):
        if i != st[-1] and (not knows(i, st[-1]) or knows(st[-1], i)):
            st.pop()
            break
    
    return -1 if not st else st[-1]