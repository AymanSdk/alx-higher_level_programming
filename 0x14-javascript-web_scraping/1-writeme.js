#!/usr/bin/node
const { Console } = require('console');
const fs = require('fs');
fs.writeFile(process.agrv[2], process.argv[3], (error) => {
	if (error) Console.log(error);
});
