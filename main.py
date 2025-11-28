from src.extract import DataExtractor
from src.transform import DataTransformer
from src.analysis import DataAnalyzer
from src.load import DataLoader

import os

def ensure_output_folder():
    if not os.path.exists("output"):
        os.makedirs("output")

def main():
    ensure_output_folder()

    # Step 1: Extract
    extractor = DataExtractor()
    raw_data = extractor.fetch_products()

    # Step 2: Transform
    transformer = DataTransformer()
    df = transformer.json_to_dataframe(raw_data)

    if df.empty:
        print("No data to process.")
        return

    # Step 3: Analyze
    analyzer = DataAnalyzer()
    insights = analyzer.generate_insights(df)

    with open("output/summary.txt", "w") as f:
        f.write(insights)

    print("Insights generated:\n", insights)

    # Step 4: Load (CSV + SQLite)
    loader = DataLoader()
    loader.save_to_csv(df)
    loader.save_to_sqlite(df)

    print("\nPipeline executed successfully!")

if __name__ == "__main__":
    main()
