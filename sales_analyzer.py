# PROJECT 3
# SALES DATA ANALYZER

import numpy as np
num_day = int(input('Enter number of days:'))#FOR ROWS
num_products = int(input('Enter number of products:'))#FOR COLUMNS
sales = []#LIST FOR DATA
for i in range(num_day):
    day_sale = []#PER DAY SALE CONTAINER
    print(f'For day {i+1} :')
    for j in range(num_products):
        sale = int(input(f'Sale of product {j+1} : '))
        day_sale.append(sale)
    sales.append(day_sale)
sales_array = np.array(sales)#LIST TO ARRAY CONVERSION
print(sales_array)
#NOW TOTAL SALES
total_revenue = np.sum(sales_array)
print(f'Total revenue for {num_day} days  is : {total_revenue}')

#AVERAGE REVENUE
average_revenue = np.mean(sales_array,axis = 1)
print(f'Average revenue is {average_revenue:.2f}')

# DAILY AVERAGE REVENUE//
daily_revenue = np.sum(sales_array,axis = 1)
daily_av_revenue = np.mean(daily_revenue)
print(daily_av_revenue)

# HIGHEST REVENUE DAY
total_revenue_per_day = np.sum(sales_array,axis = 1)
max_revenue = np.max(total_revenue_per_day)
max_day = np.argmax(total_revenue_per_day)
print(f'Maximum revenue of ${max_revenue} collected on day {max_day+1}')


# LOWEST REVENUE  DAY
min_revenue = np.min(total_revenue_per_day)
min_day = np.argmin(total_revenue_per_day)
print(f'Minimum revenue of ${min_revenue} collected on day {min_day+1}')


# NOW FINDING BEST SELLING PRODUCT
sum_products = np.sum(sales_array,axis = 0)
best_sell = np.max(sum_products)
best_sell_pos = np.argmax(sum_products)
worst_sell = np.min(sum_products)
worst_sell_pos = np.argmin(sum_products)
print(f'Best selling product is product {best_sell_pos+1} sales goes upto ${best_sell}')
print(f'worst selling product is product {worst_sell_pos+1} sales goes upto ${worst_sell}')

# PRODUCT WISE REVENUE
print('Product wise revenue')
pro_sum = np.sum(sales_array,axis = 0)
for i in range(len(pro_sum)):
    print(f'Day {i+1} : ${pro_sum[i]}')

print('Day wise revenue')
day_sum = np.sum(sales_array,axis = 1)
for i in range(len(day_sum)):
    print(f'Day {i+1} : ${day_sum[i]}')

# PRODUCT SUMMARY
print("=" * 50)
print("        SALES DATA ANALYZER REPORT")
print("=" * 50)


print(f'Total revenue:     ${total_revenue}')
print(f'Average daily revenue:    ${daily_av_revenue:.2f}')
print(f'Highest revenue day:   day {max_day+1} ${(max_revenue)}')
print(f'Lowest revenue day:   day {min_day+1} ${(min_revenue)}')
print(f'Best selling product : product{best_sell_pos+1} {(best_sell)}')
print(f'worst selling product : product{worst_sell_pos+1} {(worst_sell)}')

