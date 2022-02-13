import pymqi

queue_manager = 'QM1'
qmgr = pymqi.connect(queue_manager)

qmgr.disconnect()
