const Discord = require("discord.js")
const fs = require("fs")
var requireDir = require('require-dir');
var dir = requireDir('./');

let helpmessage = '';

module.exports.command = message => {
    //Splices all help strings from all commands into a contiguous message and sends it.
    //TODO: Make help subsets for when there are enough commands that you might want a subset of them.
    message.channel.send("+max Cucumber Giblet", {
            files: [{
                attachment: "./images/ben.png"
                        }]
        })
        .catch(console.error);

}