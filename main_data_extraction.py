from data_extraction.function import (
    parse_dataset,
    find_products_and_brands_in_LLM_results,
    transform_data_set,
    insert_into_sql_db,
)

parsed_data_set = parse_dataset()
brand_set, product_set = find_products_and_brands_in_LLM_results()
transformed_data_set = transform_data_set(parsed_data_set, brand_set, product_set)
insert_into_sql_db(transformed_data_set)
