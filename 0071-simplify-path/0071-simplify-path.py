class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        new_path = []
        for index, ele in enumerate(arr):
            if ele == '.':
                continue
            elif ele == '..':
                if new_path:
                    new_path.pop()
            elif ele == '':
                continue
            else:
                new_path.append(ele)
        
        
        return "/"  + "/".join(new_path)
                
            
            
            
            
            
            
            
            
'''         
規範路徑應具有以下格式：
該路徑以單斜杠“/”開頭。
任何兩個目錄都由一個斜杠“/”分隔。
該路徑不以尾隨“/”結尾。
該路徑僅包含從根目錄到目標文件或目錄的路徑上的目錄（即沒有句點“.”或雙句點“..”）

'''