pk =752767
g =5
p =16777213
c1 ='897EB47587560DE80915BFEC86580F4AD120ECA23E0888DCCE8A1E1B669451F4B3127521FBD70F4816E4977A98E41921C5DAD01742C45EBB624DA2D4759D75FC1C96611F8A4CAF11'

c2 ='1E6121CE60B635D8B59CB982C55F520727D8F62D3F15FD2AF1C213B82D92D5A6B0DA69BB32136C9653F0DEF0BDFD2655E7E54521D852430755AAC2EAEA5C86CC8DACF5A85B2EA6AA'
#c1 ='897EB4'
#c2 ='1E6121'

def isInt(c2,p,x):
    n=1

    while True :
        if (c2+n*p)%x ==0:
            #print('n : {}'.format(n)) 
            return n
        else: n+=1
# g,p,pk are not enough big so we can find private key(a) by testing
# if (g^a) mod p equal to pk, it means it is private key        
def findk(g,p,pk):
    n=1
    while 1:
        if pow(g,n,p) == pk:
            return n            
        n+=1
#n is private key
n=findk(g,p,pk)
print ('private key : ', n)

message=''

for i in range(0,len(c1),6):
    # ElGamal just works with integers
    #first we cut 6 hexa chars and convert them to int
    m1=int(c1[i:i+6],16)
    m2=int(c2[i:i+6],16)
    #to decrypt we have all requirments
    mess=int((m2*(pow(m1,p-n-1,p))%p))
    #to convert to string we have to change to hexa and if lenght is less than 6
    # we add zeros then convert
    #python 2
    message+=hex(mess)[2:].zfill(6).decode('hex')
    #python 3
    #message+=bytes.fromhex(hex(mess)[2:].zfill(6)).decode('utf-8')
    print(message)
print (message) 

