# ntlmIntr
ntlm 爆破脚本
### 使用方法：
##### 安装第三方库
```python
pip install passlib
```
##### 使用方法：
```python
python3 ntmlIntr.py -p 32ed87bdb5fdc5e9cba88547376818d4 -f password.txt
python3 ntmlIntr.py -p 32ed87bdb5fdc5e9cba88547376818d4 -f password.txt -t 50
python3 ntmlIntr.py -p 32ed87bdb5fdc5e9cba88547376818d4 -f password.txt -t 50 -v  (加-v显示过程)

optional arguments:
  -h, --help            show this help message and exit
  -p NTML, --ntml NTML  NTML密文
  -f FILE, --file FILE  本地明文密码字典
  -t THREAD, --thread THREAD
  -v, --verbosity       显示爆破记录
```
