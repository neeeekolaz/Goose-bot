# cmd_source.py

from twitchio.ext import commands
from data_operations import load_data

categories = ['compliment', 'insult']

help_text = (
    "Checks who added an entry to another command. "
    f"Currently checks [{', '.join(categories)}] listings. "
    "Usage: \"!source <compliment or insult> <entry number>\""
)

@commands.command(name='source')
async def cmd_source(ctx, category=None, entry_number=None):
    if category and entry_number:
        if category.lower() in categories:
            data_file_path = f'C:\\Users\\neeee\\Documents\\Python\\goosetavobot\\{category}s.json'
            entries = load_data(data_file_path)

            try:
                entry_number = int(entry_number)
                if 1 <= entry_number <= len(entries):
                    source_username = entries[entry_number - 1]['username']
                    await ctx.send(f"@{source_username} added {category} #{entry_number}.")
                else:
                    await ctx.send(f"{category.capitalize()} #{entry_number} not found.")
            except ValueError:
                await ctx.send("Please provide a valid entry number.")
        else:
            await ctx.send(f"Invalid category. Available categories: {', '.join(categories)}.")
    else:
        await ctx.send("Usage: !source <compliment / insult> <number>.")

def prepare(bot):
    bot.add_command(cmd_source)
