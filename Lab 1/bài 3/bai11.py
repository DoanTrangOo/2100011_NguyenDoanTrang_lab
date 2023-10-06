
def commonfun(str1,str2):
    return(len((set(str1)).intersection(set(str2))))

string1="VISHAV"
string2="VANSHIKA"

no_of_common_character=commonfun(string1.lower(),string2.lower())
print("NO. OF COMMON CHRACTERS ARE : ",no_of_common_character)
