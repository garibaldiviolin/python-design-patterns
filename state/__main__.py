from .classes import Order


order = Order()
order.show_state()  # created

order.proceed()  # shipped
order.proceed()  # delivered
