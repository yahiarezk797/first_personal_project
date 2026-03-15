from argon2 import PasswordHasher

ph = PasswordHasher()



print(ph.verify("$argon2id$v=19$m=102400,t=2,p=8$yfLgxAFoM0IBXyFuFWAAxg$oJ4ozEmqdH0hRmWMgrIfzA", input()))
