# Data validation script for customer segments
import pandas as pd
from pathlib import Path

# Load and clean data exactly like in the app
DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_FILE = DATA_DIR / "customer_segments.csv"

SEGMENT_LABELS = {
    0: "High Value",
    1: "Budget Conscious",
    2: "Family Focused",
    3: "Growth Potential",
}

def load_and_validate_data():
    df = pd.read_csv(DATA_FILE)
    
    print("=== BEFORE CLEANING ===")
    print(f"Total records: {len(df)}")
    print(f"Unique cluster values: {sorted(df['Cluster'].unique())}")
    print(f"Cluster data types: {df['Cluster'].dtype}")
    
    # Clean the Cluster column: remove extra characters and convert to int
    df["Cluster"] = df["Cluster"].astype(str).str.strip().str.replace(r'[^0-9]', '', regex=True)
    df["Cluster"] = pd.to_numeric(df["Cluster"], errors='coerce').fillna(-1).astype(int)
    
    # Map clusters to segment names
    df["ClusterName"] = df["Cluster"].map(SEGMENT_LABELS).fillna("Unknown")
    
    print("\n=== AFTER CLEANING ===")
    print(f"Unique cluster values: {sorted(df['Cluster'].unique())}")
    print(f"Cluster data types: {df['Cluster'].dtype}")
    
    print("\n=== SEGMENT DISTRIBUTION ===")
    segment_counts = df["ClusterName"].value_counts()
    print(segment_counts)
    
    print(f"\n=== VALIDATION RESULTS ===")
    unknown_count = (df["ClusterName"] == "Unknown").sum()
    print(f"Unknown segments: {unknown_count}")
    
    if unknown_count == 0:
        print("✅ SUCCESS: All segments properly mapped!")
    else:
        print(f"❌ WARNING: {unknown_count} segments are still unknown")
        
    return df

if __name__ == "__main__":
    df = load_and_validate_data()