from blockchain import Blockchain 
from blockchain import Transaction
from blockchain import Block
from blockchain import Ledger
import unittest


class TestBlockchain(unittest.Testcase):

    def test_blockchain(self):
        '''test a new blockchain and check it's empty'''
        blockchain = Blockchain()
        assert len(blockchain._blockchain) == 1
        assert blockchain.validate_chain()

        '''Testing a valid block''' 
        transaction1 = Transaction("Alice", "Bob", 10)
        blockchain1 = Block([trans1], bc.get_latest_block_hash())
        assert blockchain.add_block(block1)
        assert len(bc._blockchain) == 2
        assert blockchain.validate_chain()
        assert blockchain._bc_ledger.user_balances["Alice"] == -10
        assert blockchain._bc_ledger.user_balances["Bob"] == 10

        '''Testing an invalid block w/ incorrect previous_block_hash''' 
        transaction2 = Transaction("Charlie", "Dave", 5)
        blockchain2 = Block([transaction2], hash("invalid_hash"))
        assert not bc.add_block(blockchain2)
        assert len(bc._blockchain) == 2
        assert bc.validate_chain()
        assert "Charlie" not in bc._bc_ledger.user_balances

        '''Testing an invalid block w/ empty transactions'''
        blockchain3 = Block([])
        assert not blockchain.add_block(blockchain3)
        assert len(blockchain._blockchain) == 2
        assert blockchain.validate_chain()
        assert "Dave" not in blockchain._bc_ledger.user_balances

        '''adding multiple valid blocks'''
        transaction4 = Transaction("Alice", "Eve", 20)
        transaction5 = Transaction("Bob", "Eve", 15)
        blockchain4 = Block([transaction4, transaction5], bc.get_latest_block_hash())
        assert blockchain.add_block(blockchain4)
        assert len(blockchain._blockchain) == 3
        assert blockchain.validate_chain()
        assert blockchain._bc_ledger.user_balances["Eve"] == 35


        '''distributing mining rewards to users'''
        blockchain.distribute_mining_reward("Alice")
        assert blockchain._bc_ledger.user_balances["Alice"] == 1000
        assert len(blockchain._blockchain) == 4
        assert blockchain.validate_chain()