
weight= int(input('What is your Weight? '))
unit=input(' (L)bs or (K)g:  ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print ('You are' + str(converted) + ' Kilos')

else:
    converted = weight / 0.45
    print ('You are ' + str(converted) + ' pounds')
