from getpass import getpass

class Password():
    def __init__(self, password) -> None:
        self.score = 0
        if " " in password:
            print("Password should not containe white spaces")
        self.password = password.replace(" ", "")

    def additions(self) -> int:
        symbols = "@#$&_-()=%*:/!?+."
        numbers = "0123456789"

        password_len = len(self.password)
        uppercase_len = sum(map(str.isupper, self.password))
        lowercase_len = sum(map(str.islower, self.password))
        numbers_len = sum(map(str.isdigit, self.password))
        symbols_len = self.password.count(symbols)
        requirements = 0
        try:
            middle_numbers = self.password[1:-1].count(symbols)
            middle_symbols = self.password[1:-1].count(numbers)
        except:
            middle_symbols = middle_symbols = 0

        # if four requirements get fullfiled then we will add requirement score
        if uppercase_len and lowercase_len and numbers_len and symbols_len: requirements = 4
        
        score = (password_len*3) + ((password_len-uppercase_len)*2) + ((password_len-lowercase_len)*2) + (numbers_len*4) + (symbols_len*6) + (requirements*2) + ((middle_numbers + middle_symbols)*2)
        return score
    
    def negatives(self):

        def consecutive_uppercase(string: str) -> int:
            ans = count = 0
            for i in string:
                if i.isupper(): count += 1
                elif count >= 1: ans += count - 1; count = 0
            return ans

        def consecutive_lowercase(string: str) -> int:
            ans = count = 0
            for i in string:
                if i.islower(): count += 1
                elif count >= 1: ans += count - 1; count = 0
            return ans

        def consecutive_numbers(string: str) -> int:
            ans = count = 0
            for i in string:
                if i.isdigit(): count += 1
                elif count >= 1: ans += count - 1; count = 0
            return ans
        
        letters_only = len(self.password) if self.password.isalpha() else 0
        numbers_only = len(self.password) if self.password.isdigit() else 0

        consecutive_upper = consecutive_uppercase(self.password)
        consecutive_lower = consecutive_lowercase(self.password)   
        consecutive_number = consecutive_numbers(self.password)   
        
        score = (letters_only) + (numbers_only) + (consecutive_lower*2) + (consecutive_number*2) + (consecutive_upper*2)
        return score


    def calculate_score(self):
        positive_score = self.additions() 
        negative_score = self.negatives()
        self.score = positive_score - negative_score   


    def get_score(self) -> int:
        self.calculate_score()
        return self.score
    
    def get_complexity(self) -> str:
        if self.score <= 0: return "Too short/invalid"
        elif self.score < 20: return "very weak"
        elif self.score < 40: return "weak"
        elif self.score < 60: return "good"
        elif self.score < 80: return "strong"
        else: return "very strong"

            

if __name__ == "__main__":
    password = getpass("Enter password : ")
    obj = Password(password)

    print("Password Score : ", obj.get_score())
    print("Password Complexity : ", obj.get_complexity())

