class Solution:
    def isNumber(self, s: str) -> bool:
        
        engine = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$")
        return engine.match(s.strip(" ")) # i prefer this over putting more things (\S*) in regex