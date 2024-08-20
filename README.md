# Generative AI Application

original_data_set: ```test_data_social_network.json```

## 1. Overview

The objective is to extract meaningful insights from unstructured social network data using Python and Large Language Models (LLMs). The task is broken down as follows:

### Phase 1: Data Extraction

- **Dataset Review:** Analyze the provided JSON dataset containing social network data.
- **Attribute Extraction:** Develop Python code that leverages LLMs to identify and extract key attributes from unstructured text, such as "brand name" and "product name".
- **Database Schema Design:** Design a relational database schema to store the extracted attributes.
- **Data Insertion:** Insert all identified attributes into the database for subsequent analysis.

### Phase 2: Data Aggregation and Insight Generation

- **SQL Queries:** Write Python code that uses SQL queries to aggregate data and generate insights.
- **Insight Extraction:** Export the generated insights into CSV-formatted text files, such as identifying popular products, brands, and mentioned authors.

### Report Summary

After analyzing the data from approximately 4500 posts, it was found that a few key products and brands dominate the mentions within the dataset. The top mentioned products and brands significantly outweigh others in terms of frequency, indicating a concentrated influence. Additionally, the distribution of posts over time suggests that certain periods saw higher engagement, which could be linked to specific events or trends. The variety in post types, including retweets and replies, highlights the diverse ways users interact with the content.

## 2. Deliverables

The following deliverables are included in this repository:

- **Python Code for Data Extraction:** Located in the `data_extraction/` directory, this code is responsible for parsing the JSON data, extracting relevant attributes using LLMs, and inserting them into the database. Since the project is using GCP Vertex AI API, please first follow the instructions here: https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal
  
- **Database Schema:** The database schema design can be found in the `persistence/` directory.

- **Python Code for Data Aggregation and Insight Generation:** Located in the `data_aggregation/` directory, this code performs SQL-based data aggregation to generate insights, which are then exported to CSV files.

- **Extracted Insight CSV Files:** The generated insights are stored as CSV files in the `CSV_files/` directory.


## 3. Run
1. 
    ```
    pip install -r requirements.txt
    ```
2.
    ```
    python3 main_LLM_extraction.py
    ```
3. 
    ```
    python3 main_data_extraction.py
    ```
4.
    ```
    python3 main_aggregation_and_insight.py
    ```
