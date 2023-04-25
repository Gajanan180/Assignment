class Probability:
    def __init__(self, days):
        if type(days) == 'int':
            raise TypeError("Days argument should be of integer type!!!")
        self.days = days
        self.present_in_class = self.present_in_classes()
    
    def number_of_ways_to_attend_classes(self):
        return len(self.present_in_class)

    def probability_to_miss_gradution_ceremony(self):
        chances_of_miss_graduation = self.chances_of_missing_graduation()
        return f'{len(chances_of_miss_graduation)}/{self.number_of_ways_to_attend_classes()}'

    def present_in_classes(self):
        list1 = []
        pattern = ""
        self._util(self.days, pattern, list1)
        print('List of probability of that student he/she will absent/present in class = ', list1)
        return list1
    
    def _util(self, days, pattern, list1):
        if days == 0:
            list1.append(pattern)
        else:
            self._util(days - 1, pattern + 'A', list1)  # student absent in class
            self._util(days - 1, pattern + 'P', list1)  # student present in class
    
    def chances_of_missing_graduation(self):
        missing_graduation = []
        for i in self.present_in_class:
            if "AAAA" in i:
                missing_graduation.append(i)
        print('The student is absent for 4 or more consecutive days = ', missing_graduation)
        return missing_graduation
