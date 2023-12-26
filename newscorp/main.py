from newscorp.modules.data_modules import HitlogInputRow
from newscorp.modules.data_processor import (
    get_top_articles,
    process_influential_articles,
)
from newscorp.modules.file_handler import read_file, write_file

INPUT_FILE_PATH = "data/input/sample_hitlog.csv"
OUTPUT_FILE_PATH = "data/output/top.csv"

# Read input file
rows = read_file(INPUT_FILE_PATH, HitlogInputRow)

# Process data
article_stats = process_influential_articles(rows)
top_articles = get_top_articles(article_stats, 3)

# Write output file
write_file(OUTPUT_FILE_PATH, top_articles)
