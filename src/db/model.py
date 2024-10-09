import json


class Inbound:
    def __init__(self, data):
        self.id = data[0]
        self.user_id = data[1]
        self.up = data[2]
        self.down = data[3]
        self.total = data[4]
        self.remark = data[5]
        self.enable = bool(data[6])
        self.expiry_time = data[7]

        # Конфигурационные поля
        self.listen = data[8]
        self.port = data[9]
        self.protocol = data[10]
        self.settings = json.loads(data[11])
        self.stream_settings = json.loads(data[12])
        self.tag = data[13]
        self.sniffing = json.loads(data[14])

    def __repr__(self):
        return f"<Inbound(id={self.id}, listen={self.listen}, port={self.port}, protocol={self.protocol})>"


class User:
    def __init__(self, client_data):
        self.id = client_data["id"]
        self.flow = client_data["flow"]
        self.email = client_data["email"]
        self.limit_ip = client_data["limitIp"]
        self.total_gb = client_data["totalGB"]
        self.expiry_time = client_data["expiryTime"]
        self.enable = client_data["enable"]
        self.tg_id = client_data["tgId"]
        self.sub_id = client_data["subId"]
        self.reset = client_data["reset"]

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, tg_id={self.tg_id})>"
