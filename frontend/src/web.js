var axios = require('axios');

var web = axios.create({
  baseURL: 'http://localhost:5000',
  /* other custom settings */
});

module.exports = web;
