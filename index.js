const { Client, Intents } = require("discord.js");
const TOKEN = process.env.DISCORD_TOKEN;
const client = new Client({
    intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

client.once("ready", () => {
    console.log("Ready!");
});

client.on("messageCreate", (message) => {
    if (!message.author.bot && message.content.toLowerCase().includes("i'm")) {
        const word = message.content.toLowerCase().split("i'm")[1].trim();
        console.log(word);
        message.channel.send(`Hi ${message.author}, I'm ${word}`);
    }
});

client.login(TOKEN);
