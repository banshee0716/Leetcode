class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_num = 0
        for i in s:
            if i == '(':
                count += 1
                if max_num < count:
                    max_num = count
                    
            if i == ")":
                count -= 1
                
        return(max_num)
        
        
    
    
    """
如果字串滿足以下條件之一，則該字串是有效的括號字串（表示為 VPS）：

它是一個空字串“”，或不等於“(”或“)”的單一字符，
它可以寫成 AB（A 與 B 連接），其中 A 和 B 是 VPS，或者
可以寫成(A)，其中A是VPS。
我們可以類似地定義任何 VPS S 的嵌套深度深度（S），如下所示：
    -深度（“”）= 0
    -height(C) = 0，其中 C 是單一字元不等於「(」或「)」的字串。
    -深度(A + B) = max(深度(A), 深度(B))，其中A和B是VPS。
    -深度("(" + A + ")") = 1 + 深度(A)，其中A 是VPS。

例如，「」、「()()」和「()(()())」是 VPS（嵌套深度為 0、1 和 2），「)(」和「(()」是不是VPS 的。

給定一個表示為字串 s 的 VPS，傳回 s 的嵌套深度。
    """