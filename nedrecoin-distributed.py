from flask import Flask
from flask import request

this_nodes_transactions = []

@node.route('/txion', methods=['POST'])
def trancaction():
    if request.method == 'POST':
        new_txion = request.get_json()
        this_nodes_transactions.append(new_txion)
        print "New Trancaction"
        print"FROM: {}".format(new_txion['from'])
        print "TO: {}". format(new_txion['to'])
        print "AMOUNT: {}\n".format(new_txion['amount'])
        return "Trancaction submission successful\n"

node.run()