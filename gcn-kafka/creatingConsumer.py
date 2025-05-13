from gcn_kafka import Consumer
consumer = Consumer(client_id='joanalnu',
                    client_secret='Emma23JiC')
print('Trespased point 1')
print(consumer.list_topics().topics)
print('Trespased point 2')

# consumer.subscribe(['gcn.classic.text.FERMI_GBM_FIN_POS',
#                     'gcn.classic.text.LVC_INITIAL'])
# while True:
#     for message in consumer.consume(timeout=1):
#         if message.error():
#             print(message.error())
#             continue
#         print(message.value())