import math

amt = raw_input("Enter the bill amount:")
amt = float(amt)
print "Bill Amount:", amt
cgst = amt*(9.0/100.0)
print "CGST(9%):", cgst
sgst = amt*(9.0/100.0)
print "SGST(9%):", sgst
total = amt + cgst + sgst
print "Total Bill Amount = Bill Amount + CGST + SGST :", total
