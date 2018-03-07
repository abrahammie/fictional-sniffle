const webpack = require('webpack');

const config = {
    entry:  __dirname + '/client/src/main.js',
    output: {
        path: __dirname + '/client/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
        {
          test: /\.jsx?/,
          exclude: /node_modules/,
          use: 'babel-loader'
        },
      ]
      presets: ['es2015', 'react'],
    },
};

module.exports = config;