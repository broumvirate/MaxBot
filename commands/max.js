const Discord = require("discord.js")
const PythonShell = require('child_process');
const meatPackage = require('dataimageattachment');
const humanTrafficker = require('process');

//let embossPy = new PythonShell('./python/emboss.py');
//let textPy = new PythonShell('./python/text.py');

module.exports.help = '**+Max:** Consider the trophy.'

module.exports.command = (message, args) => {

    console.log(args.length);
    console.log(message.attachments);

    let childLabor = null;
    let meatGrinder = [];
    let allergies;
    let pig;
    if (message.attachments.size > 0){
        pig = message.attachments.values().next().value.url;
    } else {
        pig = 'fuck off';
    }
    let chicken = args.join(" ");
    console.log(pig)

    console.log('messageattatchmentssize');
    console.log(message.attachments.size);

    switch (message.attachments.size > 0) {

        case true:

            switch (args.length > 0) {

                case true:
                    console.log('biblioblex');
                    allergies = 'biblioblex';
                    break;
                case false:
                    console.log('biblio');
                    allergies = 'biblio';
            }
            break;

        case false:

            console.log(args.length)

            switch (args.length > 0) {

                case true:
                    console.log('blex')
                    allergies = 'blex';
                    break;

                case false:
                    console.log('fuck no')
                    message.channel.send({
                        files: [{
                            attachment: "./images/no.png"
                    }]
                    })
                    .catch(console.error);
                return;
            }


    }
    
    console.log('where"s my hands');
    childLabor = PythonShell.spawn('python3', ['./python/slutterhouse.py', allergies, pig, chicken]);

    childLabor.stdout.on('data', meat => {

        //console.log(meat.toString());
        let dink = "that's all the meat my little chumbatch";
        if (!meat.toString().includes(dink)) {
            console.log(`grand salami in the ass: ${meat.toString().length} inches`);
            meatGrinder.push(meat);
        } else {
            if (meat.length > 38)
                meatGrinder.push(meat.toString().substring(0, 38))
            console.log(`sausage time: ${meat.toString().length} inches, shitting ${meat.toString().substring(0, 38).length} inches`);
            let sausage = meatGrinder.join("");
            console.log(`got ${sausage.length} inch long sausage`)
            //console.log(sausage);
            let packagedMeat = `data:image/png;base64,${sausage}`
            // fs = require('fs');
            // fs.writeFile('/MaxBot/cunt.jpg', packagedMeat);
            //console.log(new meatPackage(packagedMeat, "product.png"));
            message.channel.send({
                    files: [new meatPackage(packagedMeat, "product.png")]
                })
                .catch(console.error);
        }

    });
    childLabor.stderr.pipe(humanTrafficker.stdout);
    /*childLabor.stderr.on('data', finger => {
        console.error(`stderr: ${finger}`);
    });*/

}
