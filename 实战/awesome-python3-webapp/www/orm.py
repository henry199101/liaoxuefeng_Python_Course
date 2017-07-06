'''
编写orm模块
'''

import asyncio
import logging
import aiomysql

def log(sql):
	logging.info("SQL: %s"%(sql))

# 创建一个全局的连接池，每个HTTP请求都从池中获得数据库连接
# 连接池由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务
@asyncio.coroutine
def create_pool(loop, **kw): # charset参数是utf8
	logging.info('create database connecting pool...')
	global __pool # 全局变量
	__pool = await aiomysql.create_pool(
		host = kw.get('host', 'localhost'),
		port = kw.get('port', 3306),
		user = kw['user'],
		db = kw['db'],
		password = kw['password'],
		charset = kw.get('charset', 'utf-8'),
		autocommit = kw.get('autocommit', True)
		maxsize = kw.get('maxsize', 10),
		minsize = kw.get('minsize', 1),
		loop=loop
	) # 创建连接所需要的参数

# 用于输出元类中创建sql_insert语句中的占位符
def create_args_string(num):
	L=[]
	for x in range(num):
		L.append('?')
	return ','.join(L)

# 单独封装select，其他insert,update,delete一并封装，理由如下：
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
@asyncio
def select(sql, args, size=None):
	log(sql)
	global __pool # 引入全局变量
	with await __pool as conn: # 打开pool的方法,或-->async with __pool.get() as conn:
		cur = await conn.cursor(aiomysql.DictCursor) # 创建游标,aiomysql.DictCursor的作用使生成结果是一个dict
		await cur.execute(sql.replace('?', "%s"), args or ()) # 执行sql语句，sql语句的占位符是'?',而Mysql的占位符是'%s'
		if size:
			rs = await cur.fetchmany(size)
		else:
			rs = await cur.fetchall()
	await cur.close()
	logging.info('rows returned: %s'%len(rs))
	return rs

# 封装INSTERT,UPDATE,DELETE，老师的做法
@asyncio.coroutine
def execute(sql, args, autocommit=True):
	log(sql)
	with await __pool as conn:
		if not autocommit:
			await conn.begin()
		try:
			async with conn.cursor(aiomysql.DictCursor) as cur:
				await cur.execute(sql.replace('?', '%s'), args)
				affected = cur.rowcount
			if not autocommit:
				await conn.commit()
		except BaseException as e:
			if not autocommit:
				await conn.rollback()
			raise
		return affected

# 定义Field
class Field(object):
	def __init__(self, name, colum_type, primary_key, default):
		self.name = name
		self.colum_type = colum_type
		self.primary_key = primary_key
		self.default = default
	def __str__(self):
		return '<%s,%s:%s>'%(self.__class__.__name__, self.colum_type, self.name)

class StringField(Field):
	def __init__(self, name=None, ddl='varchar(100)', primary_key=False, default=None):
		super(StringField, self).__init__(name, ddl, primary_key, default)

class BooleanField(Field):
	def __init__(self, name=None, ddl='boolean', primary_key=False, default=None):
		super(BooleanField, self).__init__(name, ddl, primary_key, default)

class IntegerField(Field):
	def __init__(self, name=None, ddl='bigint', primary_key=False, default=0):
		super(IntegerField, self).__init__(name, ddl, primary_key, default)

class FloatField(Field):
	def __init__(self, name=None, ddl='real', primary_key=False, default=0.0):
		super(FloatField, self).__init__(name, ddl, primary_key, default)

class TextField(Field):
	def __init__(self, name=None, ddl='Text', primary_key=False, default=None):
		super(TextField, self).__init__(name, ddl, primary_key, default)
# 元类
class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
