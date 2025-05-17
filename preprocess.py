import csv

def preprocess_csv(filepath):
    data = []

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean_row = {}
            for header, value in row.items():
                value = value.strip() if value and value.strip() != "" else None

                if header in ["CLAIM_AMOUNT", "PAID_AMOUNT", "PREMIUM_COLLECTED"]:
                    try:
                        clean_row[header] = float(value) if value is not None else 0.0
                    except ValueError:
                        clean_row[header] = 0.0
                elif header in ["CLAIM_ID", "CUSTOMER_ID"]:
                    try:
                        clean_row[header] = int(value) if value is not None else None
                    except ValueError:
                        clean_row[header] = None
                else:
                    clean_row[header] = value if value is not None else ""
            data.append(clean_row)
    return data

if __name__ == "__main__":
    filepath = "Insurance_auto_data.csv"
    dataset = preprocess_csv(filepath)

    for row in dataset[:5]:
        print(row)
