from kafka import KafkaConsumer
import _thread

time = ['']

tick_consumer = KafkaConsumer('future.quoteTopic', group_id='kafka-time-diff',
                              bootstrap_servers=[
                                  '10.168.1.2:9092',
                                  '10.168.1.3:9092',
                                  '10.168.1.4:9092'
                              ])

one_min_consumer = KafkaConsumer('future.quoteTopicProcessed_1m', group_id='kafka-time-diff',
                                 bootstrap_servers=[
                                     '10.168.1.2:9092',
                                     '10.168.1.3:9092',
                                     '10.168.1.4:9092'
                                 ])


def update_time(threadName, delay):
    for msg in tick_consumer:
        try:
            time[0] = str(msg.value).split('@')[20]
        except:
            print('warn: ' + str(msg.value))


try:
    _thread.start_new_thread(update_time, ("Thread-1", 2, ))
except:
    print("Error: unable to start thread")

for msg in one_min_consumer:
    one_m_q = str(msg.value).split(',')
    print(time[0] + ' ' + one_m_q[19].split(' ')[1].split('.')[0] + ' ' + one_m_q[0] )
