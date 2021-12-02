const fs = require('fs')

fs.readFile('input2', 'utf8', (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    lines = data.split('\n')

    x1 = 0, y1 = 0
    x2 = 0, y2 = 0, aim = 0
    for (i = 0; i < lines.length; i++) {
        [order, increment] = lines[i].split(' ')
        switch(order) {
            case "forward":
                x1 += parseInt(increment)
                x2 += parseInt(increment)
                y2 += aim * parseInt(increment)
                break
            case "down":
                y1 += parseInt(increment)
                aim += parseInt(increment)
                break
            case "up":
                y1 -= parseInt(increment)
                aim -= parseInt(increment)
                break
        }
    }
    console.log('Part 1:', x1 * y1)
    console.log('Part 1:', x2 * y2)
})
