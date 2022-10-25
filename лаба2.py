from threading import Thread
import hashlib

hash_1="1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad"
hash_2="3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"
hash_3="74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"

first_litter=97

def calculating_hash_0_6():
    for litter_1 in range (7):
        for litter_2 in range (26):
            for litter_3 in range (26):
                for litter_4 in range (26):
                    for litter_5 in range (26):
                        str_password=str(chr(litter_1+first_litter)+chr(litter_2+first_litter)+chr(litter_3+first_litter)+chr(litter_4+first_litter)+chr(litter_5+first_litter))
                        hash_password=hashlib.sha256(str_password.encode('utf-8')).hexdigest()
                        if hash_password==hash_1:
                            print(' multi_treated '+str_password)
                        if hash_password==hash_2:
                            print(' multi_treated '+str_password)
                        if hash_password==hash_3:
                            print(' multi_treated '+str_password)

                                
def calculating_hash_6_12():
    for litter_1 in range (6,13):
        for litter_2 in range (26):
            for litter_3 in range (26):
                for litter_4 in range (26):
                    for litter_5 in range (26):
                        str_password=str(chr(litter_1+first_litter)+chr(litter_2+first_litter)+chr(litter_3+first_litter)+chr(litter_4+first_litter)+chr(litter_5+first_litter))
                        hash_password=hashlib.sha256(str_password.encode('utf-8')).hexdigest()
                        if hash_password==hash_1:
                            print(' multi_treated '+str_password)
                        if hash_password==hash_2:
                            print(' multi_treated '+str_password)
                        if hash_password==hash_3:
                            print(' multi_treated '+str_password)


                                
def calculating_hash_12_18():
    for litter_1 in range (13,19):
        for litter_2 in range (26):
            for litter_3 in range (26):
                for litter_4 in range (26):
                    for litter_5 in range (26):
                        str_password=str(chr(litter_1+first_litter)+chr(litter_2+first_litter)+chr(litter_3+first_litter)+chr(litter_4+first_litter)+chr(litter_5+first_litter))
                        hash_password=hashlib.sha256(str_password.encode('utf-8')).hexdigest()
                        if hash_password==hash_1:
                            print(' multi_treated '+str_password)
                        if hash_password==hash_2:
                            print(' multi_treated '+str_password)
                        if hash_password==hash_3:
                            print(' multi_treated '+str_password)



def calculating_hash_18_25():
    for litter_1 in range (18,26):
        for litter_2 in range (26):
            for litter_3 in range (26):
                for litter_4 in range (26):
                    for litter_5 in range (26):
                        str_password=str(chr(litter_1+first_litter)+chr(litter_2+first_litter)+chr(litter_3+first_litter)+chr(litter_4+first_litter)+chr(litter_5+first_litter))
                        hash_password=hashlib.sha256(str_password.encode('utf-8')).hexdigest()
                        if hash_password==hash_1:
                            print( 'multi_treated '+str_password)
                        if hash_password==hash_2:
                            print(' multi_treated '+str_password)
                        if hash_password==hash_3:
                            print(' multi_treated '+str_password)

def calculating_hash_one_tread():
    for litter_1 in range (26):
        for litter_2 in range (26):
            for litter_3 in range (26):
                for litter_4 in range (26):
                    for litter_5 in range (26):
                        str_password=str(chr(litter_1+first_litter)+chr(litter_2+first_litter)+chr(litter_3+first_litter)+chr(litter_4+first_litter)+chr(litter_5+first_litter))
                        hash_password=hashlib.sha256(str_password.encode('utf-8')).hexdigest()
                        if hash_password==hash_1:
                            print(' one_treated '+str_password)
                        if hash_password==hash_2:
                            print(' one_treated '+str_password)
                        if hash_password==hash_3:
                            print(' one_treated '+str_password)



th1 = Thread(target=calculating_hash_0_6, args=())
th1.start()
th2 = Thread(target=calculating_hash_6_12, args=())
th2.start()
th3 = Thread(target=calculating_hash_12_18, args=())
th3.start()
th4 = Thread(target=calculating_hash_18_25, args=())
th4.start()

calculating_hash_one_tread()
