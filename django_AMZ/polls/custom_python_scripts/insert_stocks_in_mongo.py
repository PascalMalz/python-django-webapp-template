from __future__ import print_function
import mysql.connector



# def stock_records():
#     #Read stock records entry from mysql db
#     cnx = mysql.connector.connect(user='passi', password='Arbeit-0',
#                               host='127.0.0.1',
#                               database='amz_users')
#     cursor = cnx.cursor()
#     query = ("SELECT * FROM stock_records ")
#     cursor.execute(query)
#     stock_records = []
#     for ( stock_record_id, asin_id, asin, stock_amount, created_at ) in cursor:
#             stock_records.append([stock_record_id, asin_id, asin, stock_amount, created_at])
#     cursor.close()
#     cnx.close()
#     return stock_records


# def create_key(key_value):
#     key = 0
#     for char in key_value:
#         key = key + ord(char)
#     return key
    
# def determine_address(key, n):
#     address = key % n
#     return address

# def initiate_hashed_table(n):
#     hashed_table_init = [None for i in range(n)]
#     return hashed_table_init



# def best_sellers():
#     stock_records_array = stock_records()
#     len_stock_records_array = len(stock_records_array)
#     hashed_table = initiate_hashed_table(len_stock_records_array)
#     for entries in stock_records_array[:]:
#         key = create_key(entries[2])
#         address = determine_address(key, len_stock_records_array)
#         found_slot = False
#         try:
#             if hashed_table[address] != None:
#                 while found_slot == False:
#                     if hashed_table[address][0] == entries[2]:
#                         hashed_table[address][1].append([int(str(entries[4])[:10].replace("-","")), entries[3]])
#                         found_slot = True
#                     else: address -= 1

#             else: # = None
#                 hashed_table[address] = [entries[2], [[int(str(entries[4])[:10].replace("-","")) ,entries[3]]]]
#         except:
#             hashed_table[address] = [entries[2], [[int(str(entries[4])[:10].replace("-","")), entries[3]]]]
#     clean_table = []
#     for index, value in enumerate(hashed_table):
#         if value != None:
#             clean_table.append(value)
#     return clean_table


# print (best_sellers())

dbname = my_client['stock_records_by_day']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["mongodb"]

#let's create two documents
medicine_1 = {
    "medicine_id": "RR000123456",
    "common_name" : "Paracetamol",
    "scientific_name" : "",
    "available" : "Y",
    "category": "fever"
      "name": { "first" : "John", "last" : "Backus" },
  "contribs": [ "Fortran", "ALGOL", "Backus-Naur Form", "FP" ]
}
medicine_2 = {
    "medicine_id": "RR000342522",
    "common_name" : "Metformin",
    "scientific_name" : "",
    "available" : "Y",
    "category" : "type 2 diabetes"
}
# Insert the documents
collection_name.insert_many([medicine_1,medicine_2])
