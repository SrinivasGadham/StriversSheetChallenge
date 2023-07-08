def median(a: int, b: int) -> float:
    nums1=a
    nums2=b
    m = len(nums1)
    n = len(nums2)
    
    res = []
    c = 0

    if not nums1:
        if n % 2 == 1:
            return float(nums2[n//2])
        else:
            return float((nums2[n//2] + nums2[n//2 - 1])/2)
    
    if not nums2:
        if m % 2 == 1:
            return float(nums1[m//2])
        else:
            return float((nums1[m//2] + nums1[m//2 - 1])/2)
    if m == 1 and n == 1:
        return float((nums1[0] + nums2[0]) / 2)
    else:
        
        s = (m + n)//2
        e = s+1
        while nums1 or nums2:
            if c == e and (m + n) % 2 == 0:
                return (res[-1] + res[-2])/2
            if c == e and (m+n) % 2 == 1:
                return float(res[-1])

            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    res.append(nums2.pop(0))
                    c += 1
                else:
                    res.append(nums1.pop(0))
                    c += 1
            elif nums1:
                res.append(nums1.pop(0))
                c += 1
            elif nums2:
                res.append(nums2.pop(0))
                c += 1