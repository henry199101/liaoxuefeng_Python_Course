# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000

import re

matchTest = re.match(r'(\w+)@(\w+).com', 'someone@gmail.com')

print(matchTest)