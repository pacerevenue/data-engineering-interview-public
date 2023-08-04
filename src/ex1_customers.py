from databases import CustomerDatabase
from typing import List

"""
Customer Database schema
------------------------

countries                customers
+------------+           +------------------------------------+
|id   |int   +----+      |id        |int                      |
|name |text  |    +-----X|country_id|foreign key(countries.id)|
+------------+           |name      |text                     |
                         +------------------------------------+
                                                              |
bookings                                                      |
+------------------------------------------------+            |
|id                  |int                        |            |
|customer_id         |foreign key(customers.id)  |X-----------+
+-----------------------+------------------------+
                        |
                        |
booked_dates            X
+------------------------------------------------+
|id                  |int                        |
|booking_id          |foreign key(bookings.id)   |
|reserved_night_date |date                       |
|price               |Numeric(10, 2) [Decimal]   |
+------------------------------------------------+
"""


class CustomerDataProvider:
    """
    Manages queries to be run against the customer DB.
    """

    def __init__(self) -> None:
        self.database = CustomerDatabase()

    def list_customers(self) -> List[dict]:
        return self.database.run_query("SELECT name FROM customers")


# -----------------------------------------------------------------
# Example Run
# -----------------------------------------------------------------
def main() -> None:
    provider = CustomerDataProvider()
    result = provider.list_customers()
    for customer in result:
        print(customer)
    print(f"Row Count: {len(result)}")
    print("OK")


if __name__ == "__main__":
    main()
