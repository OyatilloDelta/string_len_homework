def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    x=len(s1)
    y=len(s2)
    z=len(s3)
    if x%2==0:
        c=print("[s1]")
    if y%2==0:
        c=print("[s2]")
    if z%2==0:
        c=print("[s3]")
    if x%2!=0:
        c=print("[s1 toq]")
    if y%2!=0:
        c=print("[s2 toq]")
    if z%2!=0:
        c=print("[s3 toq]")
    



    return c 
print(main("asd","asdf","asdfgh"))