require("dotenv").config()
const Discord = require("discord.js")
const client = new Discord.Client()
const fs = require("fs")
var requireDir = require('require-dir');
var commands = requireDir('../commands');

const prefix = "+";

module.exports = (client, message) => {
    //Check if message should be processed.
    if (!message.content.startsWith(prefix) || message.author.bot) {
        return
    }
    //Break message into component parts and pass to relevant module.
    const args = message.content.split(" ");
    const command = args[0].substr(prefix.length);
    args.shift();
    
    fs.access(`./commands/${command}.js`, function (err) {
        if (err) {
            message.channel.send("Still don't know what that is, buddy.");
        } else {
            commands[command].command(message, args);
        }
    });
}
