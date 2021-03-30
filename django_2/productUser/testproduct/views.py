from django.shortcuts import render
import pika, json
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from time import sleep
from .task import go_to_sleep
# Create your views here.
class GetProductData(APIView):
    def get(self, request):
        check=request.query_params.get('get', request.data.get("get", None))
        
        
        if check:
            # sleep(5)
            # go_to_sleep.delay(100)
            objects = Product.objects.values()
            return Response(objects)
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
                from .models import Product

                p=Product.objects.create(title=data['title'], image=data['image'])
                p.save()
                
                # all_=Product.objects.values()
                # print('yes created ----->',all_)
                print(data)
            elif properties.content_type == 'product_deleted':
                print('deleted -----<')
                
        channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
        print("started consumming")
        channel.start_consuming()
        channel.close()
        
        
        
        
        
        
        # Product.objects.create()
        return Response("found data")
        