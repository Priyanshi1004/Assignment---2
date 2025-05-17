from preprocess import preprocess_csv

def complex_rejection_classifier(remark):
    if not remark or str(remark).strip() == "":
        return "No Remark"
    remark = remark.lower()
    if "late" in remark or "delay" in remark:
        return "Late Submission"
    elif "fraud" in remark or "false" in remark or "fake" in remark:
        return "Fraudulent Claim"
    elif "document" in remark or "missing" in remark:
        return "Incomplete Documentation"
    elif "policy" in remark or "not covered" in remark:
        return "Policy Limitation"
    elif "duplicate" in remark:
        return "Duplicate Claim"
    elif "unauthorized" in remark or "invalid" in remark:
        return "Unauthorized Claim"
    else:
        return "Other"

def apply_rejection_classification(data):
    for record in data:
        remark = record.get('REJECTION_REMARKS') or record.get('REJECTION REMARKS') or ""
        record['REJECTION_CLASS'] = complex_rejection_classifier(remark)

def print_sample_results(data, limit=10):
    print("Sample Rejection Remark Classifications:\n")
    count = 0
    for record in data:
        remark = record.get('REJECTION_REMARKS', '')
        if remark and remark.strip():
            print(f"Remark: {remark}")
            print(f"Classified As: {record['REJECTION_CLASS']}\n")
            count += 1
        if count >= limit:
            break

if __name__ == "__main__":
    file_path = 'Insurance_auto_data.csv'  
    data = preprocess_csv(file_path)

    apply_rejection_classification(data)
    print_sample_results(data)
