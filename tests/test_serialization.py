# from .data.dummy_data import payment, customer

# # 2. Uji model_dump()

# payment_dict = payment.model_dump()

# print(payment_dict)

# # 3. Uji model_dump_json()

# payment_json = payment.model_dump_json()

# print(payment_json)

# # 4. Serialization data sensitif

# print(customer.model_dump())

# # 5. Mengatur field yang keluar dengan include
# # include = ambil field tertentu saja

# customer_test = customer.model_dump(
#     include={
#         "name",
#         "email"
#     }
# )
# print(customer_test)

# # 6. Menghilangkan field dengan exclude
# # exclude = buang field tertentu

# customer_test2 = customer.model_dump(
#     exclude={
#         "password"
#     }
# )

# # 7. Nested Serialization

# response = payment.model_dump(
#     exclude={
#         "order": {
#             "customer": {
#                 "password"
#             }
#         }
#     }
# )

# print(response)