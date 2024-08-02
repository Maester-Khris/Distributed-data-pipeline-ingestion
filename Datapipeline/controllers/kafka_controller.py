from flask import Blueprint, render_template, jsonify, request, make_response
from kafka import KafkaProducer

# Kafka producer
# producer = KafkaProducer(
#     bootstrap_servers=['localhost:9092'],
#     value_serializer=lambda x:x.encode('utf-8')
# )

kafka_bp = Blueprint('kafka', __name__)


@kafka_bp.route('/', methods=['GET'])
def produce():
    r="what's up buddy!"
    # producer.send('my-first-kafka-topic', value=r)
    return make_response("message {0} well send to message broker".format(r))

@kafka_bp.route('/close', methods=['GET'])
def close_producing():
    # producer.flush()
    return make_response("all remaining messages have been sent and producer closed")