import MySQLdb
import urllib.request
import json
import requests


class Product:

    def __init__(self, antibody_name, rate_count, current_rating):
        self.antibody_name = antibody_name
        self.rate_count = rate_count
        self.current_rating = current_rating


class ProductDB:

    def __init__(self, host_name, user_name, password, db_name):
        """ This function gets db params and connects to the db"""

        try:
            self.db = MySQLdb.connect(host = host_name, user = user_name, passwd = password, db = db_name)
            self.cursor = self.db.cursor()

        except Exception as e:
            print("Failed to connect to the db: ", e)
            raise

    def createTable(self):
        """ This function creates the Auctions table if it doesn't exist """

        try:
            if self.tableExists("antibodies"):
                print("antibodies table already exists")
                return

            table = """CREATE TABLE antibodies(
                 ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                 antibody_name VARCHAR(200) NOT NULL,
                 rate_count INT,
                 current_rating INT)"""
            self.cursor.execute(table)

        except Exception as e:
            print("Failed to create the auctions table: ", e)
            raise

    def tableExists(self, table_name):
        """ This function gets table name and returns True if it exists, else returns False """

        try:
            exp = "SHOW TABLES LIKE '" + table_name + "'"
            self.cursor.execute(exp)
            result = self.cursor.fetchone()

            if result:
                return True

            else:
                return False

        except Exception as e:
            print("Failed to check if table " + table_name + "exists: ", e)
            raise

    def addProduct(self, Product):
        """ T... """

        antibody_record = self.antibodyExists(Product)
        if antibody_record:
            print("Antibody '" + Product.antibody_name + "' already exists")
            if self.updateAntibodyRecord(Product, antibody_record):
                print("Domain auction details were updated")

        try:
            self.cursor.execute("INSERT INTO auctions(domain_name, bid_count) VALUES('%s', '%d')" % (Product.antibody_name, Product.rate_count))
            self.db.commit()

        except Exception as e:
            print("Failed to insert the parameters into the db table: ", e)
            raise

    def antibodyExists(self, Product):
        """ This function gets domain auction record and returns current record info if it's exists in the db, else returns False """

        try:
            self.cursor.execute("SELECT * FROM antibodies WHERE antibody_name = '" + Product.antibody_name + "'") #TODO: add site name
            self.db.commit()
            antibody_record = self.cursor.fetchone()

            if antibody_record:
                return antibody_record
            else:
                return False

        except Exception as e:
            print("Failed to check if domain's name '" + Product.antibody_name + "' exists : ", e)
            raise

    def updateAntibodyRecord(self, Product, antibody_record):
        """dd........"""

        # ind_record_id = 0
        ind_antibody_name = 1
        ind_rate_count = 2

        if antibody_record[ind_rate_count] != Product.rate_count: #TODO: add other factors
            try:
                self.cursor.execute("UPDATE auctions SET bid_count Product= " + str(Product.rate_count) + " WHERE domain_name = '" + antibody_record[ind_antibody_name] + "'")
                self.db.commit()
                return True

            except Exception as e:
                print("Failed to update domain's record " + antibody_record[ind_antibody_name] + ": ", e)
                raise

        else:
            return False

    def deleteTable(self, table_name):
        """ This function gets table name and delete it if it exists"""

        if self.tableExists(table_name):
            try:
                self.cursor.execute("DROP TABLE " + table_name)
                self.db.commit()
                print("Table '" + table_name + "' was deleted")
            except Exception as e:
                print("Failed to delete table: ", e)
                raise
        else:
            print("Table '" + table_name + "' do not exist")


if __name__ == "__main__":
    domains_db = ProductDB("localhost", "root", "", "antibody_rating")
    # domains_db.createAuctionsTable()
    # domain_auction = DomainAuction("ResumesLive.com", 4)
    # domains_db.addAuction(domain_auction)
    # print(domains_db.auctionExists(domain_auction))
    # domains_db.deleteTable("auctions")
    # updateFlippaListings(domains_db)
    # print(domains_db.domainExists("ebookbell.com"))
    # updateDropCatchListings(domains_db)
