"""" function with hinting
 hinting is basically for developer to provide some hint"""
def sub(n1:int,n2:int):
    """
    :param n1: int (Hint is given)
    :param n2: int( Hint is given
    :return: Nothing (None)
    """
    print(f"{n1} - {n2} = {n1-n2}")

sub(8,2)
sub(5.5,2.2)
print(sub.__doc__)