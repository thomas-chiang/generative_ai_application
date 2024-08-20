def extract_brands_and_products(data, brand_set, product_set):
    # Initialize empty lists to hold the matched brands and products
    brands = []
    products = []

    # Split the text into words and check each word against brand_set and product_set
    for word in data["text"].split():
        # Remove punctuation and convert to lowercase for a case-insensitive match
        word_clean = word.strip('.,!?').lower()
        
        if word_clean in brand_set:
            brands.append(word_clean)
        if word_clean in product_set:
            products.append(word_clean)

    # Update the data dictionary with the found brands and products
    if brands:
        data["brands"] = brands
    if products:
        data["products"] = products
    
    return data
