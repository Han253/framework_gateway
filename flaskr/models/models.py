#import sqlite3
from flaskr.db import get_db
from flaskr.popyo.device import Device


class DeviceModel():

    @staticmethod
    def get_all():
        db = get_db()
        devices = db.execute(
            'SELECT p.id, tagGlobal, name, device_type, description'
            ' FROM device p'
            ' ORDER BY name DESC'
            ).fetchall()
        return devices
    
    @staticmethod
    def get_device_tag(tag):
        db = get_db()
        device_cursor = db.execute(
                'SELECT id, tagGlobal, name, device_type, description'
                ' FROM device'
                ' WHERE tagGlobal == ?',(tag,)
            ).fetchone()
        device = Device()
        device.set_cursor(device_cursor)
        return device
    

    @staticmethod
    def create_device(device):
        db = get_db()
        db.execute(
            'INSERT INTO device (tagGlobal, name, device_type, description)'
            ' VALUES (?, ?, ?, ?)',
            (device.tag, device.name, device.device_type, device.description)
        )
        db.commit()