var path = require('path'),
    config;

config = {
    // ### Production
    production: {
        url: 'http://my-ghost-blog.com',
        mail: {},
        database: {
            client: 'sqlite3',
            connection: {
                filename: path.join(process.env.GHOST_CONTENT, '/data/ghost.db')
            },
            debug: false
        },
        server: {
            host: '0.0.0.0',
            port: '2368'
        }
    },

    // ### Development **(default)**
    development: {
        // The url to use when providing links to the site, E.g. in RSS and email.
        // Change this to your Ghost blog's published URL.
        url: "http://13.57.234.247:31760",

        // #### Database
        database: {
            client: 'mysql',
            connection: {
              host    : process.env.MYSQL_INTERNAL_SERVICE_HOST,
              user    : process.env.GHOST_DB_USER,
              password  : process.env.GHOST_DB_PASSWORD,
              database  : process.env.GHOST_DB_NAME,
              charset : 'utf8'
            },
            debug: true
        },

        // #### Server
        server: {
            host: '0.0.0.0',
            port: '2368'
        },

        // #### Paths
        // Specify where your content directory lives
        paths: {
            contentPath: path.join(process.env.GHOST_CONTENT, '/')
        }
    },

};

module.exports = config;
