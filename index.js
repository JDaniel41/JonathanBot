const { Client, Intents } = require("discord.js");
const TOKEN = "ODE3ODc5ODA5NDQyNDQ3NDEw.YEP77g.7N4woRwrOmHyIBBWH-DBSGQOqPU"; //process.env.DISCORD_TOKEN;

const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

client.once("ready", () => {
    console.log("Ready!");
});

console.log(process.env);
console.log(TOKEN);
client.login(TOKEN);
