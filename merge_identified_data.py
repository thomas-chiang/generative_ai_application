from util import clean_string
from deserialize import product_set, brand_set
from extract_from_orginal import parsed_data

def extract_brands_and_products(data, brand_set, product_set):
    # Initialize empty lists to hold the matched brands and products
    brands = []
    products = []
    cleaned_data =  clean_string(data["text"])
    for product in product_set:
        if product in  cleaned_data:
            products.append(product)
    for brand in brand_set:
        if brand in  cleaned_data:
            brands.append(brand)       
   
    data["brands"] = brands
    data["products"] = products
    
    return data

merged_data = [extract_brands_and_products(data, brand_set, product_set) for data in parsed_data]

print(merged_data[:5])
