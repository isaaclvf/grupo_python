# python3 -m unittest ticket_test.py

from ticket import Ticket
from vip_ticket import VIPTicket
import unittest

class TicketTest(unittest.TestCase):
    def test_ticket_str(self):
        ticket = Ticket(20)
        self.assertEqual(str(ticket), "R$ 20.00")

    def test_vip_ticket_str(self):
        vip = VIPTicket(20, 5)
        self.assertEqual(str(vip), "R$ 25.00")