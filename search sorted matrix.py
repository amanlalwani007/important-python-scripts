def searchsort(matrix,element,up,down,left,right):
    if up>down or right< left:
        return None
    mid_row=int((up+down)/2)
    mid_col=int((left+right)/2)
    mid_elem=matrix[mid_row][mid_col]
    if element==mid_elem:
        return mid_row,mid_col
    elif up==down and left==right:
        return None

    if element>mid_elem:
        right_search=searchsort(matrix,element,up,down,mid_col+1,right)
        if right_search==None:
            #search down
            return searchsort(matrix,element,mid_row+1,down,left,right)

        return right_search
    else:
        left_search=searchsort(matrix,element,up,down,left,mid_col-1)
        if left_search==None:
            #search up
            return searchsort(matrix,element,up,mid_row-1,left,right)
        return left_search
    return None






matrix=[[2,8,9,12],[3,10,11,14],[5,13,16,19]]
element=11
n=len(matrix)
m=len(matrix[0])
print(searchsort(matrix,element,0,n-1,0,m-1))
