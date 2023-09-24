class Converter:
    factor = 1.60934

    @staticmethod
    def convert_miles_to_kilometers(miles):
        return miles * Converter.factor
