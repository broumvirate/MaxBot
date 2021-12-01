require("dotenv").config()
const Discord = require("discord.js")
const client = new Discord.Client()
const fs = require("fs")


//Process files in events folder as event handlers.
fs.readdir("./events/", (err, files) => {
  files.forEach(file => {
    console.log(`./events/${file}`);
    if (file != '.DS_Store') {
    const eventHandler = require(`./events/${file}`)
    const eventName = file.split(".")[0]
    client.on(eventName, arg => eventHandler(client, arg))
    }
  })
})

client.login(process.env.BOT_TOKEN)

