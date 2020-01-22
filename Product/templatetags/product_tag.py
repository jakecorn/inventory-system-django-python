from django import template

register = template.Library()

@register.simple_tag
def product(num1,num2):
	t = num1*num2
	return  '{:0,.2f}'.format(t)

@register.simple_tag
def money_format(number):
	return  '{:0,.2f}'.format(number)

@register.simple_tag
def product_discount(price,quantity,discount):
	total_discount=0
	if discount>0:
		total_discount = (price *quantity) * (discount/100)
	return  '{:0,.2f}'.format(total_discount)

@register.simple_tag
def subtract_two(a,b):
	difference = a-b
	return  '{:0,.2f}'.format(difference)

@register.simple_tag
def total_payment_format(price,quantity,discount):
	total = (price *quantity) -  ((price *quantity) * (discount/100))
	return  '{:0,.2f}'.format(total)

@register.simple_tag
def total_payment(price,quantity,discount):
	total = (price *quantity) -  ((price *quantity) * (discount/100))
	return  format(total)


@register.tag(name="set")
def set_var(number):
	return number


# @register.simple_tag
# def total_history(table,dealer_id,date,type):
# 	totals = table.objects.raw("select (product_price*product_quantity)*(product_discount/100) as discount, (product_price*product_quantity) - (product_price*product_quantity)*(product_discount/100) as amount, (select date from inventory limit 1)  from inventory where date='2017-10-23' and dealer_id=1")
# 	total_amount=0
# 	total_discount=0
# 	for total in totals:
# 		total_amount+=total.amount
# 		total_discount+=total.discount

# 	if type == "amount":
# 		return total_amount
# 	elif type == "discount":
# 		return total_discount

# 	return 0
