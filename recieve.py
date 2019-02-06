import pika
import bson

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.83.229'))
channel = connection.channel()


# ch = channel.queue_declare(queue='qw')


def callback(ch, method, properties, body):
    # print(bson.decode_object(body))
    bson_obj = bson.BSON(body)
    print(bson_obj.decode())

    # print(body)
    # print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='qwe',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# \xa6\x02\x00\x00\x02Type\x00\x14\x00\x00\x00FileOperationRecord\x00\x02Version\x00\x04\x00\x00\x001.0\x00\x02OperationTimeUTC\x00\x1b\x00\x00\x002019-02-05T13:53:41.067000\x00\x02Host\x00\x0f\x00\x00\x00192.168.83.229\x00\x02UserSid\x00\r\x00\x00\x00S-1-5-32-546\x00\x02UserName\x00\x0f\x00\x00\x00BUILTIN\\Guests\x00\x02Operation\x00\x04\x00\x00\x00Ren\x00\x02ObjectType\x00\x05\x00\x00\x00FILE\x00\x02Path\x00"\x00\x00\x00C:\\test\\folder\\subfolder\\file.txt\x00\x02RenamePath\x00%\x00\x00\x00C:\\test\\folder\\subfolder\\newname.txt\x00\x02ProcessOrIp\x00\x0c\x00\x00\x00192.168.1.2\x00\x02ZoneName\x00\t\x00\x00\x00TestZone\x00\x02Protocol\x00\x05\x00\x00\x00CIFS\x00\x02ProtocolVersion\x00\x04\x00\x00\x003.0\x00\x02UncPath\x00!\x00\x00\x00\\\\192.168.1.1\\TESTSHARE\\file.txt\x00\x02RenameUncPath\x00$\x00\x00\x00\\\\192.168.1.1\\TESTSHARE\\newname.txt\x00\x02VolumeId\x00\x0e\x00\x00\x00testvolumeid1\x00\x02OldSecurityDescriptor\x00\x01\x00\x00\x00\x00\x02NewSecurityDescriptor\x00\x01\x00\x00\x00\x00\x02ShareName\x00\n\x00\x00\x00TESTSHARE\x00\x02OldAttributes\x00\x01\x00\x00\x00\x00\x02NewAttributes\x00\x01\x00\x00\x00\x00\x02IsVss\x00\x03\x00\x00\x00No\x00\x00
