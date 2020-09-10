Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from cryptography.fernet import Fernet
>>> key=Fernet.generate_key()
>>> print(key)
b'w1qPeqDntbfU5-y5hZ6LhP44Nm-uKmmrPeWYitqykCU='
>>> file=open('k.key','wb')
>>> file.write(key)
44
>>> file.close()
>>> file=open('key.txt','wb')
>>> file.write(key)
44
>>> file.close()
>>> file=open('key.txt','rb')
>>> file.read()
b'w1qPeqDntbfU5-y5hZ6LhP44Nm-uKmmrPeWYitqykCU='
>>> message="talha habib"
>>> encode=message.encode()
>>> f=Fernet(key)
>>> encryted=f.encrypt(encode)
>>> print(encrypted)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(encrypted)
NameError: name 'encrypted' is not defined
>>> print(encryted)
b'gAAAAABewdT_g10k-VQ0rn5bZPYUaftiTvvkXYkyP7JhgVSmBzYDUtozjAm0Tg0cNQgQVPXzXMDkDqR4LSiFmWZICKPjpKXn1Q=='
>>> f2=Fernet(key)
>>> decrypted=decrypted=f2.decrypt(encryted)
>>> print(decrypted)
b'talha habib'
>>> 
