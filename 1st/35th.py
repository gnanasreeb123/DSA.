n=int(input())
board=[['.']*n for _ in range(n)]
ans=[]

def safe(r,c):
    for i in range(r):
        if board[i][c]=='Q':
            return False
        if c-(r-i)>=0 and board[i][c-(r-i)]=='Q':
            return False
        if c+(r-i)<n and board[i][c+(r-i)]=='Q':
            return False
    return True

def solve(r):
    if r==n:
        ans.append([''.join(row) for row in board])
        return

    for c in range(n):
        if safe(r,c):
            board[r][c]='Q'
            solve(r+1)
            board[r][c]='.'

solve(0)

for x in ans:
    print(*x,sep='\n')
    print()