
from config import db
from order import Order
from discount import Discount
from finance import Bill,Payment
from saloon import ResTable
from user import Supervisor
from menu import Item

if __name__ == '__main__':
    ItemOrderTemp = Order.item.get_through_model()
    # db.connect()
    # db.close()

    db.create_tables(
        [Bill, Payment,ResTable, Order,Item,Supervisor,Discount,ItemOrderTemp]
    )

