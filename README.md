# 後端基礎學習

參考資源: [Willisの後端幼幼班](https://ithelp.ithome.com.tw/users/20151015/ironman/5137)

使用工具:
1. Python, Flask
2. MySQL
3. Visual Studio Code

---

## 筆記

---

### CMD指令

1. py --version -> 查看python版本
2. mkdir folder_name -> 建立資料夾
3. cd path -> 移動到路徑
4. code. -> 開啟VScode


### Python 學習

1. test.py -> main() -> 雙層巢狀迴圈用法

---

### Decorator 裝飾器

※ 參考 decorator.py
[參考資料](https://blog.typeart.cc/%E5%BF%AB%E9%80%9F%E7%90%86%E8%A7%A3%E4%B8%A6%E4%BD%BF%E7%94%A8Python%20Decorator/#%E5%89%8D%E8%A8%80)

規則:

    1. 使用decorator呼叫.__name__時，會變成decorator的名字，在debug時會難以查找問題。
    2. 需from functools import wraps，來重新指向，此為python原生功能，由decorator實現。
    3. 使用 Class-Based Decorator，就不用functools.wraps來重新指向.__name__
    4. 多個decorator使用時，執行順序"由下至上"，靠近的decorator先執行