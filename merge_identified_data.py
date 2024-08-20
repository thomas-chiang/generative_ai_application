def extract_brands_and_products(data, brand_set, product_set):
    # Initialize empty lists to hold the matched brands and products
    brands = []
    products = []
    for product in product_set:
        if product in  data["text"]:
            products.append(product)
    for brand in brand_set:
        if brand in  data["text"]:
            brands.append(product)       
   
    data["brands"] = brands
    data["products"] = products
    
    return data
