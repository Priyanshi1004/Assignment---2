import pandas as pd

#### Dic for mapping
REJECTION_REASONS_MAP = {
    "fake_document": "Fake_document",
    "not_covered": "Not_Covered",
    "policy_expired": "Policy_expired"
}

##### Function 1 #######
def handle_error(error_message):
    print(f"Error: {error_message}")
    return "Errror"

#### Function 2 #########
def contains_rejection_reason(rejection_text, reason):  
    try:
        if rejection_text and isinstance(rejection_text, str):
            return reason in rejection_text.lower()
    except Exception as e:  
        handle_error(f"Error in contains_rejection_reason: {str(e)}")
        return False
    return False

####### Function 3 #######
def map_rejection_reason(rejection_text):
    try:
        if rejection_text and isinstance(rejection_text, str):
            for reason, rejection_class in REJECTION_REASONS_MAP.items():  
                if contains_rejection_reason(rejection_text, reason):  # Check if reason exists in text
                    return rejection_class
            return "Unknown"
        else:
            return "NoRemark"
    except Exception as e:
        handle_error(f"Error in map_rejection_reason: {str(e)}")
        return "Errror"

######## Function 4 ##########
def complex_rejection_classifier(remark_text):
    try:
        if isinstance(remark_text, int) or len(str(remark_text.strip())) == 0:
            return "Invalid Remark"

        ##### Check for each rejection reason
        fake_doc = contains_rejection_reason(remark_text, "fake_document")  
        not_covered = contains_rejection_reason(remark_text, "not_covered")
        policy_expired = contains_rejection_reason(remark_text, "policy_expired")

        if fake_doc:
            return "Fake_document"  
        elif not_covered:
            return "Not_Covered"
        elif policy_expired:
            return "Policy_expired"
        else:
            ### Unknown or null remarks
            return map_rejection_reason(remark_text)
    except Exception as e:
        handle_error(f"Error in complex_rejection_classifier: {str(e)}")
        return "Errror"

df = pd.read_csv("Insurance_auto_data.csv")
df['REJECTION_CLASS'] = df['REJECTION_REMARKS'].apply(
    lambda remark: complex_rejection_classifier(remark) if pd.notna(remark) else 'No Remark'
)
print("Classifications for first 20 non-null REJECTION_REMARKS:")
print(df[['REJECTION_REMARKS', 'REJECTION_CLASS']].loc[df['REJECTION_REMARKS'].notna()].head(20))
