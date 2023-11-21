
class RepeatedDigitCalculator:
    def __init__(self):
        print("This python program works out the range of numbers that have repeated digits")
        print("In between starting_number and final_number (they are not included)")

        self.run()

    def get_input(self):
        
        self.starting_number = int(input("Enter in the starting number: "))
        self.final_number = int(input("Enter in the final number: "))

    def make_list_n_z(self):
        range_list = []
        for value in range(self.starting_number + 1,self.final_number):
            range_list.append(value)

        return range_list
        
    def repeated_digit_finder(self,range_list):
        repeated_digit_count = 0
        for item in range_list:
            char_dict = {}
            for char in str(item):
                if char not in char_dict:
                    char_dict[char] = 1    
                elif char in char_dict:
                    char_dict[char] += 1

            for key in char_dict.keys():
                if char_dict[key] > 1:
                    repeated_digit_count += 1
                    break

        return repeated_digit_count
            

    def run(self):
        while True:
            self.get_input()
            range_list = self.make_list_n_z()
            print(range_list)
            repeated_digit_count = self.repeated_digit_finder(range_list)
            print(repeated_digit_count)

            
RepeatedDigitCalculator()
