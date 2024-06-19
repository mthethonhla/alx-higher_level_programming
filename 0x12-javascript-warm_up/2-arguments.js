!#/usr/bin/node
/* prints a message depending on
 * the number of arguments passed
*/
const args = process.argv;
if (args[2] <= undefined) {
 console.log('No argument');
} else if (args.length === 3 ) {
 console.log('Argument found');
} else {
 console.log('Argument found');
}
