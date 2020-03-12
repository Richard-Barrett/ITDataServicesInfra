config = {
  …
  development: {
    client: 'mysql',
    connection: {
      host    : process.env.MYSQL_INTERNAL_SERVICE_HOST,
      user    : process.env.GHOST_DB_USER,
      password  : process.env.GHOST_DB_PASSWORD,
      database  : process.env.GHOST_DB_NAME,
      charset : 'utf8'
    }
  }
  …
}
