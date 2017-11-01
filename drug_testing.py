# bayesian theorem
# drug testing

true_positive = float(input("True positive rate: "))
true_negative = float(input("True negative rate: "))
popn_drug = float(input("Popn drug user rate: "))

def drug_user(x,y,z):
	return ((x*z) / (((1-x)*(1-z))+(x*z)))

kevin = drug_user(true_positive,true_negative,popn_drug)

print('{0:.2f}'.format(kevin))