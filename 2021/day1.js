const fs = require('fs')

fs.readFile('input1', 'utf8', (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    lines = data.split('\n')

    var increases = 0
    for (var i = 1; i < lines.length; i++) {
        if ( parseInt(lines[i-1]) < parseInt(lines[i]) ) {
            increases++
        }
    }
    console.log('Part 1:', increases)

    var increases = 0
    for (var i = 1; i < lines.length - 3; i++) {
        var prev_window = [parseInt(lines[i-1]), parseInt(lines[i]), parseInt(lines[i+1])].reduce((a, b) => a + b, 0)
        var curr_window = [parseInt(lines[i]), parseInt(lines[i+1]), parseInt(lines[i+2])].reduce((a, b) => a + b, 0)
        if ( prev_window < curr_window ) {
            increases++
        }
    }
    console.log('Part 2:', increases)
})
