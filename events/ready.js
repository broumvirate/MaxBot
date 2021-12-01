module.exports = client => {

    console.log("Bot is up and running");
    client.user.setActivity("+help", {
        type: "STREAMING"
    });

}