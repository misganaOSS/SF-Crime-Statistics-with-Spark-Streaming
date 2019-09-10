
from pykafka.simpleconsumer import OffsetType
import logging
from pykafka import KafkaClient


logging.getLogger("pykafka.broker").setLevel('ERROR')



consumer_client = KafkaClient(hosts="localhost:9092")

topic = consumer_client.topics['test']

consumer = topic.get_balanced_consumer(
    consumer_group = b'pytkafka-test-2',
    auto_commit_enable = False,
    auto_offset_reset = OffsetType.EARLIEST,
    zookeeper_connect = 'localhost:2181'
)

for mes in consumer:
    if mes is not None:
        print("Message",mes.offset, mes.value)