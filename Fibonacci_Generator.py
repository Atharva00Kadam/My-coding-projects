Golden_ratio = 1.618
# Using the fibonacci formula of sequence
# then rounding off to nearest int.
# use array_1 and increase it to n_numbers if required.
Phi_ratio = -0.618
array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for array in array_1:
    formula = (Golden_ratio)**array - (Phi_ratio)**array
    formula_2 = formula/2.2360679775
    rounded_int = round(formula_2)
    print(rounded_int)
