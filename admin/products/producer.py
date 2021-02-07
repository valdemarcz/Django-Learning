# amqps://lfjntxwl:ajLLnJomCYyxsB1yMZo-dSCdhPl58YSs@hawk.rmq.cloudamqp.com/lfjntxwl

import pika


params = pika.URLParameters('amqps://lfjntxwl:ajLLnJomCYyxsB1yMZo-dSCdhPl58YSs@hawk.rmq.cloudamqp.com/lfjntxwl')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')