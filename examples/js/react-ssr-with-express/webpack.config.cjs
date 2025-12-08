const path = require('path');
const webpack = require('webpack');
const htmlWebpackPlugin = require('html-webpack-plugin');

/**
 * Load JS and JSX files through Babel.
 */
const babelLoader = {
    rules: [
        {
            test: /.(js|jsx)$/,
            exclude: /node_modules/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/preset-env',
                        ['@babel/preset-react', {'runtime': 'automatic'}]]
                }
            }
        }
    ]
};

const resolve = {
    extensions: ['.js', '.jsx']
};

const serverConfig = {
    /* Instructs webpack to generate runtime code for a specific environment.
     * Note that webpack runtime code is not the same as the user code you
     * write, you should transpile that code with transpilers like Babel if you
     * want to target specific environments, e.g, you have arrow functions in
     * source code and want to run the bundled code in ES5 environments. Webpack
     * won't transpile them automatically with a target configured.
     * */
    target: 'node',
    /* Providing the mode configuration option tells webpack to use its built-in
     * optimizations accordingly. (production|development|none)
     *
     * https://webpack.js.org/configuration/mode/
     */
    mode: 'production',
    entry: './src/server/server.jsx',
    output: {
        path: path.join(__dirname, '/dist'),
        filename: 'server.cjs',
    },
    /* These options determine how the different types of modules within a
     * project will be treated.
     */
    module: babelLoader,
    plugins: [
        new webpack.EnvironmentPlugin({
            PORT: 3001
        })
    ],
    resolve
};

const clientConfig = {
    target: 'web',
    mode: 'development',
    entry: './src/client/index.jsx',
    output: {
        path: path.join(__dirname, '/dist'),
        /*
         * Appends /static to index.html when looking for client.js
         * This is where Express is serving static files from.
         */
        publicPath: '/static',
        filename: 'client.js',
    },
    module: babelLoader,
    plugins: [
        new htmlWebpackPlugin({
            template: `${__dirname}/src/client/index.html`
        }),
    ],
    resolve
};

module.exports = [serverConfig, clientConfig];
