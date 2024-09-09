def find_missing_delivery(inventory, sales, delivery_list, dec_2019):
    deliveries = []
    j = 0
    for i in range(len(sales)):
        number_of_deliveries = []
        if i == 0:
            # first month
            deliveries_required_per_month = inventory[i] + sales[
                i] + dec_2019  # number of items from inventory of last year.
        else:
            deliveries_required_per_month = inventory[i] + sales[i] - inventory[i - 1]
        deliveries_for_the_month = 0

        '''
        The only additional change is to check at what point the sum of delivery will be greater than delivery required for that month.
        since, we have a missing month, we will add the next element from the delivery list, and so on until a point the sum > what's required,
        this is when we get to know we have a missing month

        if there's no missing month, we would ideally end up matching all the deliveries with deliveries_required,
        '''
        while True:
            if deliveries_required_per_month == deliveries_for_the_month:
                break
            if deliveries_for_the_month > deliveries_required_per_month:

                return f'Delivery is missing for the month {i + 1}'
            elif j >= len(delivery_list):
                return "Delivery is missing for last month "
            else:
                number_of_deliveries.append(delivery_list[j])
                j += 1
                deliveries_for_the_month = sum(number_of_deliveries)
        deliveries.append(number_of_deliveries)
    return deliveries

inventory_2020 = [4, 4, 4, 4]
sales_2020 = [1, 1, 1, 2]
deliveries_2020 = [2, 1, 1, 2]  # removed 3 from the delivery
dec_2019 = 0  # given
find_missing_delivery(inventory_2020, sales_2020, deliveries_2020, dec_2019)
