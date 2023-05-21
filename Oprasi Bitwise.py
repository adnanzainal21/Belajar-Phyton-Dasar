#Operator Bitwise adalah opersi biner atau binary 

a = 9 
b = 5
c = a | b

print('\n=====OR=====')
print('nilai : ',a , ' , binary : ' , format(a,'08b'))
print('nilai : ',b , ' , binary : ' , format(b,'08b'))
print('=====(|)=====')
print('nilai : ',c , ' , binary : ' , format(c,'08b'))

#bitwise And(&)
c = a & b
print('\n=====AND=====')
print('nilai : ',a , ' , binary : ' , format(a,'08b'))
print('nilai : ',b , ' , binary : ' , format(b,'08b'))
print('=====(&)=====')
print('nilai : ',c , ' , binary : ' , format(c,'08b'))

#bitwise XOR(^)
c = a ^ b
print('\n=====XOR=====')
print('nilai : ',a , ' , binary : ' , format(a,'08b'))
print('nilai : ',b , ' , binary : ' , format(b,'08b'))
print('=====(^)=====')
print('nilai : ',c , ' , binary : ' , format(c,'08b'))

#Botwise NOt (~)
c = ~a
print('\n=====NOT=====')
print('nilai : ',a , ' , binary : ' , format(a,'08b'))
print('=====(~)=====')
print('nilai : ',c , ' , binary : ' , format(c,'08b'))

#shifting

#shifting right (>>)
c = a >> 2
print('\n=====SHIFTING=====')
print('nilai : ',a , ' , binary : ' , format(a,'08b'))
print('=====(>>)=====')
print('nilai : ',c , ' , binary : ' , format(c,'08b'))


#shifting ;left (<<)
c = a << 2
print('\n=====SHIFTING=====')
print('nilai : ',a , ' , binary : ' , format(a,'08b'))
print('=====<<)=====')
print('nilai : ',c , ' , binary : ' , format(c,'08b'))

