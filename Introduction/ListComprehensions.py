if __name__ == '__main__':
    
    x, y, z, n = (int(input()) for _ in range(4))   
    
    # assign variables to input with place holder _ variable in range of number of variables using int(input)
    
    print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])
    
    # algorithm to print matrix coordinates up to the value of x,y,z only if not = to n
