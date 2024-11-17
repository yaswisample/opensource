X = int(input())
discount_1 = X * 0.10
amount_after_coupon_1 = X - discount_1
amount_after_coupon_2 = X - 100 
final_amount = min(amount_after_coupon_1,amount_after_coupon_2)
print(int(final_amount))
