# Data Access Objects:
# All of these are meant to be Singleton


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, vaccine):
        self._conn.execute("""INSERT INTO vaccines (id, date, supplier, quantity) VALUES ( ?, ?, ?, ?)""", [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])

    def find(self, vaccine_id):
        c = self._conn.cursor()
        c.execute("""SELECT id FROM vaccines WHERE  id =?""", [vaccine_id])


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""INSERT INTO suppliers (id, name, logistic) VALUES (?, ?, ?)""",
                           [supplier.id, supplier.name, supplier.logistic])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""SELECT id FROM suppliers WHERE  id =?""", [supplier_id])


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""INSERT INTO clinics (id, location, demand, logistic) VALUES ( ?, ?, ?, ?)""",
                           [clinic.id, clinic.location, clinic.demand, clinic.logistic])

    def find(self, clinic_id):
        c = self._conn.cursor()
        c.execute("""SELECT id FROM clinics WHERE  id =?""", [clinic_id])

    def find_demand_by_location(self, location, amount):
        c = self._conn.executr()
        demand = c.execute("""SELECT demand FROM clinics WHERE location=?""", [location])
        demand = demand - amount


class _Logistics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, logistic):
        self._conn.execute("""INSERT INTO logistics (id, name, count_sent, count_received) VALUES (?, ?, ?, ?)""",
                           [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])

    def find(self, logistic_id):
        c = self._conn.cursor()
        c.execute("""SELECT id From logistics WHERE id =?""", [logistic_id])

