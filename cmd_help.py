# cmd_help.py

from twitchio.ext import commands

def get_help_text(command_name):
    try:
        command_module = __import__(f"cmd_{command_name.lower()}", globals(), locals(), ['help_text'], 0)
        return getattr(command_module, 'help_text', '')
    except ImportError:
        return ''

@commands.command(name='help', aliases=['commands'])
async def cmd_help(ctx, *args):
    if not args:
        command_list = ", ".join([command.name for command in ctx.bot.commands.values() if isinstance(command, commands.Command)])
        await ctx.send(f"Use \"!help <command>\" for more specific help information. Available commands: {command_list} ")
    else:
        command_name = args[0]
        command = ctx.bot.get_command(command_name)
        if command and isinstance(command, commands.Command):
            help_text = get_help_text(command_name)
            if help_text:
                await ctx.send(help_text)
            else:
                await ctx.send(f"No help text available for command !{command_name}")
        else:
            await ctx.send(f"Command !{command_name} not found. Available commands: {command_list}")

def prepare(bot):
    bot.add_command(cmd_help)
