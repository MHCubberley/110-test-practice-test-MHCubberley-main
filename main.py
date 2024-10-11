in1 = float(input())
in2 = float(input())
in3 = float(input())

sub = abs(in1-in2)

if sub <= 0.001:
    print('equal')
elif sub <= in3:
    print('close enough')
else:
    print('not close')