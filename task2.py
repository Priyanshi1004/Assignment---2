from preprocess import preprocess_csv

def recommend_city_to_shutdown(data):
    target_cities = {'Pune', 'Kolkata', 'Ranchi', 'Guwahati'}
    city_stats = {}
    for record in data:
        city = record.get('CITY', '')
        city = city.strip().title()  # Normalise
        if city not in target_cities:
            continue  
        if city not in city_stats:
            city_stats[city] = {
                'claims': 0,
                'rejected': 0,
                'claimed_amt': 0.0,
                'paid_amt': 0.0
            }
        city_stats[city]['claims'] += 1
        try:
            city_stats[city]['claimed_amt'] += float(record.get('CLAIM_AMOUNT', 0.0))
            city_stats[city]['paid_amt'] += float(record.get('PAID_AMOUNT', 0.0))
        except:
            city_stats[city]['claimed_amt'] += 0.0
            city_stats[city]['paid_amt'] += 0.0
        if float(record.get('PAID_AMOUNT', 0.0)) == 0.0:
            city_stats[city]['rejected'] += 1
    city_score = {}
    for city, stats in city_stats.items():
        payout_ratio = stats['paid_amt'] / stats['claimed_amt'] if stats['claimed_amt'] else 0
        rejection_rate = stats['rejected'] / stats['claims'] if stats['claims'] else 0
        city_score[city] = rejection_rate - payout_ratio
    if city_score:
        worst_city = max(city_score, key=city_score.get)
        print("City Recommended for Shutdown:", worst_city)
        print("Stats:")
        print(" - Total Claims:", city_stats[worst_city]['claims'])
        print(" - Claims Rejected:", city_stats[worst_city]['rejected'])
        print(" - Total Claimed Amount: ₹", city_stats[worst_city]['claimed_amt'])
        print(" - Total Paid Amount: ₹", city_stats[worst_city]['paid_amt'])
        print(" - Performance Score:", round(city_score[worst_city], 3))
    else:
        print("No matching city data available for analysis.")

if __name__ == "__main__":
    file_path = 'Insurance_auto_data.csv'  
    data = preprocess_csv(file_path)
    print("Unique cities in dataset:")
    city_set = set()
    for record in data:
        city = record.get('CITY')
        if city:
            city_set.add(city.strip().title())
    print(sorted(city_set))

    recommend_city_to_shutdown(data)
