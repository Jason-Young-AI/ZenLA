#!/usr/bin/env python

from tornado.options import define, options

define("port", default=8888, help="Zen run on the given port", type=int)

define("mariadb_host", default="localhost", help="Zen database host")
define("mariadb_database", default="Zen", help="Zen database name")
define("mariadb_user", default="root", help="Zen database user")
define("mariadb_password", default="JoYa", help="Zen database password")

define("title", default=u"Zen - Chinese Word Segmentation System", help="Zen title")

Port = options.port

Host = options.mariadb_host
Database = options.mariadb_database
User = options.mariadb_user
Password = options.mariadb_password

Title = options.title