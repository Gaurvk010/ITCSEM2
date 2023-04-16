grossincome=int(input('enter total income'))
standarddeduction=10000
dependentdeduction=3000*int(input('enter no.of dependent'))
taxableincome=grossincome-standarddeduction-dependentdeduction
print(taxableincome*0.2)