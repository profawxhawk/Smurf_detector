if __name__ == "__main__":
    a=[1,2,3,4,5,6,7,8,9,10]
    val=10
    low=0
    high=len(a)
    while low<high:
        mid = (low+high)//2
        if a[mid]>val:
            high=mid-1
        elif a[mid]<val:
            low = mid-1
        else:
            ans=a[mid]
            print(ans)
            exit(0)

