print('*'*40)
print('<<<<<<<<<<<<<<<<<<<< TASK 1 >>>>>>>>>>>>>>>>>>>>>')
print('*'*40)
#1)Demand-Supply Mismatch Analysis
 
zone_regional_zone_weights = {}
with open('FMCGdata.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    zone_index = headers.index('zone')
    regional_zone_index = headers.index('WH_regional_zone')
    product_weight_index = headers.index('product_wg_ton')

    for line in file:
        values = line.strip().split(',')
        zone = values[zone_index]
        regional_zone = values[regional_zone_index]

        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue        
        key = (zone, regional_zone)
        if key in zone_regional_zone_weights:
            zone_regional_zone_weights[key] += product_weight
        else:
            zone_regional_zone_weights[key] = product_weight
for key, total_weight in zone_regional_zone_weights.items():
    print(f'Zone: {key[0]}, Regional Zone: {key[1]}, Total Supply Weight: {total_weight}')
print('*'*40)    
print('<<<<<<<<<<<<<<<<<<<< TASK 2 >>>>>>>>>>>>>>>>>>>>>')
print('*'*40)
#2)Warehouse Refill Frequency Correlation

def convert_capacity_to_numeric(capacity_size):
    size_map = {
        'Small': 1,
        'Mid': 2,
        'Large': 3
    }
    return size_map.get(capacity_size, 0)

capacities = []
refill_requests = []
with open('FMCGdata.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    capacity_index = headers.index('WH_capacity_size')
    refill_index = headers.index('num_refill_req_l3m')
    for line in file:
        values = line.strip().split(',')
        try:
            capacity = convert_capacity_to_numeric(values[capacity_index])
            refill = float(values[refill_index])
            capacities.append(capacity)
            refill_requests.append(refill)
        except ValueError:
            continue
def calculate_correlation(x, y):
    n = len(x)
    if n == 0:
        return None

    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
    denominator_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5

    if denominator_x == 0 or denominator_y == 0:
        return None    
    return numerator / (denominator_x * denominator_y)
correlation = calculate_correlation(capacities, refill_requests)
if correlation is not None:
    print(f"Correlation coefficient: {correlation}")
else:
    print("Insufficient data to compute correlation.")
print('*'*40)
print('<<<<<<<<<<<<<<<<<<<< TASK 3 >>>>>>>>>>>>>>>>>>>>>')
print('*'*40)
#3)Transport Issue Impact Analysis
 
issue_weights = {}
with open('FMCGdata.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    issue_index = headers.index('transport_issue_l1y')
    product_weight_index = headers.index('product_wg_ton')

    for line in file:
        values = line.strip().split(',')
        issue = values[issue_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue 
        if issue in issue_weights:
            issue_weights[issue] += product_weight
        else:
            issue_weights[issue] = product_weight
for issue, total_weight in issue_weights.items():
    print(f'Transport Issue: {issue}, Total Supply Weight: {total_weight}')
print('*'*40)
print('<<<<<<<<<<<<<<<<<<<< TASK 4 >>>>>>>>>>>>>>>>>>')
print('*'*40)
#4)Storage Issue Analysis
 
storage_issue_weights = {}
with open('FMCGdata.csv', mode='r') as file:

    headers = file.readline().strip().split(',')
    issue_index = headers.index('storage_issue_reported_l3m')
    product_weight_index = headers.index('product_wg_ton')

    for line in file:
        values = line.strip().split(',')
        issue = values[issue_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue 
        if issue in storage_issue_weights:
            storage_issue_weights[issue] += product_weight
        else:
            storage_issue_weights[issue] = product_weight

for issue, total_weight in storage_issue_weights.items():
    print(f'Storage Issue: {issue}, Total Supply Weight: {total_weight}')
