class CharityMapping:
# ALL CHARITIES HAVE DIFFERENT COLUMN HEADERS AND DATA INPUTS ON THE FILES PROVIDED
    def __init__(self, charity_name, model,file, dict_data):
        self.charity_name = charity_name
        self.model = model
        self.dict_data = dict_data
        self.file = file

    def mapper(self):
        count = 0
        if self.charity_name == 'fourpaws':

            for row in self.dict_data:
                self.model.create(
                    charity_name            = self.charity_name,
                    file_name               = self.file,
                    title                   = row['title'],
                    firstname               = row['forename'],
                    surname                 = row['surname'],
                    add1                    = row['address1'],
                    add2                    = row['address2'],
                    add3                    = row['address3'],
                    town                    = row['town'],
                    county                  = row['county'],
                    postcode                = row['postcode'],
                    country                 = row['country'],
                    card_holders_name       = row['card_holders_name'],
                    bank_account_number     = row['bank_account_number'],
                    first_collection_date   = row['collection_date'],
                    amount                  = row['amount'],
                    frequency               = row['frequency']
                )
                count += 1
        return count