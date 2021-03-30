import pika, json
# from .productuser.models import Product
# from testproduct.models import Product
# import os
# from productUser.CRUD import show_data
# print(os.curdir)
# print(os.defpath)
def run()
    params = pika.URLParameters('amqps://jdbfsffv:q0qNYM29La7lp8D-agpQQRa5GLaKyCBp@jellyfish.rmq.cloudamqp.com/jdbfsffv')

    connection = pika.BlockingConnection(params)

    channel = connection.channel()


    channel.queue_declare(queue='main')

    def callback(ch,method,properties, body):
        print("received in main")
        print(body)
        print("properties -- ",properties.content_type)
        
        data = json.loads(body)
        if properties.content_type == 'product_created':
            

            # p=Product.objects.create(title=data['title'], image=data['image'])
            # p.save()
            
            # all_=Product.objects.values()
            # print('yes created ----->',all_)
            print(data)
        elif properties.content_type == 'product_deleted':
            print('deleted -----<')
            
            
    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

    print("started consumming")

    channel.start_consuming()

    channel.close()