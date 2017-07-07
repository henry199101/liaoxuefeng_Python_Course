import time, uuid

from orm import Model, StringField, FloatField, TextField

def next_id():
	return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
	__table__ = 'users'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	email = StringField(ddl='varchar(50)')
	passwd = StringField(ddl='varchar(50)')
	admin = BooleanField()
	name = StringField(ddl='varchar(50)')
	image = StringField(ddl='varchar(50)')
	created_at = FloatField(defaul=time.time)

class Blog(Model)
	__table__ = 'blogs'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	user_id = StringField(dll='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(ddl='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	created_at = FloatField(default=time.time)

class Comment(Model):
	__table__ = 'blogs'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	user_id = StringField(ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(dll='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	created_at = FloatField(default=time.time)

-- schema.sql

drop database if exists awesome;

create database awesome;

use awesome;

grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data'

create table users (
	`id` varchar(50) not null,
	`email` varchar(50) not null,
	`passwd` varchar(50) not null,
	`admin` bool not null,
	`name` varchar(50) not null,
	`image` varchar(500) not null,
	`created_at` real not null,
	unique key `idx_email` (`email`)
	key `idx_created_at` (`created_at`),
	primary key (`id`)
) engine=innodb default charset=utf-8;

create table comments (
	`id` varchar(50) not null,
	`blog_id` varchar(50) not null,
	`user_id` varchar(50) not null,
	`user_name` varchar(50) not null,
	`user_image` varchar(500) not null,
	`content` mediumtext not null,
	`created_at` real not null,
	key `idx_created_at` (`created_at`),
	primary key (`id`)
) engine=innodb default charset=utf-8;

import orm
from models import User, Blog, Comment

def test():
	yield from orm.created_pool(user='www-data', password='www-data', database='awesome')

	u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')

	yield from u.save()

for x in test():
	pass